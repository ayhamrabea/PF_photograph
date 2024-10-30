from audioop import reverse
from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
# Create your models here.







class Comments(models.Model):
    user = models.ForeignKey( User ,on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.TimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")
        ordering = ['created_at']

    def __str__(self):
        return self.user.username
    
    # def get_absolute_url(self):
    #     return reverse("model_detail", kwargs={"pk": self.pk})
    
    
    


class Messsages(models.Model):
    user = models.ForeignKey( User ,on_delete=models.CASCADE)
    phone_numper = models.CharField( max_length=50)
    email = models.EmailField( max_length=254)
    text = models.TextField()
    created_at = models.TimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Messsage")
        verbose_name_plural = _("Messsages")

    def __str__(self):
        return self.user.username
    