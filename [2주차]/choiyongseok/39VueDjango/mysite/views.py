from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name ='home.html'

class TeamView(TemplateView):
    template_name ='team.html'

class AboutView(TemplateView):
    template_name ='about.html'

class PortfolioView(TemplateView):
    template_name ='portfolio.html'

class ServicesView(TemplateView):
    template_name ='services.html'

class TeamView(TemplateView):
    template_name ='team.html'

