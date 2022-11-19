def get_user_group_permission(user, permission_name):
    return user.groups.filter(name=permission_name)
