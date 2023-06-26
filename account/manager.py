from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    use_in_migrations = True
    def create_user(self,email,password=None, **extrafields):
        user = self.model(email=email,**extrafields)
        user.set_password(password)
        user.save(using=self.db)
        return user
    def create_superuser(self,email,password=None, **extrafields):
        extrafields.setdefault('is_staff',True)
        extrafields.setdefault('is_superuser',True)
        extrafields.setdefault('is_active',True)
        return self.create_user(email,password,**extrafields)