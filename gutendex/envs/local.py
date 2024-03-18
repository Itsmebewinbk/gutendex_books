from decouple import config

print('Mode: Local')

# Rest settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 20,
    'EXCEPTION_HANDLER':
        'gutendex.config.exception_handler.CustomExceptionHandler',

    'DEFAULT_RENDERER_CLASSES': ['gutendex.config.renderers.CustomJSONRenderer'],

}

