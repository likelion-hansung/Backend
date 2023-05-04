from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name='home.html'
    
class AboutView(TemplateView):
    template_name='about.html'
    
class ContactView(TemplateView):
    template_name='contact.html'
    
class ServicesView(TemplateView):
    template_name='services.html'
    
class TeamView(TemplateView):
    template_name='team.html'
    