from .models import *
from fast_model.import_libs import *

def add_user(request_user, username, password, email=None, user_type='customer', company=None, 
             description=None, address=None, phone=None, phone2=None, 
             longitude=None, latitude=None, permission_group=None):
    if not request_user.custom.can_add_custom_user:
        raise PermissionDenied
    user = User.objects.create_user(username=username, email=email, password=password)
    custom_user = CustomUser.objects.create(
        user=user, 
        user_type=user_type, 
        company=company,
        description=description,
        address=address,
        phone=phone,
        phone2=phone2,
        longitude=longitude,
        latitude=latitude,
        permission_group=permission_group
    )
    return custom_user

def edit_user(request_user, custom_user, username=None, password=None, email=None, 
              user_type=None, company=None, description=None, address=None, 
              phone=None, phone2=None, longitude=None, latitude=None, 
              permission_group=None):
    if not request_user.custom.can_edit_custom_user:
        raise PermissionDenied
    
    user = custom_user.user
    if username: user.username = username
    if email: user.email = email
    if password: user.set_password(password)
    user.save()
    
    if user_type: custom_user.user_type = user_type
    if company: custom_user.company = company
    if description: custom_user.description = description
    if address: custom_user.address = address
    if phone: custom_user.phone = phone
    if phone2: custom_user.phone2 = phone2
    if longitude is not None: custom_user.longitude = longitude
    if latitude is not None: custom_user.latitude = latitude
    if permission_group: custom_user.permission_group = permission_group
    
    custom_user.save()
    return custom_user

def delete_user(request_user, custom_user):
    if not request_user.custom.can_delete_custom_user:
        raise PermissionDenied
    custom_user.is_active = False
    custom_user.save()
    return True

def add_permission_group(request_user, name, description, **kwargs):
    if not request_user.custom.can_add_permission_group:
        raise PermissionDenied
    permission_group = PermissionGroup.objects.create(name=name, description=description, **kwargs)
    return permission_group

def edit_permission_group(request_user, permission_group, name=None, description=None, **kwargs):
    if not request_user.custom.can_edit_permission_group:
        raise PermissionDenied
    if name: permission_group.name = name
    if description: permission_group.description = description
    for key, value in kwargs.items():
        setattr(permission_group, key, value)
    permission_group.save()
    return permission_group

def delete_permission_group(request_user, permission_group):
    if not request_user.custom.can_delete_permission_group:
        raise PermissionDenied
    permission_group.delete()
    return True
