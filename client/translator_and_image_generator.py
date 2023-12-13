import requests
import json
import translators as ts

def interpreter(text):  
    return ts.translate_text(query_text= text, from_language='ru', to_language='en')

def get_picture(text):
    url = "https://stablediffusionapi.com/api/v3/text2img"

    payload = json.dumps({
        "key": "s29JCMM84AoNOGLWBlamyWKVZQIsghIlL6TKhYQNCEFB0lhPttl23J302j6f",
        "prompt": f"{text}",
        "negative_prompt": None,
        "width": "720",
        "height": "720",
        "samples": "1",
        "num_inference_steps": "20",
        "seed": None,
        "guidance_scale": 7.5,
        "safety_checker": "yes",
        "multi_lingual": "no",
        "panorama": "no",
        "self_attention": "no",
        "upscale": "yes",
        "embeddings_model": None,
        "webhook": None,
        "track_id": None
    })

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    output_url = response.json()
    print(output_url)
    img_url = output_url['output'][0]
    print(img_url)
    return img_url











