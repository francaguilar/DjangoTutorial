from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pokemon(models.Model):
	id = models.IntegerField(primary_key=True)
	image = models.URLField(default="")
	name = models.CharField(max_length=50)
	attack = models.IntegerField()
	defense = models.IntegerField()
	hp = models.IntegerField()
	tipo = models.CharField(max_length=50)

class Purchase(models.Model):
	user = models.ForeignKey(User)
	pokemons = models.ManyToManyField(Pokemon)
	checkout = models.BooleanField(default=False)

