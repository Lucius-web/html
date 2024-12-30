from django.db import models
 
  

# Create your models here.
class Banner(models.Model):
  title = models.CharField(
       max_length=255,
       verbose_name="Заголовок"
  )
  description =models.TextField(
    verbose_name="Описание"
  )
  image = models.ImageField(
    upload_to='image/',
    verbose_name="фото"
  )
  


  def __str__(self):
    return self.title
  
  class Meta:
    verbose_name = "баннер"
    verbose_name_plural = "баннера"

