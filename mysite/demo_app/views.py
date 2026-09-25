from django.views.generic import TemplateView


class Hello(TemplateView):
    templage_name = "home.html"
