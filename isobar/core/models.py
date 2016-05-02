from django.db import models

class Article(models.Model):
	title = models.CharField(max_length=100)
	post_date = models.DateTimeField(auto_now=True)
	body = models.TextField()
	featured_image = models.FileField()

	def __unicode__(self):
		return self.title