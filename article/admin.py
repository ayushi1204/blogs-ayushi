from django.contrib import admin

# Register your models here.
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
	list_display=["title","content"]
	class Meta:
		model=Post
	#list_display=["content"]
	#class Meta:
	#	model=Post

admin.site.register(Post,PostModelAdmin)
