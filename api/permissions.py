from . import command
from .const import permissions as permissions_name

from rest_framework import permissions


class CanViewListProducts(permissions.BasePermission):
    def has_permission(self, request, view):
        print(view)
        user = request.user
        if request.method in permissions.SAFE_METHODS:
            if self.has_view_products_permission(user):
                return True
        return False

    def has_view_products_permission(self, user):
        view_permission = command.get_user_group_permission(user, permissions_name.CAN_VIEW_PRODUCTS)
        return view_permission.exists()


class CanEditProducts(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if self.has_edit_products_permission(user):
            return True
        return False

    def has_edit_products_permission(self, user):
        edit_permission = command.get_user_group_permission(user, permissions_name.CAN_EDIT_PRODUCTS)
        return edit_permission.exists()

    