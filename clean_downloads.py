

import os
import shutil

home = os.environ.get('HOME')

conf_dir = home + "/.config/user-dirs.dirs"

with open(conf_dir,"r") as f:
    lines = f.readlines()

music_path = ""
pictures_path = ""
videos_path = ""
documents_path = ""
download_path = ""

music_fileendings = ('.mp3','.flac')
picture_fileendings = ('.png','.jpg','.jpeg','.gif')
video_fileendings = ('.mp4','.mkv','.mov')
document_fileendings = ('.pdf','.doc','docx','.xlsx','.odt','.ods')



for l in lines:
    if l[0:12] in  'XDG_MUSIC_DIR':
        music_path = home + l.split('"')[1][5:]

    if l[0:15] in  'XDG_PICTURES_DIR':
        pictures_path = home + l.split('"')[1][5:]

    if l[0:13] in  'XDG_VIDEOS_DIR':
        videos_path = home + l.split('"')[1][5:]

    if l[0:16] in  'XDG_DOCUMENTS_DIR':
        documents_path = home + l.split('"')[1][5:]

    if l[0:16] in  'XDG_DOWNLOAD_DIR':
        download_path = home + l.split('"')[1][5:]

for file in os.listdir(download_path):
    if file.endswith(music_fileendings):
        shutil.move(download_path +"/"+ file,music_path +"/"+ file)
    elif file.endswith(picture_fileendings):
        shutil.move(download_path +"/"+ file,pictures_path +"/"+ file)
    elif file.endswith(video_fileendings):
        shutil.move(download_path +"/"+ file,videos_path +"/"+ file)
    elif file.endswith(document_fileendings):
        shutil.move(download_path +"/"+ file,documents_path +"/"+ file)
    else:
        pass #do nothing
