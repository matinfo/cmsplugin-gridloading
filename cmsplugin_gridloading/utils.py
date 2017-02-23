from django.conf import settings


def get_additional_effects():
    """
    Get additional effect choices from settings
    """
    choices = []
    raw = getattr(settings, 'GRIDLOADING_EFFECTS', False)
    if raw:
        if isinstance(raw, basestring):
            raw = raw.split(',')
        for choice in raw:
            clean = choice.strip()
            choices.append((clean.lower(), clean.title()))
    return choices
