import threading
import time
from pyvda import VirtualDesktop, get_virtual_desktops
from PIL import Image, ImageDraw, ImageFont
import pystray


from PIL import Image, ImageDraw, ImageFont

def make_icon(number: int) -> Image.Image:
    """Return a 32×32 tray-icon with the desktop number centered in it."""
    size = (48, 48)
    img = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # 1) background circle
    draw.ellipse((0, 0, size[0], size[1]), fill=(0, 120, 215, 255))

    # 2) Pick a TrueType font at a larger point size
    try:
        # You can swap in any .ttf you like that exists on your system
        font = ImageFont.truetype("arial.ttf", 28)
    except IOError:
        # Fallback if that font isn't found
        font = ImageFont.load_default()

    # 2) prepare text
    # font = ImageFont.load_default()
    text = str(number)
    
    # 3) Measure bounding box of the text at (0,0)
    bbox = draw.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    
    # 4) Compute position so that the text's bbox is centered in the circle
    x = (size[0] - text_w) // 2 - bbox[0]
    y = (size[1] - text_h) // 2 - bbox[1]        

    # 5) draw the number
    draw.text((x, y), text, font=font, fill="white")

    return img



def monitor(icon: pystray.Icon):
    """Thread-loop: check every second, update icon if desktop changed."""
    last = None
    while True:
        try:
            current = VirtualDesktop.current().number
        except Exception:
            current = None
        if current != last:
            icon.icon = make_icon(current)
            icon.title = f"Desktop #{current}"
            last = current
        time.sleep(1)

def main():
    # create tray-icon
    icon = pystray.Icon("vd_indicator")
    # initialize with current desktop
    num = VirtualDesktop.current().number
    icon.icon = make_icon(num)
    icon.title = f"Desktop #{num}"
    # start monitor thread
    t = threading.Thread(target=monitor, args=(icon,), daemon=True)
    t.start()
    # run the tray icon loop
    icon.run()
      

if __name__ == "__main__":
    main()
