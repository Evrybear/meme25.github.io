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
    <ul>
"""

    # Walk through the base folder and subfolders
    for root, _, files in os.walk(base_path):
        for file in files:
            if file.endswith('.html'):
                # Get the relative path to the HTML file
                relative_path = os.path.relpath(os.path.join(root, file), base_path)
                # Generate the display name (e.g., Meme 01, Meme 02, ...)
                meme_name = os.path.splitext(os.path.basename(file))[0]
                # Add the link to the HTML content
                html_content += f'        <li><a href="{relative_path}">{meme_name}</a></li>\n'

    # Close the HTML content
    html_content += """    </ul>
</body>
</html>
"""

    # Write the HTML content to an index.html file
    index_file_path = os.path.join(base_path, 'index.html')
    with open(index_file_path, 'w', encoding='utf-8') as index_file:
        index_file.write(html_content)

    print(f"index.html has been generated at: {index_file_path}")


# Replace 'your_base_folder_path_here' with the path where your folders are located
base_folder = os.getcwd()
generate_index_html(base_folder)
