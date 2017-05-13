from django.db import models
from django.forms import ModelForm

class Input(models.Model):
    deckSize = models.IntegerField(max_length=10, blank=True)
    numCardsInCategory = models.IntegerField()
    numAtLeast = models.IntegerField()
    numDraws = models.IntegerField()

class InputForm(ModelForm):
    class Meta:
        model = Input
        fields = '__all__'
