from django.db import models
import uuid

# Create your models here.
class Tag(models.Model):
	name = models.CharField(max_length = 100)
	def __str__(self):
		return self.name
	
class AbstractIdea(models.Model):
	class Meta:
		abstract = True
		
	uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length = 100)
	tags = models.ManyToManyField(Tag, blank = True)
	approved = models.BooleanField(default = False)
	
class Definition(AbstractIdea):
	definition = models.TextField()
	image_link = models.URLField(blank = True)
	example_link = models.URLField(blank = True)
	def __str__(self):
		return self.name

	