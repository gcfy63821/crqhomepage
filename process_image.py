from PIL import Image
import os

def resize_and_compress_image(input_path, output_path, max_width, max_height, quality):
    """
    Resize and compress an image for web use.

    Args:
        input_path (str): Path to the input image.
        output_path (str): Path to save the output image.
        max_width (int): Maximum width for the resized image.
        max_height (int): Maximum height for the resized image.
        quality (int): Quality level for compression (1-95, higher means better quality).
    """
    try:
        # Open the input image
        with Image.open(input_path) as img:
            # Resize the image while maintaining aspect ratio
            img.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)

            # Save the image with compression
            img.save(output_path, "JPEG", quality=quality)

        print(f"Image successfully resized and saved to {output_path}")

    except Exception as e:
        print(f"Error processing image: {e}")

# Example usage
if __name__ == "__main__":
    # Define input and output paths
    input_image = "my_photo.jpg"  # Replace with your input file
    output_image = "optimized_image.jpg"  # Replace with your output file

    # Set maximum dimensions and quality level
    max_width = 1024  # Maximum width in pixels
    max_height = 768  # Maximum height in pixels
    quality = 85  # Compression quality (1-95)

    # Resize and compress the image
    resize_and_compress_image(input_image, output_image, max_width, max_height, quality)
