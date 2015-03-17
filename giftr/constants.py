import os

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT =  587
EMAIL_HOST_USER = os.environ.get('GIFTR_GMAIL_USERNAME','')
EMAIL_HOST_PASSWORD = os.environ.get('GIFTR_GMAIL_PW','')
EMAIL_USE_TLS = True