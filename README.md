# StableDiffusionXL

This code demonstrates the use of the Stability AI API to generate high-quality images from text prompts using the Stable Diffusion engine. The code uses the requests library to make API calls to the Stability AI API, and it requires a valid API key to be present in a separate config.py file.

### Prerequisites

* Python 3.x
* requests library
* Stability API key

Before running the code, make sure you have installed Python 3.x and the requests library. You also need a valid Stability API key to access the API. Create a config.py file in the same directory as this code and define a variable api_key with your Stability API key.

### Usage

To use the code, simply run the generateStableDiffusionImage() function with the appropriate parameters:

#### generateStableDiffusionImage(prompt, height, width, steps)
* prompt: the text prompt for generating the image
* height: the height of the generated image in pixels
* width: the width of the generated image in pixels
* steps: the number of steps for generating the image (higher values generate higher quality images but take longer to generate)

The generateStableDiffusionImage() function sends a POST request to the Stability AI API with the specified parameters and saves the generated image to a file named v1_txt2img_0.png in the same directory as this code.

The getModelList() function can be used to list all the available models in the Stability AI API.
