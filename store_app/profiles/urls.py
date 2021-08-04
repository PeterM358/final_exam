from django.urls import path

from store_app.profiles.views import ProfileDetailsView

urlpatterns = (
    path('profile_details', ProfileDetailsView.as_view(), name='profile details'),

)