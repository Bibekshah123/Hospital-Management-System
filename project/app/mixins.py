from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden


class OwnerRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.created_by != request.user:
            raise PermissionDenied("You do not have permission to access this.")
        return super().dispatch(request, *args, **kwargs)