from django.forms import ModelForm
from app1.models import Rating


class RatingForm(ModelForm):
    class Meta:
        model = Rating
        fields = ('ratings', )#'movie', 'ratings', 'timestamp', 'new_stamp')