import os

def generate_index_html(base_path):
    # Start the HTML content
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meme Gallery</title>
</head>
<body>
    <h1>MEME 25 Gallery</h1>
"""

    # Initialize a counter for the numbering
    meme_counter = 1

    # Walk through the base folder and subfolders
    for root, _, files in os.walk(base_path):
        # Filter HTML files in the current folder, ignoring memetemplate.html
        html_files = [file for file in files if file.endswith('.html') and file != "memetemplate.html"]

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
    with open(index_file_path, 'w', encoding='utf-8') as index_file:
        index_file.write(html_content)
        

# Replace 'your_base_folder_path_here' with the path where your folders are located
base_folder = os.getcwd()
generate_index_html(base_folder)
