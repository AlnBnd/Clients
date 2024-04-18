from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class UserManager(models.Manager):
    use_in_migrations = True

    def create_user(self, username, full_name, password=None):
        user = self.create(username=username, full_name=full_name)
        if password:
            user.set_password(password)
            user.save()
        return user
    
    def get_by_natural_key(self, username):
        return self.get(**{f"{self.model.USERNAME_FIELD}__iexact": username})
    
class User(AbstractBaseUser):
    username = models.CharField(unique=True, null=True, max_length=255)
    full_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    USERNAME_FIELD = 'username'
    objects = UserManager()

class Client(models.Model):
    STATUS_CHOICES = [
        ('Не в работе', 'Не в работе'),
        ('В работе', 'В работе'),
        ('Отказ', 'Отказ'),
        ('Сделка закрыта', 'Сделка закрыта'),
    ]
    account_number = models.CharField(max_length=100, unique=True)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    inn = models.CharField(max_length=20, unique=True)
    responsible_person = models.ForeignKey(User, related_name='clients', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='Не в работе')
