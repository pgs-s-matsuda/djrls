from django.db import connection
from django.http import HttpResponseForbidden

from myapp.models import AppPermission

class RlsMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        tenant_id = getattr(request.user, 'tenant_id', None)
        info = request.path_info
        sp = info.split('/')
        view = sp[1]
        if tenant_id:
            with connection.cursor() as cursor:
                cursor.execute(f'SET ROLE "{tenant_id}" ')
                try:
                    permission = AppPermission.objects.get(tenant_id=tenant_id, view = view)
                except AppPermission.DoesNotExist:
                    return HttpResponseForbidden()

        response = self.get_response(request)
        return response
