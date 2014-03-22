from django.db import models
class Game(models.Model):
    appid = models.IntegerField(default=0)
    name = models.CharField(max_length = 50)
    playtime_forever = models.IntegerField(default=0)
    img_icon_url = models.CharField(max_length=100)
    img_logo_url = models.CharField(max_length=100)
    has_community_visible_stats = models.BooleanField()

    def __unicode__(self):
        return 'appid:' + str(self.appid) + ', name:' + self.name

class User(models.Model):
    steamid = models.IntegerField(default=0)
    personaname = models.CharField(max_length=100)
   # profileurl = models.CharField(max_length=100)
   # avatar = models.CharField(max_length=100)
   # avatarmedium = models.CharField(max_length=100)
   # avatarfull = models.CharField(max_length=100)
   # realname = models.CharField(max_length=100)
   # friends = models.ManyToManyField('self',blank=True,null=True,symmetrical=False)
    games = models.ManyToManyField(Game)

    def __unicode__(self):
        return 'steamid:' + str(self.steamid) + ', personaname:' + self.personaname



