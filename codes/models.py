from django.db import models
from users.models import CustomUser
import random
# Create your models here.

class CodeManager(models.Manager):
    def create_code(self, instance):
        code_items = []
        for i in range(5):
            num = random.randint(1,9)
            code_items.append(num)
        print(code_items)
        code_string = "".join(str(item) for item in code_items)
        print(code_string)
        code = self.create(number=code_string, user = instance)
        return code


class Code(models.Model):
    number = models.CharField(max_length=5, blank=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    objects = CodeManager()

    def __str__(self) -> str:
        return str(self.number)
    
    # def save(self):
    #     code_items = []
    #     for i in range(5):
    #         num = random.randint(1,10)
    #         code_items.append(num)
    #     code_string = "".join(str(item) for item in code_items)
    #     self.number = code_string
    #     return super().save()

    # def save(self, force_insert: False,  using: str | None = ..., update_fields: ["number"] = ...) :
    #     code_items = []
    #     for i in range(5):
    #         num = random.randint(1,10)
    #         code_items.append(num)
    #     code_string = "".join(str(item) for item in code_items)
    #     self.number = code_string
    #     return super().save( using, update_fields)
    