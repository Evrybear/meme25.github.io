import os
import glob
import re

# Enter the year manually
YEAR = "2025"

#================================================================================================================
#                                                   rename.py
#================================================================================================================

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
    
    # Generate new name with padding (e.g., MEME_2025_01, MEME_2025_02, ...)
    new_name = f"MEME_{YEAR}_{str(counter).zfill(2)}" + os.path.splitext(sanitized_name)[1]
    
    # Get the directory of the current file
    dir_name = os.path.dirname(filename)
    
    # Construct the new file path
    new_file_path = os.path.join(dir_name, new_name)

    # Ensure the new file name does not already exist
    while os.path.exists(new_file_path):
        counter += 1
        new_name = f"MEME_{YEAR}_{str(counter).zfill(2)}" + os.path.splitext(sanitized_name)[1]
        new_file_path = os.path.join(dir_name, new_name)
    
    # Rename the file
    os.rename(filename, new_file_path)
    
    print(f"Renamed: {filename} -> {new_file_path}")
    
    # Increment the counter for the next image
    counter += 1


#================================================================================================================
#                                                   packmemes.py
#================================================================================================================

template = open("memetemplate.html", "r")

template_text = template.read()

exts = ['png', 'jpg', 'jpeg', 'gif']

# Clean up old .html files (except memetemplate.html and index.html)
old_html_files = 0
for root, _, files in os.walk(os.getcwd()):
    for file in files:
        if file.endswith('.html') and file not in ("memetemplate.html", "index.html"):
            os.remove(os.path.join(root, file))
            old_html_files += 1

if old_html_files > 0:
    print("Old HTML files detected. Cleaning up...")
    print(f"{old_html_files} HTML files have been successfully replaced.")
else:
    print("No old HTML files detected.")

# Generate new .html files for each image
for ext in exts:
    for filename in glob.iglob(os.getcwd() + "**/**/*." + ext, recursive=True):
        meme_html = open(filename + ".html", "w")
        meme_html.write(template_text.replace("MEME_SRC", os.path.basename(filename)))
        meme_html.close()

template.close()



#================================================================================================================
#                                                   generateindex.py
#================================================================================================================

def generate_index_html(base_path):
    # Start the HTML content
    html_content = f"""<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>Meme Gallery {YEAR}</title>
</head>
<body>
    <h1>MEME {YEAR} Gallery</h1>
"""

    # Initialize a counter for the numbering
    meme_counter = 1

    # Walk through the base folder and subfolders
    for root, _, files in os.walk(base_path):
        # Filter HTML files in the current folder, ignoring memetemplate.html and index.html
        html_files = [file for file in files if file.endswith('.html') and file not in ("memetemplate.html", "index.html")]

        if html_files:  # Only process folders with HTML files
            # Add folder title as an <h2>
            folder_name = os.path.basename(root)  # Get the name of the current folder
            html_content += f'    <h2>{folder_name}</h2>\n'

            for file in html_files:
                # Get the relative path to the HTML file
                relative_path = os.path.relpath(os.path.join(root, file), base_path)
                # Generate the display name (e.g., Meme 01, Meme 02, ...)
                display_name = f"Meme {str(meme_counter).zfill(2)}"
                # Add the link to the HTML content
                html_content += f'        <li><a href="{relative_path}">{display_name}</a></li>\n'
                # Increment the counter
                meme_counter += 1

    # Close the HTML content
    html_content += """</body>
</html>
"""

    # Write the HTML content to an index.html file
    index_file_path = os.path.join(base_path, 'index.html')

    # Check if index.html already exists
    if os.path.exists(index_file_path):
        print("index.html already exists. Replacing it...")
    else:
        print("index.html not found. Creating a new one...")

    with open(index_file_path, 'w', encoding='utf-8') as index_file:
        index_file.write(html_content)

    print("index.html successfully replaced.")
        

# Replace 'your_base_folder_path_here' with the path where your folders are located
base_folder = os.getcwd()
generate_index_html(base_folder)
