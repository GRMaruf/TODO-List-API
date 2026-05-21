from django.urls import path
from .views import *

#
# Applied url versioning

#

urlpatterns = [
    path('v1/', ListTodo.as_view()),
    path('v1/<int:pk>/', DetailTodo.as_view())
]

from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register("v2", TodoViewSet, basename='todos')
urlpatterns+=router.urls