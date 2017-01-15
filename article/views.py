from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post
from .forms import PostForm

def index(request):
	queryset = Post.objects.all()
	context = {
	     "object_list":queryset,
	     "title":"search"
	}

	return render(request, "index.html",context)

def form(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		print (form.cleaned_data.get("title"))
		print (form.cleaned_data.get("content"))
		instance.save()

#		messages.success(request, "Successfully Created")
		#return HttpResponseRedirect(instance.get_absolute_url())
#	else:
#		messages.error(request, "Failed")
		

	context = {
	     "form":form,
	}

	return render(request, "post_form.html",context)


	#return HttpResponse("<h2>Welcome</h2>")
 