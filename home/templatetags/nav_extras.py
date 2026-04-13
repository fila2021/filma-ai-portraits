from django import template

register = template.Library()


@register.filter
def starts_with(value, arg):
    """Return True if value starts with arg."""
    try:
        return str(value).startswith(str(arg))
    except Exception:
        return False
