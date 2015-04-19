from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from MovieLib.models import Movie

# Create your views here.
class IndexView(ListView):
    template_name = 'index.html'
    model = Movie

class CreateView(CreateView):
    template_name = 'create.html'
    model = Movie
    success_url = '/'
    
class UpdateView(UpdateView):
    template_name = 'update.html'
    model = Movie
    success_url = '/'
    
class MovieMixin(object):
    model = Movie
    def get_context_data(self, **kwargs):
        kwargs.update({'object_name':'Movie'})
        return kwargs
    
class DeleteView(MovieMixin, DeleteView):
    template_name = 'delete_confirm.html'
    def get_success_url(self):
        return reverse('index.html')
    
   