from PIL import Image
import os

def compress_image(input_path, output_path, quality=85):
    with Image.open(input_path) as img:
        # Get the file extension
        file_extension = os.path.splitext(output_path)[1].lower()
        
        if file_extension == '.jpg' or file_extension == '.jpeg':
            # Convert to RGB if image is in RGBA mode
            if img.mode == 'RGBA':
                img = img.convert('RGB')
            # Save as JPEG
            img.save(output_path, 'JPEG', quality=quality)
        elif file_extension == '.png':
            # For PNG, we use optimize=True and adjust the compression level
            img.save(output_path, 'PNG', optimize=True, compress_level=quality)
        else:
            print(f"Unsupported file format: {file_extension}")
            return

    # Calculate compression percentage
    original_size = os.path.getsize(input_path)
    compressed_size = os.path.getsize(output_path)
    saving = (original_size - compressed_size) / original_size * 100

    print(f"Original size: {original_size/1024:.2f}KB")
    print(f"Compressed size: {compressed_size/1024:.2f}KB")
    print(f"Saved: {saving:.2f}%")

# Example usage
input_image = './RED-D.png'
output_image = './RED-D-compressed.png'  # Note: This can be .png or .jpg
quality = 85  # For JPEG: 0-95 (lower means more compression)
              # For PNG: 0-9 (higher means more compression)

compress_image(input_image, output_image, quality)