import os
import glob

template = open("memetemplate.html", "r")

template_text = template.read()

exts = ['png', 'jpg', 'jpeg', 'gif']

for ext in exts:
    for filename in glob.iglob(os.getcwd() + "**/**/*." + ext, recursive=True):
        meme_html = open(filename + ".html", "w")
        meme_html.write(template_text.replace("MEME_SRC", os.path.basename(filename)))
        meme_html.close()

template.close()