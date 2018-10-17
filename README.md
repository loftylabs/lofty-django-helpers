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
```