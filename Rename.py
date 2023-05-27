import os

desktop = os.path.expanduser('~\\Desktop\\for rn')
remove = "[SPOTIFY-DOWNLOADER.COM] "

for filename in os.listdir(desktop):
    f = os.path.join(desktop, filename)
    reformatted_name = f.replace(remove, '')
    print(filename, "-->", filename.replace(remove, ''))
    os.rename(f, reformatted_name)
