from django.urls import path

from . import views

app_name = "pages"

urlpatterns = [

    path("", views.HomeView.as_view(), name="home"),
    path("faqs/", views.FaqsView.as_view(), name="faqs"),
    path("objective/", views.ObjectiveView.as_view(), name="objective"),
    path("privacy-policy/", views.PrivacyView.as_view(), name="privacy-policy"),  # noqa
    path("dashboard/", views.DashboardView.as_view(), name="dashboard")
]
