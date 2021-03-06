from django.urls import path
from . import views
from .views import (
    AllProjectListView,
    FirstPeriodProjectListView,
    SixthPeriodProjectListView,
    SeventhPeriodProjectListView,
    ProjectCreateView,
    ProjectDetailView,
    ProjectUpdateView,
    ProjectDeleteView,
    MyProjectsListView,
    AddPhotoView,
    AddVideoView,
    AddGalleryView
)

urlpatterns = [
    path('profile/',views.profile,name='users-profile'),
    path('newproject/',ProjectCreateView.as_view(),name='create-project'),
    path('projects/',AllProjectListView.as_view(),name='users-studentprojects'),
    #path('firstperiodprojects/',FirstPeriodProjectListView.as_view(),name='users-firstperiodprojects'),
    #path('sixthperiodprojects/',SixthPeriodProjectListView.as_view(),name='users-sixthperiodprojects'),
    #path('seventhperiodprojects/',SeventhPeriodProjectListView.as_view(),name='users-seventhperiodprojects'),
    path('myprojects/<int:user_id>/',MyProjectsListView.as_view(),name='users-myprojects'),
    path('projects/<int:pk>/',ProjectDetailView,name='project-details'),
    path('projects/<int:pk>/update/',ProjectUpdateView.as_view(),name='update-project'),
    path('projects/<int:pk>/delete/',ProjectDeleteView.as_view(),name='delete-project'),
    path('projects/<int:pk>/addphoto/',AddPhotoView,name='add-photo'),
    path('projects/<int:pk>/addvideo/',AddVideoView,name='add-video'),
    path('projects/<int:pk>/addgallery/',AddGalleryView,name='add-gallery'),
]