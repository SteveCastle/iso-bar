from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    street_address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __unicode__(self):
        return "%s %s"%(self.first_name, self.last_name)

    def get_formatted_address(self):
        return "%s %s\n%s\n%s, %s %s"%(self.first_name,
                                      self.last_name,
                                      self.street_address,
                                      self.city,
                                      self.state,
                                      self.zipcode)
