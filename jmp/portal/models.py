from django.db import models

# Create your models here.

class Proxy(models.Model):
    proxy_name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.proxy_name

class PConfig(models.Model):
    proxy = models.ForeignKey(Proxy)
    pconfig_name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.pconfig_name

class ContentSwitch(models.Model):
    pconfig = models.ForeignKey(PConfig)
    content_switch_name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.content_switch_name

class Target(models.Model):
    content_switch = models.ForeignKey(ContentSwitch)
    target_name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.target_name

class Endpoint(models.Model):
    target = models.ForeignKey(Target)
    endpoint_name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.endpoint_name
