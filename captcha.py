import string
import random
from captcha.image import ImageCaptcha
from PIL import Image
import random

# Function to generate a random CAPTCHA text of specified length
def captcha_image_text(length=10):
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))

# Function to generate and save CAPTCHA image
def captcha_image(captcha_text, image_width=300):
    image = ImageCaptcha(image_width)
    image_file = f"{captcha_text}.png"
    image.write(captcha_text, image_file)
    return image_file

# Generate random CAPTCHA text
captcha_text = captcha_image_text()

# Create and save the CAPTCHA image
image_file = captcha_image(captcha_text=captcha_text)

# Output message and open the generated CAPTCHA image
print(f"Generated CAPTCHA: {captcha_text}")
Image.open(image_file).show()  # Use .show() to open the image
