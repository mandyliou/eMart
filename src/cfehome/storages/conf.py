from cfehome.env import config

AWS_ACCESS_KEY_ID=config("AWS_ACCESS_KEY_ID", default=None)
AWS_SECRET_ACCESS_KEY=config("AWS_SECRET_ACCESS_KEY", default=None)
AWS_S3_SIGNATURE_VERSION="s3v4"
AWS_STORAGE_BUCKET_NAME = "micro-ecommerce"
AWS_S3_ENDPOINT_URL=f"https://{AWS_STORAGE_BUCKET_NAME}.us-sea-1.linodeobjects.com"

AWS_DEFAULT_ACL="public-read"
AWS_S3_USE_SSL = True

#file upload storage default
# STORAGES = {
#     "default": {
#         "BACKEND": "cfehome.storages.backends.MediaStorage",
#     },
# }

# #staticfiles
# STATICFILES_STORAGE ="cfehome.storages.backends.StaticFileStorage"

STORAGES = {
    "default": {
        "BACKEND": "cfehome.storages.backends.MediaStorage",
        "OPTIONS": {
            # ...your_options_for_media_here
        },
    },
    "staticfiles": {
        "BACKEND": "cfehome.storages.backends.StaticFileStorage",
        "OPTIONS": {
            # ...your_options_for_static_here
        },
    },
}
