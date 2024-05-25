from django . urls import path, include
from . import views
from . views import index
from . views import MyModelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'mymodel', MyModelViewSet)

urlpatterns = [
    path("", index, name='index'),
    path("cardlist", views.CardListView.as_view(), name="card-list"),
    path('api/', include(router.urls)),
    path("new", views.CardCreateView.as_view(), name="card-create"),
    path("edit/<int:pk>", views.CardUpdateView.as_view(), name="card-update"),
    path("box/<int:box_num>", views.BoxView.as_view(), name="box"),
]