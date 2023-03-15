from shortuuid import ShortUUID



SHORT_URL_LENGTH = 16


def get_unique_short_id(original_url):
    return ShortUUID().random(length=SHORT_URL_LENGTH)
