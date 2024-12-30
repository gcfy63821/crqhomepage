from PIL import Image

def convert_to_ico(input_path, output_path):
    """
    Convert an image to ICO format.

    Args:
        input_path (str): Path to the input image file.
        output_path (str): Path to save the output ICO file.
    """
    try:
        # Open the input image
        img = Image.open(input_path)

        # Convert and save as .ico
        img.save(output_path, format='ICO')

        print(f"Image successfully converted to {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    input_image_path = "2.png"  # Replace with your input image path
    output_ico_path = "page_icon.ico"   # Replace with your desired output path

    convert_to_ico(input_image_path, output_ico_path)
