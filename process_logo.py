from PIL import Image, ImageOps

def invert_logo():
    try:
        # Load the image
        img = Image.open('logo.png').convert('RGBA')
        
        # Split into channels
        r, g, b, a = img.split()
        
        # Invert the RGB channels
        rgb_image = Image.merge('RGB', (r, g, b))
        inverted_image = ImageOps.invert(rgb_image)
        
        # Combine with original alpha
        r2, g2, b2 = inverted_image.split()
        final_transparent_image = Image.merge('RGBA', (r2, g2, b2, a))
        
        # Save
        final_transparent_image.save('logo_white.png')
        print("Logo invertido guardado como 'logo_white.png'")
        
    except Exception as e:
        print(f"Error procesando logo: {e}")

if __name__ == '__main__':
    invert_logo()
