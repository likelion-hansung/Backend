from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'

class servicesView(TemplateView):
    template_name = 'services.html'

class portfolioView(TemplateView):
    template_name = 'portfolio.html'

class aboutView(TemplateView):
    template_name = 'about.html'
    
class teamView(TemplateView):
    template_name = 'team.html'

class contactView(TemplateView):
    template_name = 'contact.html'