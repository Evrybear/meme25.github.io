Dear successor, here's how to use the packmemes_V2.py script to easily create the website for
the next online MEME event.

To use this template successfully, you need:
- the file: packmemes_V3.py
- the file: memetemplate.html
- One folder containing your memes in subfolders

Step by step guide:

1.  add packmemes_V3.py & "memetemplate.html" above the folder structure of your memes. It should
    look like this (you can use your own folder names of course):

    your_github_repository/
    ├─ MEMEs_202X/
    │  ├─ Coding_memes/
    │  │  ├─ funnymeme.png
    │  │  ├─ sad_meme.jpg
    │  ├─ Student_life_memes/
    │  │  ├─ kms_meme.jpeg
    │  ├─ racoon_memes/
    │  │  ├─ dank_shit.gif
    ├─ memetemplate.html
    ├─ packmemes_V2.py

2. open packmemes_V3.py
3. Change the year on line 6
4. Run packmemes_V3.py

It should now:
- automatically rename all files (to avoid any troubles with silly characters and emojis in the name)
- check for already created HTML files of your images (in case you run the script multiple times)
- create the index.html file with links to all your memes with a structure according to your subfolder names