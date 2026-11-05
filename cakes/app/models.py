from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Shape(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Shape'
        verbose_name_plural = 'Shapes'


class Weight(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Weight'
        verbose_name_plural = 'Weights'


class Cake(models.Model):

    name = models.CharField(max_length=50)

    description = models.TextField()

    photo = models.ImageField(upload_to='cake-images')

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT
    )

    shape = models.ForeignKey(
        Shape,
        on_delete=models.PROTECT
    )

    weight = models.ForeignKey(
        Weight,
        on_delete=models.PROTECT
    )

    price = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Cake'
        verbose_name_plural = 'Cakes'