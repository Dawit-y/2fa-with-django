from django.db.models.signals import post_save
from users.models import CustomUser
from .models import Code
from django.dispatch import receiver

@receiver(post_save, sender=CustomUser)
def post_save_generate_code(sender, instance, created, *args, **kwargs):
        try:
                instance.code.delete()
                Code.objects.create_code(instance)
        except:
                Code.objects.create_code(instance)