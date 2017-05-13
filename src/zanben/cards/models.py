from django.db import models
from django.forms import ModelForm

class Input(models.Model):
    deckSize = models.IntegerField()
    numCardsInCategory = models.IntegerField()
    numAtLeast = models.IntegerField()
    numDraws = models.IntegerField()

class InputForm(ModelForm):
    class Meta:
        model = Input
        fields = '__all__'
