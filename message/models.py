from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager, PermissionsMixin
from django.db import models



class Message(models.Model):
    user_id = models.IntegerField(default=123)
    message = models.CharField(max_length=200)
    status = models.CharField(max_length=200, default="review")

# class User(AbstractBaseUser, PermissionsMixin):
#     username = models.CharField(db_index=True, max_length=255, unique=True)
#     email = models.EmailField(db_index=True, unique=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']
#     objects = UserManager()
#
#     def __str__(self):
#         """ Строковое представление модели (отображается в консоли) """
#         return self.email
#
#     @property
#     def token(self):
#         """
#         Позволяет получить токен пользователя путем вызова user.token, вместо
#         user._generate_jwt_token(). Декоратор @property выше делает это
#         возможным. token называется "динамическим свойством".
#         """
#         return self._generate_jwt_token()
#
#     def get_full_name(self):
#         """
#         Этот метод требуется Django для таких вещей, как обработка электронной
#         почты. Обычно это имя фамилия пользователя, но поскольку мы не
#         используем их, будем возвращать username.
#         """
#         return self.username
#
#     def get_short_name(self):
#         """ Аналогично методу get_full_name(). """
#         return self.username
#
#     def _generate_jwt_token(self):
#         """
#         Генерирует веб-токен JSON, в котором хранится идентификатор этого
#         пользователя, срок действия токена составляет 1 день от создания
#         """
#         dt = datetime.now() + datetime.timedelta(days=1)
#
#         token = jwt.encode({
#             'id': self.pk,
#             'exp': int(dt.strftime('%s'))
#         }, settings.SECRET_KEY, algorithm='HS256')
#
#         return token.decode('utf-8')

# Create your models here.
