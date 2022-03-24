from django import template

register = template.Library()


@register.filter
def is_attending(user, event):
    return user.profile.attending.filter(id=event.id).exists()
