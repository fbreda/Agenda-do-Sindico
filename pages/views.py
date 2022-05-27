from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "pages/index.html"


class ObjectiveView(TemplateView):
    template_name = "pages/objective.html"


class PrivacyView(TemplateView):
    template_name = "pages/privacy-policy.html"


class FaqsView(TemplateView):
    template_name = "pages/faqs.html"


class DashboardView(TemplateView):
    template_name = "pages/dashboard.html"
