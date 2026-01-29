from .models import *
from fast_model.import_libs import *

def add_base_cash(name, description):
    base = BaseCash.objects.create(name=name, description=description)
    return base

def add_cash(base, currency, start_amount):
    cash = Cash.objects.create(base=base, currency=currency, start_amount=start_amount)
    return cash

def edit_cash(cash, name=None, description=None, start_amount=None):
    if name: cash.base.name = name
    if description: cash.base.description = description
    if start_amount: cash.start_amount = start_amount
    cash.save()
    return cash

def delete_cash(cash):
    cash.is_active = False
    cash.save()
    return True

def add_person_account(person, currency, start_amount):
    person_account = PersonAccount.objects.create(person=person, currency=currency, start_amount=start_amount)
    return person_account

def edit_person_account(person_account, start_amount=None):
    if start_amount: person_account.start_amount = start_amount
    person_account.save()
    return person_account

def delete_person_account(person_account):
    person_account.is_active = False
    person_account.save()
    return True

def add_base_payment_source(name, description):
    base = BasePaymentSource.objects.create(name=name, description=description)
    return base

def edit_base_payment_source(base_payment_source, name=None, description=None):
    if name: base_payment_source.name = name
    if description: base_payment_source.description = description
    base_payment_source.save()
    return base_payment_source

def delete_base_payment_source(base_payment_source):
    base_payment_source.is_active = False
    base_payment_source.save()
    return True

def add_payment_source(base, name, description, source_type):
    payment_source = PaymentSource.objects.create(base=base, name=name, description=description, source_type=source_type)
    return payment_source

def edit_payment_source(payment_source, name=None, description=None, source_type=None):
    if name: payment_source.name = name
    if description: payment_source.description = description
    if source_type: payment_source.source_type = source_type
    payment_source.save()
    return payment_source

def delete_payment_source(payment_source):
    payment_source.is_active = False
    payment_source.save()
    return True

def auto_conversion(from_currency, to_currency, amount, currency_value):
    if from_currency == to_currency:
        return amount
    base_currency = Currency.objects.filter(is_base=True).first()
    if not base_currency and currency_value == 0 and amount == 0:
        return amount
    if from_currency != base_currency and to_currency == base_currency:
        return amount * currency_value
    elif from_currency == base_currency and to_currency != base_currency:
        return amount / currency_value
    elif from_currency == base_currency and to_currency == base_currency:
        return amount
    else:
        return amount * currency_value

@transaction.atomic
def add_payment_for_person(person, cash, amount, payment_type, currency, currency_value, payment_source, description):
    if payment_type != payment_source.source_type:
        raise ValueError("Payment type and source type must be the same")
    person_account = PersonAccount.objects.filter(person=person, currency=currency).first()
    if not person_account:
        person_account = add_person_account(person, currency, 0)
    payment = Payment.objects.create(person_account=person_account, cash=cash, amount=amount, payment_type=payment_type, currency=currency, currency_value=currency_value, payment_source=payment_source, description=description)
    if currency != cash.currency:
        if payment_type == "in":
            conversion = Conversion.objects.create(from_currency=currency, to_currency=cash.currency, currency_value=currency_value)
            payment.conversion = conversion
            cash_amount = auto_conversion(currency, cash.currency, amount, currency_value)
        else:
            conversion = Conversion.objects.create(from_currency=cash.currency, to_currency=currency, currency_value=currency_value)
            payment.conversion = conversion
            cash_amount = auto_conversion(cash.currency, currency, amount, currency_value)
    else:
        cash_amount = amount
    if payment_type == "in":
        payment.person_old = person_account.amount
        payment.cash_old = cash.amount
        person_account.amount -= amount
        cash.amount += cash_amount
        payment.person_new = person_account.amount
        payment.cash_new = cash.amount
    else:
        payment.cash_old = cash.amount
        payment.person_old = person_account.amount
        person_account.amount += amount
        cash.amount -= cash_amount
        payment.person_new = person_account.amount
        payment.cash_new = cash.amount
    person_account.save()
    cash.save()
    return payment

@transaction.atomic
def add_payment_for_source(cash, amount, payment_type, currency, currency_value, payment_source, description):
    if payment_type != payment_source.source_type:
        raise ValueError("Payment type and source type must be the same")
    payment = Payment.objects.create(cash=cash, amount=amount, payment_type=payment_type, currency=currency, currency_value=currency_value, payment_source=payment_source, description=description)
    if payment_type == "in":
        payment.cash_old = cash.amount
        cash.amount += amount
        payment.cash_new = cash.amount
    else:
        payment.cash_old = cash.amount
        cash.amount -= amount
        payment.cash_new = cash.amount
    cash.save()
    return payment