from django.db import models

class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=600)

    def __str__(self):
        return self.question[:10]
    
    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'


class ContactUs(models.Model):    
    TOPIC_CHOICES = (     # add
        (),
        (),
        (),
        (),
        (),
        ()
    )

    name = models.CharField(max_length=30)
    topic = models.CharField(max_length=..., choices=TOPIC_CHOICES)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    question = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.question[:10]
    
    class Meta:
        verbose_name = 'Contact Us request'
        verbose_name_plural = 'Contact Us requests'