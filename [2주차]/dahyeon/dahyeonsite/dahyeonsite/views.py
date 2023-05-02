from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name ='home.html'
    
class AboutView(TemplateView):
    template_name ='about.html'
    
class ContactView(TemplateView):
    template_name ='contact.html'
    
class PortfolioView(TemplateView):
    template_name ='portfolio.html'
    
class ServicesView(TemplateView):
    template_name ='services.html'