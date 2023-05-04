from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'

class HelloView(TemplateView):
    template_name = 'hello.html'

class Baseview(TemplateView):
    template_name = 'base.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class ServicesView(TemplateView):
    template_name = 'services.html'

class PortfolioView(TemplateView):
    template_name = 'portfolio.html'

class ContactView(TemplateView):
    template_name = 'contact.html'
