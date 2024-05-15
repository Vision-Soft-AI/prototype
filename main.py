from sys import argv
from scripts.error_checking import check_image

def main():
    if len(argv) != 2:
        print("Usage: python main.py <image_path>")
        return

    image_path = argv[1]
    if check_image(image_path):
        print("Image is ready for manipulation!")
    else:
        print("Error: Image is not valid for processing.")

if __name__ == "__main__":
    main()