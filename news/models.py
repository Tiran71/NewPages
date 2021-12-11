from django.db import models
#from django.urls import reverse
from django.db.models.fields import CharField, DateField, TextField

class Blog(models.Model):
    title=CharField('Заголовок', max_length=20)
    text = TextField('Статья', max_length=255)
    date = DateField('Дата публикации')

    def __str__(self):
        return (self.title)

    class Meta:
        verbose_name='Блог'
        verbose_name_plural='Мои блоги'    

   # def get_absolute_url(self): # Тут мы создали новый метод
        #return reverse('detail', args=[str(self.id)])
    #    return reverse('list')