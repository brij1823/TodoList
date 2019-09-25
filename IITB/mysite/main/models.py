from django.db import models
from datetime import datetime

class Tutorials(models.Model):
	tutorial_title = models.CharField(max_length = 200)
	tutorial_content = models.TextField()
	tutorial_publised = models.DateTimeField("date published" , default = datetime.now()) 


	def __str__(self):
		return self.tutorial_title 


class List(models.Model):
	item = models.CharField(max_length = 200)
	priority = models.CharField(default = 'Incomplete' , max_length = 200)
	completed = models.BooleanField(default = False)



	def __str__(self):
		return self.item + ' '+str(self.priority)+' '+str(self.completed) 