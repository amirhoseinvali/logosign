import os
from django.conf import settings
from .ascii_logo_builder import image_to_ascii_with_alpha

def create_ascii_file():
    target_path = os.path.join(os.getcwd(), "logosign.ascii")
    asciilogo_path = os.path.join(os.getcwd(), "") + getattr(settings, 'LOGOSIGN_FILENAME', "logo.png")
    if os.path.exists(asciilogo_path):
        width = getattr(settings, 'LOGOSIGN_WIDTH', 60)
        asciilogo = image_to_ascii_with_alpha(asciilogo_path, width)
    else:
        default_path = os.path.join(os.path.dirname(__file__), "default.ascii")
        with open(default_path, "r", encoding="utf-8") as f:
            asciilogo = f.read()

    with open(target_path, "w", encoding="utf-8") as f:
        f.write(asciilogo)
