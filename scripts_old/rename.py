import os
import glob
import re

# Define image extensions
exts = ['png', 'jpg', 'jpeg', 'gif']

# Function to sanitize filenames
def sanitize_filename(filename):
    # Remove any characters that are not alphanumeric or the file extension dot
    return re.sub(r'[^a-zA-Z0-9._-]', '_', filename)

# Collect all image files into a single list
image_files = []
for ext in exts:
    image_files.extend(glob.iglob(os.path.join(os.getcwd(), '**', f'*.{ext}'), recursive=True))

# Sort the files to maintain a consistent order
image_files.sort()

# Initialize counter for sequential naming
counter = 1

# Loop through the sorted files and rename them
for filename in image_files:
    # Sanitize the original filename
    sanitized_name = sanitize_filename(os.path.basename(filename))
    
    # Generate new name with padding (e.g., MEME_25_01, MEME_25_02, ...)
    new_name = f"MEME_25_{str(counter).zfill(2)}" + os.path.splitext(sanitized_name)[1]
    
    # Get the directory of the current file
    dir_name = os.path.dirname(filename)
    
    # Construct the new file path
    new_file_path = os.path.join(dir_name, new_name)
    
    # Rename the file
    os.rename(filename, new_file_path)
    
    print(f"Renamed: {filename} -> {new_file_path}")
    
    # Increment the counter for the next image
    counter += 1
