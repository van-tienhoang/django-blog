from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path='/img')


class Person(models.Model):
    title = models.CharField(max_length=100)
    first_name = models.TextField(max_length=100)
    address = models.TextField(max_length=1000)
    photo = models.ImageField()


class heo(object):
    """this is the heo class, it stores information about heo

    Arguments:
        object {[type]} -- [description]
    """
    import seaborn as sns
    iris = sns.load_dataset('iris')
    sns.pairplot(iris, hue='spieces')
