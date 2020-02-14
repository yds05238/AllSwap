from django.urls import path

from products.api.views import ProductViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', ProductViewSet, basename='products')

urlpatterns = router.urls