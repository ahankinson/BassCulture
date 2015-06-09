from django.conf import settings


def diva_settings(request):
    return {
        'IIP_SERVER': settings.IIP_SERVER,
        'IIP_SERVER_IMAGE_PATH': settings.IIP_SERVER_IMAGE_PATH,
        'DIVA_OBJECT_DATA': settings.DIVA_OBJECT_DATA
    }
