from django import template
from myMusicApp.utils import get_profile

register = template.Library()

@register.simple_tag
def get_user():
    return get_profile()