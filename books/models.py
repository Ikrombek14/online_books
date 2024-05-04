from django.db import models

# Create your models here.
class Authors(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'authors'

    def __str__(self):
        return self.name
class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)
    price = models.IntegerField()
    body=models.TextField()
    class Meta:
        db_table = 'books'
    
    def __str__(self):
        return self.title

