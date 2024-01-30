from django.db import models
# Date Time
from django.utils import timezone
# Token UUID
import uuid

class Token(models.Model):
  token_id = models.AutoField(primary_key=True)
  token_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
  token_owner = models.UUIDField(default=uuid.uuid4,editable=False)
  token_date = models.DateTimeField(default=timezone.now())
  token_expires = models.DateTimeField()

class User(models.Model):
  user_id = models.AutoField(primary_key=True)
  user_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
  user_type = models.CharField(max_length=255)
  user_data = models.JSONField(default=dict)
  user_date = models.DateTimeField(default=timezone.now())

class Event(models.Model):
  event_id = models.AutoField(primary_key=True)
  event_owner = models.JSONField(default=dict)
  event_member = models.JSONField(default=dict)
  event_name = models.CharField(max_length=255)
  event_date = models.DateTimeField()
  event_place = models.JSONField(default=dict)
  category_uuid = models.UUIDField(default=uuid.uuid4,editable=False)

class Category(models.Model):
  category_id = models.AutoField(primary_key=True)
  category_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
  category_name = models.CharField(max_length=255)
  category_owner = models.JSONField()
  category_date = models.DateTimeField(default=timezone.now())