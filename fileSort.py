import shutil
import os
import questionary
from time import sleep

a = input(r"Please input a directory path: ")[1:-1]
parent_dir = a.replace("\\", "/")
commonFileTypes = {
    "jpg": "Image",
    "jpeg": "Image",
    "exe": "Executable",
    "ttf": "Fonts",
    "otf": "Fonts",
    "zip": "Zipped",
    "pdf": "Documents",
    "mp3": "Audio",
    "mp4": "Video",
    "ogg": "Audio",
    "wav": "Video",
    "7z": "Zipped",
}
if os.path.exists(parent_dir):

    def CreateFolder():
        global dir_list
        dir_list = os.listdir(parent_dir)
        for i in dir_list:
            nameL = i.split(".")
            if len(nameL) <= 1:
                continue
            else:
                if (
                    nameL[1]
                    and os.path.exists(parent_dir + "/" + nameL[1] + "Files") == False
                ):
                    os.mkdir(parent_dir + "/" + nameL[1] + "Files")

    def SortFiles():
        global dir_list
        dir_list = os.listdir(parent_dir)
        for i in dir_list:
            nameL = i.split(".")
            if len(nameL) <= 1:
                continue
            else:
                if nameL[1]:
                    shutil.move(
                        f"{parent_dir}/{i}", f"{parent_dir}/{nameL[1]}Files/{i}"
                    )

    CreateFolder()
    sleep(0.5)
    SortFiles()
else:
    print("Please give a proper directory")
