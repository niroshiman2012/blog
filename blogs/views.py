from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .models import BlogPost
from .forms import PostForm

# Create your views here.
def index(request):
	"""Home page for blogs app, showing all blog posts."""
	posts = BlogPost.objects.order_by('date_added')
	if request.user.is_authenticated():
		can_add_post = True
	else:
		can_add_post = False
	context = {'posts': posts, 'can_add_post': can_add_post}

	return render(request, 'blogs/index.html', context)

def post(request, post_id):
	"""Detail page for post."""
	post = BlogPost.objects.get(id=post_id)
	context = {'post': post,'user': request.user}
	return render(request, 'blogs/post.html', context)

@login_required
def new_post(request):
	"""Add a new post."""
	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = PostForm()
	else:
		# POST data submitted; process data
		form = PostForm(request.POST)
		if form.is_valid():
			new_post = form.save(commit=False)
			new_post.owner = request.user
			new_post.save()
			return HttpResponseRedirect(reverse('blogs:index'))

	context = {'form': form}
	return render(request,'blogs/new_post.html',context)

@login_required
def edit_post(request, post_id):
	"""Page to edit post."""
	post = BlogPost.objects.get(id=post_id)
	if post.owner != request.user:
		raise Http404

	if request.method != 'POST':
		# Initial request; pre-fill form with the current entry.
		form = PostForm(instance=post)
	else:
		# POST data submitted; process data.
		form = PostForm(instance=post,data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('blogs:post', args=[post_id]))	

	context = {'post': post, 'form': form}
	return render(request, 'blogs/edit_post.html', context)
