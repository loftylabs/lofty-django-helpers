# lofty-django-helpers
Lofty's favorite helper methods and modules for Django projects.

## S3 Storage Backends
These custom storage backends for `django-storages` subclass the builtin s3 storage classes allowing you to prefix media and static file S3 paths with the `STATICFILES_LOCATION` and `MEDIAFILES_LOCATION` settings.

Doing this allows you to use a single s3 bucket for static assets and media assets without sharing a directory (which can lead to name collisions or, worse, `collectstatic --clear` nuking your uploaded media files.)

Usage:


```
# in settings.py

STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'lofty_helpers.storage_backends.StaticStorage'
MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'lofty_helpers.storage_backends.MediaStorage'

# And, just general django-storages s3 config, if you need it:

AWS_ACCESS_KEY_ID = '<access_key>'
AWS_SECRET_ACCESS_KEY = '<secret_key>'
AWS_STORAGE_BUCKET_NAME = 'bucket-name'
AWS_S3_REGION_NAME = 'region-name' # i.e., us-east-1

# Tell django-storages the domain to use to refer to static files.
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_AUTO_CREATE_BUCKET = True
AWS_BUCKET_ACL = 'public-read'
```