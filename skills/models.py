from django.db import models

# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=50)
    xp = models.PositiveIntegerField(default=0)
    subskills = models.ManyToManyField("self", symmetrical=False, blank=True)
    is_sub = models.BooleanField(default = False)

    def is_subskill(self):
        return self.is_sub()
    
    def __str__(self) -> str:
        return self.name
