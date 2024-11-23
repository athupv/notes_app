from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.NoteList.as_view(), name='note-list'),
    path('<int:pk>/',views.NoteDetail.as_view(),name='note-detail'),
    path('create/',views.NoteCreate.as_view(),name='note-create'),
    path('<int:pk>/delete/',views.NoteDelete.as_view(),name='note-delete'),
    path('<int:pk>/edit/',views.NoteUpdate.as_view(),name='note-update'),
]