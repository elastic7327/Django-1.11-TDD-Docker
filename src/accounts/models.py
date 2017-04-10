from django.db import models
from django.contrib.auth.models import (
        AbstractBaseUser, BaseUserManager, PermissionsMixin 
)



class Token(models.Model):
    """
    doc
    """
    email = models.EmailField(max_length=75, blank=True)
    uid = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Token"
        verbose_name_plural = "Tokens"

    def __str__(self):
        return super(Token, self).__str__()



class ListUserManager(BaseUserManager):
    
    def create_user(self, email):
        """TODO: Docstring for create_user.

        :email: TODO
        :returns: TODO

        """
        ListUser.objects.create(email=email)

    def create_superuser(self, email, password):
        """TODO: Docstring for create_superuser.

        :email: TODO
        :password: TODO
        :returns: TODO

        """
        self.create_user(email)

class ListUser(AbstractBaseUser, PermissionsMixin):
    """
    doc
    """
    email = models.EmailField(primary_key=True)
    USERNAME_FIELD = 'email'
    objects = ListUserManager()

    @property
    def is_staff(self):
        """TODO: Docstring for is_staff.
        :returns: TODO

        """
        return self.email == 'elastic7327@gmail.com'

    @property
    def is_active(self):
        """TODO: Docstring for is_active.

        :f: TODO
        :returns: TODO

        """
        return True

    class Meta:
        verbose_name = "ListUser"
        verbose_name_plural = "ListUsers"

    def __str__(self):
        return super(ListUser, self).__str__()

