from django.conf import settings

def options_selector(request):
    return { 'OPTIONS' : settings.OPTIONS_ID, 'NUMERIC' : settings.NUMERIC_ID, 'BOOL' : settings.BOOL_ID, 'TEXT': settings.TEXT_ID}

