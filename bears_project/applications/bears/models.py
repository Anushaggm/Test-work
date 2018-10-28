# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Bear(models.Model):
    """Model, which represents a bear entity.
    :name: Name of the bear.
    :bear_type: Official bear type.
    """
    name = models.CharField(_('Name'), max_length=128, )

    bear_type = models.CharField(_('Name'),max_length=128,choices=(
        ('grizzy', _('Grizzy')),
        ('mini', _('Mini')),
                                                                    ),
    )