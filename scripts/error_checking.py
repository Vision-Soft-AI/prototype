from scripts.data_preprocessing import is_valid_image

def check_image(image_path):
    """
    Checks if the image is valid and ready for processing.

    Args:
        image_path: Path to the image file.

    Returns:
        True if the image is valid, False otherwise.
    """
    if not is_valid_image(image_path):
        return False
    # Add more specific error checks here if needed (e.g., image size limitations)
    return True