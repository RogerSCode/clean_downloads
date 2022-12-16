

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


file_types = {
    music_fileendings: music_path,
    picture_fileendings: pictures_path,
    video_fileendings: videos_path,
    document_fileendings: documents_path
}

for file in os.listdir(download_path):
    for endings, path in file_types.items():
        if file.endswith(endings):
            shutil.move(download_path + "/" + file, path + "/" + file)
            break
