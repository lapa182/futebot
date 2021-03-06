import requests

from util.helpers import generate_image_search_url, validate_image, create_discord_file_object


def get_image(ctx, search_query, spoiler, **kwargs):
    file_type = ".gif" if kwargs.get("gif", None) else ".jpg"

    url = generate_image_search_url(search_query, file_type)
    res = requests.get(url)
    search_result = res.json()
    if "items" not in search_result:
        raise Exception("We couldn't find any images for your search")
    image_is_valid = False

    for item in search_result["items"]:
        image_link = item["link"]
        image_is_valid, file_bytes = validate_image(image_link)
        if image_is_valid:
            f = create_discord_file_object(file_bytes, file_type, spoiler)
            return f
            break
