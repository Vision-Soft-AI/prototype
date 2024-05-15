from PIL import Image

def preprocess_image(image_path, target_size=(256, 256)):
    """
    Preprocesses an image for further usage.

    Args:
        image_path: Path to the image file.
        target_size: Desired output size (width, height) after resizing.

    Returns:
        A PIL Image object representing the preprocessed image, or None on error.
    """
    try:
        img = Image.open(image_path)
        img = img.resize(target_size, Image.ANTIALIAS)  # Resize with anti-aliasing
        return img
    except (IOError, OSError) as e:
        print(f"Error opening image: {e}")
        return None

def is_valid_image(image_path):
    """
    Checks if the file format is supported (JPG, PNG) and can be opened as an image.

    Args:
        image_path: Path to the image file.

    Returns:
        True if the format is valid and the image can be opened, False otherwise.
    """
    supported_formats = (".jpg", ".jpeg", ".png")
    try:
        return image_path.lower().endswith(supported_formats) and preprocess_image(image_path) is not None
    except Exception as e:
        print(f"Error checking image: {e}")
        return False
