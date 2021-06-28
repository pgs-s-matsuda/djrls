from rest_framework import routers

from rest.views import CustomerViewSet

router = routers.DefaultRouter()
router.register(r'customer', CustomerViewSet)
