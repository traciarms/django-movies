import datetime
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse, reverse_lazy
from django.db.models import Avg, Count
from django.forms import Form
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render


# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, DeleteView, \
    UpdateView
from app1.forms import RatingForm
from app1.models import Movie, Rater, Rating, Category


class MovieList(ListView):
    model = Movie
    template_name = "app1/list_movies.html"
    queryset = Movie.objects.all().order_by('title')
    paginate_by = 20


class MostRatings(ListView):
    model = Movie
    template_name = "app1/most_ratings.html"
    queryset = Movie.objects.exclude(rating=None).annotate(
        count=Count('rating__ratings')).order_by('-count')[:20]
    paginate_by = 10


class AccountProfile(ListView):
    model = Rating
    template_name = "app1/account_profile.html"
    paginate_by = 10

    def get_queryset(self):
        queryset = Rater.objects.get(
            pk=self.request.user.rater.id).get_rating_list()
        return queryset


class DetailRater(DetailView):
    model = Rater
    pk_url_kwarg = 'rater_id'
    template_name = 'app1/detail_rater.html'


class DetailMovie(DetailView):
    model = Movie
    pk_url_kwarg = 'movie_id'
    template_name = 'app1/detail_movie.html'

    def get_context_data(self, **kwargs):
        movie = self.object
        context = super(DetailMovie, self).get_context_data(**kwargs)
        context['rated'] = self.request.user.rater.has_rated_movie(movie.id)
        return context


class AvgRating(ListView):
    model = Movie
    template_name = "app1/avg_rating.html"
    paginate_by = 7

    def get_queryset(self):
        select_cat = self.request.GET.get("select_category", None)
        queryset = Movie.objects.exclude(rating=None)
        if select_cat != 'None':
            queryset = queryset.filter(
                category__category__icontains=select_cat)
        queryset = queryset.annotate(
            average=Avg('rating__ratings')).order_by('-average')[:20]

        return queryset

    def get_context_data(self, **kwargs):
        context = super(AvgRating, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['select_category'] = \
            self.request.GET.get("select_category", None)
        return context


@login_required(login_url='/login')
def change_rating(request, rating_id):

    if request.method == 'POST':
        form = RatingForm(request.POST)

        if form.is_valid():
            rating = Rating.objects.get(pk=rating_id)
            form_rating = form.save(commit=False)
            rating.movie_id = rating.movie.id
            rating.rater_id = request.user.rater.id
            rating.new_stamp = datetime.datetime.now()
            rating.ratings = form_rating.ratings
            rating.save()

            return HttpResponseRedirect(reverse('account_profile'))

    else:
        form = RatingForm()
    return render(request, 'app1/update_rating.html', {'form': form,
                                                       'rating_id': rating_id})


class UpdateRating(UpdateView):
    model = Rating
    fields = ['ratings']
    pk_url_kwarg = 'rating_id'
    template_name = "app1/update_rating.html"

    def get_success_url(self):
        return reverse('account_profile')


class DeleteRating(DeleteView):
    model = Rating
    pk_url_kwarg = 'rating_id'
    template_name = "app1/delete_rating.html"

    def get_success_url(self):
        return reverse('account_profile')


class CreateRating(CreateView):
    model = Rating
    fields = ('ratings',)
    success_url = reverse_lazy('detail_movie')
    template_name = "app1/create_rating.html"

    def get_success_url(self):
        return reverse('detail_movie',
                       kwargs={'movie_id': self.kwargs.get('movie_id', None)})

    def get_context_data(self, **kwargs):
        context = super(CreateRating, self).get_context_data(**kwargs)
        context['movie_id'] = self.kwargs.get('movie_id', None)
        return context

    def form_valid(self, form):
        form.instance.rater_id = self.request.user.rater.id
        form.instance.movie_id = self.kwargs.get('movie_id', None)
        form.instance.rating = form.cleaned_data.get('rating', None)
        form.instance.new_stamp = datetime.datetime.now()
        return super(CreateRating, self).form_valid(form)

