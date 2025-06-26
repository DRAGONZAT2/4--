from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название фильма', help_text='Тут надо писать название фильма (макс. 100 сим.)')

    description = models.TextField(verbose_name='Описание')

    image = models.ImageField(verbose_name='Изображение', upload_to='movies/')

    year = models.IntegerField(verbose_name='Год выпуска') 

    rating = models.FloatField(verbose_name='Pейтинг от 0 до 10') 

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'