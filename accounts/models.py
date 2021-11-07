from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db.models.signals import post_save
from jobs.models import Job
# Create your models here.


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password):
        if not email:
            raise ValueError('Adresse email obligatoire')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email=email,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    fist_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_employer = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="profile")
    image = models.ImageField(upload_to="photos", default="user.jpg", blank=True, null=True)
    birth_day = models.DateField(default=None, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True)
    resume = models.TextField(blank=True)
    company = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.user.email


def post_save_receiver(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


post_save.connect(post_save_receiver, sender=CustomUser)


class Invite(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="invites")
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="invites", default=1)
    description = models.TextField(blank=True)
    created = models.DateField(default=None, blank=True, null=True)
    unread = models.BooleanField(default=True)

    def __str__(self):
        return self.user.email