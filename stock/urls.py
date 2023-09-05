from django.urls import path,include
from .views import PurchaseView
from rest_framework import routers
  # 'PurchaseView' adını doğru şekilde içe aktardığınızdan emin olun
router=routers.DefaultRouter()
router.register("purchase/<int:pk>",PurchaseView)
urlpatterns = [
    path('', include(router.urls)),
]