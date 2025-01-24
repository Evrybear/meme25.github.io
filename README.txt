Dear successor, here's how to use the packmemes_V2.py script to easily create the website for
the next online MEME event.

1. add packmemes_V2.py & "memetemplate.html" above the folder structure of your memes. It should look like this:

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

2. open packmemes_V2.py and update the year on line 86. (yeah sorry, i was too lazy to automate that)
3. run packmemes_V2.py


If anything fails do these steps:

1. delete the memes folder (html files were already created and if you run the script again, they will be duplicated)
2. delete the index.html file
3. re-add the memes folder