from celery import shared_task
import requests
import os

from chaotix import settings
from .models import GeneratedImage


@shared_task
def generate_image(text_prompt,width,height):
    engine_id = "stable-diffusion-xl-1024-v1-0"
    api_host = settings.API_HOST
    api_key = settings.STABILITY_API_KEY

    if api_key is None:
        raise Exception("Missing Stability API Key.")


    response = requests.post(
        f"{api_host}/v1/generation/{engine_id}/text-to-image",
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {api_key}"
        },
        json={
            "text_prompts": [
                {
                    "text": text_prompt
                }
            ],
            "cfg_scale": 7,
            "height": height,
            "width": width,
            "samples": 1,
            "steps": 30
        },
    )

    if response.status_code!=200:
        raise Exception(("Non-200 response: " + str(response.text)))

    data = response.json()
    print(data)

    image_data=data["artifacts"][0]["base64"]
    # Save image data in Django
    generated_image = GeneratedImage.objects.create(
        text_prompt=text_prompt, image_data=image_data
    )

    # generated_image = GeneratedImage(
    #     text_prompt=text_prompt, image_data=image_data
    # )
    # generated_image.save()

    # print(generated_image)
    return generated_image.pk
    # return data["artifacts"][0]["base64"]

#
# def test_func(self):
#     # operations
#     for i in range(10):
#         print(i)
#     return "Done"
