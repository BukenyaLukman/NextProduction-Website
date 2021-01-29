from django.contrib import admin

from . models import (
	NextService, 
	FilmProduction, 
	Projects, 
	RadioAdverts,
	OurClients,
	Testimonials,
	Team,
	Contact,
	BackgroundIntro,
)

class BackgroundIntroAdmin(admin.ModelAdmin):
	list_display = ('header','description',)
	list_filter = ('header',)
	search_fields = ('header',)

class NextServiceAdmin(admin.ModelAdmin):
	list_display = ('service_name','description',)
	list_filter = ('service_name',)
	search_fields = ('service_name',)

class FilmProductionAdmin(admin.ModelAdmin):
	list_display = ('service_name',)
	list_filter = ('service_name',)
	search_fields = ('service_name',)
		
class ProjectsAdmin(admin.ModelAdmin):
	list_display = ('clients','projects','hours_of_support','hard_work',)

class RadioAdvertsAdmin(admin.ModelAdmin):
	list_display = ('title','description',)
	list_filter = ('title','description',)

class OurClientsAdmin(admin.ModelAdmin):
	list_filter = ('name',)
	list_display = ('name',)

class TestimonialAdmin(admin.ModelAdmin):
	list_display = ('client_name','client_profession','comment',)
	list_filter = ('client_name','client_profession',)


class TeamAdmin(admin.ModelAdmin):
	list_display = ('name','position','twitter','facebook','gmail','linked',)
	list_filter = ('name','position',)


class ContactAdmin(admin.ModelAdmin):
	list_display = ('sender','subject','email','message',)
	list_filter = ('sender','subject',)



admin.site.site_header = 'Next Production'
admin.site.site_title = 'Next Production'
admin.site.register(NextService,NextServiceAdmin)
admin.site.register(FilmProduction, FilmProductionAdmin)
admin.site.register(Projects, ProjectsAdmin)
admin.site.register(RadioAdverts,RadioAdvertsAdmin)
admin.site.register(OurClients, OurClientsAdmin)
admin.site.register(Testimonials, TestimonialAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(BackgroundIntro, BackgroundIntroAdmin)
