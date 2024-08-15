from django.core.exceptions import PermissionDenied


class UserIsAssignedMixin:
    def dispatch(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.assigned_to != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
