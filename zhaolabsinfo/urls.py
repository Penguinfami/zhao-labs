from django.urls import path, include

from . import views

app_name = "zhaolabsinfo"

urlpatterns = [
    path("", views.HomeView.as_view(), name="index"),
    path("bio", views.BioView.as_view(), name="bio"),
    path("teaching", views.TeachingView.as_view(), name="teaching"),
    path("opportunities", views.OpportunitiesView.as_view(), name="opportunities"),
    path("publications", views.PublicationView.as_view(), name="publications"),
    path("members", views.MemberView.as_view(), name="members"),
    path("contact", views.ContactView.as_view(), name="contact"),
    path("useful-links", views.UsefulLinksView.as_view(), name="useful links"),


]