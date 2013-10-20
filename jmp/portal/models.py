from django.db import models

# Create your models here.

class Proxy(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class PConfig(models.Model):
    proxy = models.ForeignKey(Proxy)
    name = models.CharField(max_length=200)
    fqdn = models.CharField(max_length=200)
    ssl_key = models.CharField(max_length=2000)
    port = models.IntegerField()
    ssl_port = models.IntegerField()
    active = models.BooleanField(default=True)
    def __unicode__(self):
        return self.name

class ContentSwitch(models.Model):
    pconfig = models.ForeignKey(PConfig)
    name = models.CharField(max_length=200)
    regex = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    def __unicode__(self):
        return self.name

class Target(models.Model):
    content_switch = models.ForeignKey(ContentSwitch)
    name = models.CharField(max_length=200)
    ROUND_ROBIN = 'rr'
    LEAST_CONNECTION = 'lc'
    LOAD_BALANCING_ALG = (
        (ROUND_ROBIN, 'Round Robin'),
        (LEAST_CONNECTION, 'Least Connection'),
    )
    lb_alg = models.CharField(max_length=2, choices=LOAD_BALANCING_ALG, default=ROUND_ROBIN)

    def __unicode__(self):
        return self.name

class Endpoint(models.Model):
    target = models.ForeignKey(Target)
    name = models.CharField(max_length=200)
    ip = models.IPAddressField()
    port = models.IntegerField()
    PROTOCOLS = (
        ('http', 'HTTP'),
        ('https', 'HTTPS'),
    )
    protocol = models.CharField(max_length=200, choices=PROTOCOLS, default='HTTP')
    active = models.BooleanField(default=True)
    def __unicode__(self):
        return self.name
