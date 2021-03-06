import datetime
from django.db import models
from django.template.defaultfilters import slugify
from preps.apps.models import ModelBase
from preps.apps.sports.models import Season, School, MeetBase, Sport, Player, Conference
from preps.apps.utils import functions as preps_utils

class Meet(MeetBase):
    season                          = models.ForeignKey(Season, related_name='cross_country_meet_season')
    teams                           = models.ManyToManyField(School, null=True, related_name='cross_country_meet_teams')
    
    def __unicode__(self):
        if self.meet_date_and_time == None or self.meet_date_and_time == '':
            return u'Meet: %s cross-country (%s)' % (self.get_status_display(), self.id)
        else:
            return u'Meet [%s]: %s cross-country (%s)' % (self.meet_date_and_time, self.get_status_display(), self.id) 
    
    def save(self, *args, **kwargs):
        if self.slug == None or self.slug == '':
            self.slug               = slugify(self.__unicode__())
        super(Meet, self).save(*args, **kwargs)