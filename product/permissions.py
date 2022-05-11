from rest_framework import permissions

#Only author of the object can change
class IsProductOwner(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if obj.market.user.pk == request.user.pk:
            return True
        return False


#Only author of the object can change
class IsMoveProductOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if obj.product.market.user.pk == request.user.pk:
            return True
        return False


#Only author of the object can change
class IsReturnedProductOwner(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if obj.product.market.user.pk == request.user.pk:
            return True
        return False


class IsCategoryOwner(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if obj.sub_category.product.market.user.pk == request.user.pk:
            return True
        return False


class IsSubCategoryOwner(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if obj.product.market.user.pk == request.user.pk:
            return True
        return False


class IsTrashProductOwner(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if obj.market.user.pk == request.user.pk:
            return True
        return False

























