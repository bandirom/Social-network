import os


# AUTH_USER_MODEL = 'app.UserProfile'

"""SignUp settings via email"""
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_UNIQUE_EMAIL = True


"""Login Attempt Limit"""
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 60


"""Email setting"""
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = "bandirom1@gmail.com"
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_PASS"),
EMAIL_PORT = 587

"""Login and Logout URL redirection"""
LOGIN_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_REDIRECT_URL = "/"


# ACCOUNT_SIGNUP_FORM_CLASS = 'app.profile.forms.SignupForm'
ACCOUNT_FORMS = {
    # 'signup': 'app.forms.CustomSignupForm',
    'change_password': 'app.profile.forms.ChangePassForm'
}


AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': os.environ.get("Google_client_id"),
            'secret': os.environ.get("Google_secret"),
            'key': os.environ.get("Google_key")
        }
    },
    'facebook': {
        'APP': {
            'client_id': os.environ.get("FB_client_id"),
            'secret': os.environ.get("FB_secret"),
            'key': os.environ.get("FB_key")
        },
        'METHOD': 'oauth2',
        'SCOPE': ['email', 'public_profile', 'user_birthday'],

        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'id',
            'email',
            'name',
            'picture',
            'first_name',
            'last_name',
            'verified',
            'locale',
            'timezone',
            'link',
            'gender',
            'updated_time',
        ],
        'EXCHANGE_TOKEN': True,
        'VERIFIED_EMAIL': True,
        'VERSION': 'v7.0',
    }
}
