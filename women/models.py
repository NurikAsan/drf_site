from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return self.name
    
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Women(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=100, blank=True)
    time_creat = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    draft = models.BooleanField('Черновик', default=True)
    category = models.ForeignKey(to=Category, on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def __str__(self) -> str:
        return self.title
    

    class Meta:
        verbose_name = 'Женщина'
        verbose_name_plural = 'Женщины'