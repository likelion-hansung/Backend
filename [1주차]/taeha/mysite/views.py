from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'

class hiView(TemplateView):
    template_name = 'hi.html'