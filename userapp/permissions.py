from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS

class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        
        if request.user == obj.owner:
            return True

        return False


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        
        if request.method in SAFE_METHODS or request.user == obj.owner:
            return True

        return False


class IsAdminUserOrReadOnly(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS or request.user.is_superuser:
            return True
        
        return False
