from django.db import models

class Blog(models.Model):
	titles = models.CharField(max_length=255)
	pub_date = models.DateTimeField()
	body = models.TextField()
	image = models.ImageField(upload_to='images/')

	def __str__(self):
		return self.titles

	def date(self):
		return self.pub_date.strftime("%b %e %Y")