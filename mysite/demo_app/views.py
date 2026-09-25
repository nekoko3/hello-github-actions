from django.views.generic import TemplateView


class Hello(TemplateView):
    TemplateView = "home.html"
