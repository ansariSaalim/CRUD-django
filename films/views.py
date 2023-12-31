from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Film
from django.shortcuts import redirect

class FilmBaseView(View):
    model = Film
    fields = '__all__'
    success_url = reverse_lazy('films:all')

class FilmListView(FilmBaseView, ListView):
    """View to list all films.
    Use the 'film_list' variable in the template
    to access all Film objects"""

class FilmDetailView(FilmBaseView, DetailView):
    """View to list the details from one film.
    Use the 'film' variable in the template to access
    the specific film here and in the Views below"""

class FilmCreateView(FilmBaseView, CreateView):
    """View to create a new film"""

class FilmUpdateView(FilmBaseView, UpdateView):
    """View to update a film"""

class FilmDeleteView(FilmBaseView, DeleteView):
    """View to delete a film"""

class FilmDeleteAllView(View):
    def get(self, request, *args, **kwargs):
        # Delete all data logic (replace this with your actual logic)
        Film.objects.all().delete()
        return redirect('films:all')  # Redirect to the list view after deletion
