from django.db import models


class Breed(models.Model):
    breed_name      = models.CharField(max_length = 100 , null = True , blank = True)
    created_at      = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.breed_name

class Animal(models.Model):
    name            = models.CharField(max_length = 100 , null = True , blank = True)
    breed           = models.ManyToManyField(Breed , null = True , blank = True)


    def __str__(self):
        return self.name


class AnimalList(models.Model):
    name            = models.ForeignKey(Animal, on_delete=models.CASCADE , null = True , blank = True)
    breed           = models.ForeignKey(Breed, on_delete=models.CASCADE , null = True , blank = True)
    date            = models.DateField(null=True, blank=True)
