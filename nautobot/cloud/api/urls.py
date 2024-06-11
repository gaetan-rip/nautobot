from nautobot.core.api.routers import OrderedDefaultRouter

from . import views

router = OrderedDefaultRouter(view_name="Cloud")

# Cloud Accounts
router.register("cloud-accounts", views.CloudAccountViewSet)
router.register("cloud-networks", views.CloudNetworkViewSet)
router.register("cloud-network-prefix-assignments", views.CloudNetworkPrefixAssignmentViewSet)
router.register("cloud-types", views.CloudTypeViewSet)

app_name = "cloud-api"
urlpatterns = router.urls