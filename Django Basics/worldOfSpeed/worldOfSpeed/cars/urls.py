from django.urls import path, include

from worldOfSpeed.cars.views import CarCreateView, CarCatalogueView, CarDetailsView, CarEditView, CarDeleteView

urlpatterns = [
    path('create/', CarCreateView.as_view(), name='create-car'),
    path('catalogue/', CarCatalogueView.as_view(), name='catalogue'),
    path('<int:id>/', include([
        path('details/',CarDetailsView.as_view(), name='details'),
        path('edit/', CarEditView.as_view(), name='edit'),
        path('delete/', CarDeleteView.as_view(), name='delete')
    ]))

]