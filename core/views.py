from django.shortcuts import render
from django.http import HttpResponse

from . models import (
	BackgroundIntro,
	NextService,
	FilmProduction,
	Projects,
	RadioAdverts,
	OurClients,
	Testimonials,
	Team,
)




def home_view(request):
	intro = BackgroundIntro.objects.all()
	services = NextService.objects.all()
	production = FilmProduction.objects.all()
	projects = Projects.objects.all()
	adverts = RadioAdverts.objects.all()
	clients = OurClients.objects.all()
	testimonial = Testimonials.objects.all()
	teams = Team.objects.all()
	context = {
			"intro":intro,
			"services":services,
			"production":production,
			"projects":projects,
			"adverts":adverts,
			"clients":clients,
			"tests":testimonial,
			"teams":teams,
	}
	return render(request, "core/home.html", context)


