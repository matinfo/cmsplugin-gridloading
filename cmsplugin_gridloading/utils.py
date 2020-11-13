from django.conf import settings


def get_additional_effects():
    """
    Get additional effect choices from settings
    """
    choices = []
    raw = getattr(settings, 'GRIDLOADING_EFFECTS', False)
    if raw:
        if isinstance(raw, str):
            raw = raw.split(',')
        for choice in raw:
            clean = str(choice).strip()
            choices.append((clean.lower(), clean.title()))
    return choices
