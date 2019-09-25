from django.contrib import admin
from .models import Tutorials,List
from tinymce.widgets import TinyMCE
from django.db import models


class TutorialAdmin(admin.ModelAdmin):
	#To separate them contentwise
	fieldsets = [
		("Title/data" , {"fields" : ["tutorial_title" , "tutorial_published"]}),
		("Content" , {"fields" : ["tutorial_content"]})
	]

	formfield_overrides = {
		models.TextField: {"widget" : TinyMCE()}
	}




admin.site.register(Tutorials)
admin.site.register(List)
