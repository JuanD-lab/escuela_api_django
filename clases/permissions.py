from rest_framework.permissions import BasePermission

class ClasesPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST' and not request.user.is_staff:
            return False
        
        return True
