REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        #'rest_framework.throttling.UserRateThrottle'
    ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '120/minute',
        #'user': '60/minute',
        'GetDataWatermlRateThrottle_User': "60/mintue",
        'GetDataWatermlRateThrottle_Anon': '3/minute',
        'SubsetWatershedApiRateThrottle_User': '60/minute',
        'SubsetWatershedApiRateThrottle_Anon': '3/minute',
    },
    # 'DEFAULT_PERMISSION_CLASSES': (
    #     'rest_framework.permissions.IsAuthenticated',
    # ),
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #     'rest_framework.authentication.TokenAuthentication',
    # )
}
