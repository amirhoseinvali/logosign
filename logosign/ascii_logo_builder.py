from PIL import Image

ASCII_CHARS = "█▓▒░."
THRESHOLD = 240

def image_to_ascii_with_alpha(path, width=100):
    image = Image.open(path).convert("RGBA")
    aspect_ratio = image.height / image.width
    height = int(width * aspect_ratio * 0.5)
    image = image.resize((width, height))

    ascii_art = ""
    pixels = image.getdata()

    for y in range(height):
        row = ""
        for x in range(width):
            r, g, b, a = pixels[y * width + x]

            if a == 0:
                row += " "
                continue

            gray = int(0.299*r + 0.587*g + 0.114*b)
            if gray > THRESHOLD:
                row += " "
            else:
                index = gray * (len(ASCII_CHARS) - 1) // 255
                row += ASCII_CHARS[index]
        ascii_art += row + "\n"

    return ascii_art