from django.urls import path, include

from petstagram.pets import views
from petstagram.pets.views import AddPetView, PetDetailsView, PetDeleteView, PetEditView

urlpatterns = [
    path('add/', AddPetView.as_view(), name='add-pet'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', PetDetailsView.as_view(), name='pet-details'),
        path('edit/', PetEditView.as_view(), name='pet-edit'),
        path('delete/', PetDeleteView.as_view(), name='pet-delete')
    ]))
]