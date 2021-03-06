from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# from django.core.validators import MinLengthValidator
# Create your models here.

class CustomeUserManager(BaseUserManager):
	def _create_user(self, email, password):

		if not email:
			raise ValueError('Email must be set')

		email = self.normalize_email(email)
		user = self.model(email=email)
		# user.password(hashed)
		user.save(using=self.db)
		return user

	def create_user(self, email, password=None):
		return self._create_user(email, password)

	def create_superuser(self, email, password):
		return self._create_user(email, password)

class CustomUser(AbstractBaseUser):
	username = models.CharField(max_length=100, blank=True, null=True)
	full_name = models.CharField(max_length=100, blank=True, null=True)
	first_name = models.CharField(max_length=100, blank=True, null=True)
	last_name = models.CharField(max_length=100, blank=True, null=True)
	email = models.CharField(unique=True, max_length=100, blank=True, null=True)
	birthday = models.DateField(blank=True, null=True)
	sex = models.CharField(max_length=1, blank=True, null=True)
	password = models.TextField(blank=True, null=True)
	mobile_number = models.CharField(max_length=20, blank=True, null=True)
	api_token = models.TextField(blank=True, null=True)
	status = models.CharField(max_length=1, blank=True, null=True)
	create_user = models.IntegerField(blank=True, null=True)
	update_user = models.IntegerField(blank=True, null=True)
	created_at = models.DateTimeField(blank=True, null=True, auto_now=True)
	updated_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
	deleted_at = models.DateTimeField(blank=True, null=True)
	address = models.CharField(max_length=100, blank=True, null=True)
	code_pos = models.CharField(max_length=100, blank=True, null=True)
	city = models.CharField(max_length=100, blank=True, null=True)
	state = models.CharField(max_length=100, blank=True, null=True)
	country = models.CharField(max_length=100, blank=True, null=True)
	no_identification = models.CharField(max_length=100, blank=True, null=True)
	dashboard_id = models.CharField(max_length=50, blank=True, null=True)
	last_login = models.DateTimeField(blank=True, null=True)
	is_active = models.CharField(max_length=5, default='false', blank=False, null=True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['email']

	objects = CustomeUserManager()

	class Meta:
		db_table = 'user'
		app_label = "modulcuaca"

	def __str__(self):
		return self.email

	def get_full_name(self):
		return self.email

	def get_short_name(self):
		return self.email

class TabelSuhu(models.Model):
	time = models.DateTimeField(auto_now_add=True)
	api_key = models.CharField(max_length=8)
	nilai_suhu = models.CharField(max_length=10, blank=True, null=True)
	
	class Meta:
		db_table = 'tabel_suhu'
		verbose_name_plural = 'tabel_suhu'

class TabelKelembaban(models.Model):
	time = models.DateTimeField(auto_now_add=True)
	api_key = models.CharField(max_length=8)
	nilai_kelembaban = models.CharField(max_length=10, blank=True, null=True)
	
	class Meta:
		db_table = 'tabel_kelembaban'
		verbose_name_plural = 'tabel_kelembaban'

class TabelTekananUdara(models.Model):
	time = models.DateTimeField(auto_now_add=True)
	api_key = models.CharField(max_length=8)
	nilai_tekananudara = models.CharField(max_length=10, blank=True, null=True)
	
	class Meta:
		db_table = 'tabel_tekananudara'
		verbose_name_plural = 'tabel_tekananudara'