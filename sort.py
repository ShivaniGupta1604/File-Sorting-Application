import os, shutil

folders = {'videos': ['.mp4'],
         'audios': ['.wav','.mp3'],
         'images': ['.jpg','.png'],
         'documents': ['.doc','.xls','.xlsx','.pdf','.zip','.rar','.txt','.pptx']
         }

def rename_folder():
    for folder in os.listdir(directory):
        if os.path.isdir(directory):
            if os.path.isdir(os.path.join(directory, folder)) == True:
                os.rename(os.path.join(directory, folder), os.path.join(directory, folder.lower()))

def create_move(ext, file_name):
    find = False
    for folder_name in folders:
        if "."+ext in folders[folder_name]:
            find=True
            if folder_name not in os.listdir(directory):                 # It will make a new folders with req folder name for moving files
                os.mkdir(os.path.join(directory, folder_name))
            shutil.move(os.path.join(directory, file_name), os.path.join(directory, folder_name))     # moving the folder from current files to requierd folder.
            break

    if find == False:
        if other_name not in os.listdir(directory):
            os.mkdir(os.path.join(directory, other_name))
        shutil.move(os.path.join(directory, file_name), os.path.join(directory, other_name))



directory = "C:/Users/LENOVO/Downloads"     # input("Enter the location")
other_name= input("Enter the folder name for other names")
all_files = os.listdir(directory)    # This makes a list of all the files present on the given location.

length= len(all_files)
count = 1

rename_folder()

for i in all_files:
    if os.path.isfile(os.path.join(directory,i)) == True:     # It returns true if the file present in the given location is a file and not a folder.
        create_move(i.split(".")[-1], i)                      #   we have used (os.path.join) so that we don't need to write it as (directory + "\\" + i)

    print("Total Files: {} | Done: {} | Left: {}".format(length, count, length-count))                                                      # we use split to get the extension of the files present, i is the file name.
    count += 1

