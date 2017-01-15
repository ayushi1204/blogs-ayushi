#from _future_ import unicode_literals

from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=250)
	content = models.TextField()
	#updated = models.DateTimeFeild(auto_now=True, auto_now_add=False)
	#timestamp = models.DateTimeFeild(auto_now=False, auto_now_add=True)

	def _unicode_(self):
		return self.title

	def _str_(self):
		return self.title