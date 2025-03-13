from django.shortcuts import render
from django.views import generic
from .models import PlaylistPost

def home(request):
    posts = PlaylistPost.objects.all()  # Fetch all posts
    return render(request, 'home.html', {'posts': posts})


# Create your views here.
class PlaylistListView(generic.ListView):
    model = PlaylistPost
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = ['-created_at']  # Sort posts by date
    paginate_by = 5  # Paginate posts by 5 per page