DEBUG = True 

#######################################################################
# These config values vary on an install-by-install basis. If you
# installed using the Ubuntu package, these should be pre-set.
#######################################################################

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'localwiki',
        'USER': 'localwiki',
        'PASSWORD': 'hKxvPeSz4B7Ia2Qj1UDTVtGneKsapg',
        'HOST': '127.0.0.1',
    }
}

# Get an API key at http://cloudmade.com/start.
CLOUDMADE_API_KEY = '01555da409f94a88bc0b564bc549e000'

# Use these email settings when running the python debugging smtp server
# python -m smtpd -n -c DebuggingServer localhost:1025
EMAIL_HOST = 'localhost'
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 1025
EMAIL_USE_TLS = False

#######################################################################
# Other config values.
#######################################################################

SITE_THEME = 'maketylerweird'

OLWIDGET_DEFAULT_OPTIONS = {
    'default_lat': 37.76,
    'default_lon': -122.43,
    'default_zoom': 12,
    'zoom_to_data_extent_min': 16,

    'layers': ['cloudmade.35165', 've.aerial'],
    'map_options': {
        'controls': ['Navigation', 'PanZoomBar', 'KeyboardDefaults'],
        'theme': '/static/openlayers/theme/sapling/style.css',
    },
    'overlay_style': {'fillColor': '#ffc868',
                      'strokeColor': '#db9e33',
                      'strokeDashstyle': 'solid'},
    'map_div_class': 'mapwidget',
}

DAISYDIFF_URL = 'http://localhost:8080/daisydiff/diff'
DAISYDIFF_MERGE_URL = 'http://localhost:8080/daisydiff/merge'

# list of regular expressions for white listing embedded URLs
EMBED_ALLOWED_SRC = ['.*']

HAYSTACK_SOLR_URL = 'http://localhost:8080/solr'

LOCAL_INSTALLED_APPS = ()

CACHE_BACKEND = 'dummy:///'

# This is auto-generated.
SECRET_KEY = 'k&%@*uiw&if74(71ok8nzmb7jjx7uqad4oe@@)41lb&li^y#qi'
