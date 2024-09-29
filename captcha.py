import string
from captcha.image import ImageCaptcha
from PIL import Image
import random

def captcha_image_text(lenght=10):
    return " ".join(random.choices(string.ascii_letters + string.digits, k=lenght))

def captcha_image(captcha_text,image_width=300):
    image = ImageCaptcha(image_width)
    image_file = f"{captcha_text}.png"
    image.write(captcha_text,image_file)
    return image_file


captcha_text = captcha_image_text()
image_file = captcha_image(captcha_text=captcha_text)

# file added
print(f"Generated Captcha")
Image.open(image_file)
