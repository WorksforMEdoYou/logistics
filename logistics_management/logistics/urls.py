from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, ShipperViewSet, ConsignmentViewSet

router = DefaultRouter()
router.register('customers', CustomerViewSet, basename='customer')
router.register('shippers', ShipperViewSet, basename='shipper')
router.register('consignments', ConsignmentViewSet, basename='consignment')

urlpatterns = router.urls
