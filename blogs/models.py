from django.db import models

# Create your models here.
class BlogPost(models.Model):
	""""""
	title = models.CharField(max_length=200)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'Blog Posts'

	def __str__(self):
		"""Return string representation of the model."""
		return self.title