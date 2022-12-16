# clean_downloads
A script to tidy up the downloads folder by moving files into directories that correspond to their file type.


## Requirements

Python 3.8.10 or higher (older versions may also work but have not been tested)



## Usage:
    python clean_downloads

on some linux distros:
    
    python3 clean_downloads


## Suported filetypes:


- Music: .mp3 and .flac

- Pictures: .png, .jpg, .jpeg, and .gif

- Video: .mp4, .mkv, and .mov
    
- Documents: .pdf, .doc, .docx, .xlsx, .odt, and .ods

## Note

This script assumes that the directories for the different file types (e.g. music, pictures, etc.) are stored in the user's home directory and are specified in the user-dirs.dirs configuration file located in the .config directory. If this is not the case on your system, you will need to modify the script accordingly.