import os
from PIL import Image

# Configuration
input_folder = "Image Resizer Tool/input_images"
output_folder = "Image Resizer Tool/resized_images"
target_size = (800, 600)  # Width x Height
output_format = "JPEG"    # Options: JPEG, PNG, WEBP, etc.

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Supported image extensions
valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.webp')

# Resize and convert images
for filename in os.listdir(input_folder):
    if filename.lower().endswith(valid_extensions):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(
            output_folder,
            os.path.splitext(filename)[0] + "." + output_format.lower()
        )

        try:
            with Image.open(input_path) as img:
                # Convert RGBA to RGB if saving as JPEG
                if output_format.upper() == "JPEG" and img.mode == "RGBA":
                    img = img.convert("RGB")

                resized_img = img.resize(target_size, Image.Resampling.LANCZOS)
                resized_img.save(output_path, output_format)
                print(f"✅ Processed: {filename} → {output_path}")
        except Exception as e:
            print(f"❌ Error processing {filename}: {e}")
