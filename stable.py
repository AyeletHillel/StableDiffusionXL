import os
import requests
import config
import base64
import json

api_host = 'https://api.stability.ai'
engine_id = 'stable-diffusion-xl-beta-v2-2-2'
api_key = config.api_key
if api_key is None:
    raise Exception("Missing Stability API key.")

def getModelList():
    url = f"{api_host}/v1/engines/list"
    response = requests.get(url, headers={"Authorization": f"Bearer {api_key}"})

    if response.status_code == 200:
        payload = response.json()
        print(payload)


def generateStableDiffusionImage(prompt, height, width, steps):
    url = f"{api_host}/v1/generation/{engine_id}/text-to-image"
    headers = {"Content-Type": "application/json", "Accept": "application/json","Authorization": f"Bearer {api_key}"}
    
    payload = {}
    payload['text_prompts'] = [{ "text": f"{prompt}"}]
    payload['cfg_scale'] = 7
    payload['clip_guidance_preset'] = "FAST_BLUE"
    payload['height'] = height
    payload['width'] = width
    payload['samples'] = 1
    payload['steps'] = steps
    
    response = requests.post(url, headers=headers,json=payload)
    
    if response.status_code == 200:
        data = response.json()        
        for i, image in enumerate(data["artifacts"]):
            with open(f"v1_txt2img_{i}.png", "wb") as f:
                f.write(base64.b64decode(image["base64"]))


prompt = 'Create a high resolution picture image of a luxury car in a studio setting udio setting, showcasting its lines and high-end features. Perfect lighting with highlights.'
generateStableDiffusionImage(prompt, 512, 512, 15)