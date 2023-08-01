#! python 3
# organizes files into folders based on their extension

import os
import shutil


def organize_files(folder):
    files = os.listdir(folder)
    for filename in files:
        # get a suffix
        try:
            suffix = filename.split('.')[1]
        except IndexError:
            continue

        # do not move python scripts and .git repos
        if suffix in ('py', 'git'):
            continue

        # create the folder if it does not exist
        if suffix not in files:
            os.mkdir(os.path.join(folder, suffix))

        source = os.path.join(folder, filename)
        destination = os.path.join(folder, suffix, filename)

        # index for copies
        i = 1

        # if the file already in the folder
        while os.path.exists(destination):
            new_filename = f"{os.path.splitext(filename)[0]}_copy{i}.{suffix}"
            destination = os.path.join(folder, suffix, new_filename)
            i += 1
        os.rename(os.path.join(folder, filename), os.path.join(folder, new_filename))
        source = os.path.join(folder, new_filename)

        shutil.move(source, destination)


organize_files('.\\')
