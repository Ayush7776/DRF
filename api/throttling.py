from rest_framework.throttling import UserRateThrottle

class KunalThrottle(UserRateThrottle):
    scope='kunu'