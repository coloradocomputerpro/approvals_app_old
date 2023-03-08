from rest_framework import permissions


class IsProgramMemberOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow members of a Program to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request, so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Only allow write permissions if the user is a member of the Program.
        return obj.program.members.filter(id=request.user.id).exists()
