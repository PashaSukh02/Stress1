from django.db import models



# Create your models here.
class Test(models.Model):
    title = models.CharField('Название вопроса', max_length=50)
    anons = models.CharField('Вопрос', max_length=250)
    ans1 = models.TextField('Вариант ответа 1')
    pr1 = models.IntegerField('Цена ответа в баллах',default=1)
    ans2 = models.TextField('Вариант ответа 2')
    pr2 = models.IntegerField('Цена ответа в баллах',default=2)
    ans3 = models.TextField('Вариант ответа 3')
    pr3 = models.IntegerField('Цена ответа в баллах',default=3)

    def __str__(self):
        return self.anons

    def get_absolute_url(self):
        return f'/test/{self.id}'

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
