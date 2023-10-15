import os#for list dirs
import pathlib#for extintions
import shutil#copy files

failed = []
files = {}#counts occurances of each file extension 
phone_backup_dir = "/home/marc/Desktop/phone_backup"
try:
    shutil.rmtree(phone_backup_dir)
except:
    os.mkdir(phone_backup_dir)

def search(p):
    try:
        print("path: ",p)
        layer = os.listdir(p)#list
        layer_dirs = []
        #sort dirs and files
        for i in range(len(layer)):
            file_extension = pathlib.Path(layer[i]).suffix
            try:
                os.mkdir(phone_backup_dir+"/"+file_extension)
            except:
                pass
            file_in_path = p+"/"+layer[i]
            if os.path.isfile(file_in_path):
                shutil.copy(file_in_path,phone_backup_dir+"/"+file_extension)
                if file_extension in files.keys():
                    files[file_extension] += 1
                else:
                    files[file_extension] = 1
            else:
                layer_dirs.append(layer[i])
        for i in range(len(layer_dirs)):
            if p.count("/")<10:#depth limit
                search(p+"/"+layer_dirs[i])
    except:
        failed.append(p)
        print("FAILED      ",p,"\n")

path = "/run/user/1000/gvfs/mtp:host=Google_Pixel_7_2B301FDH2000S0/"
search(path)

sorted_files = sorted(files.items(), key=lambda x:x[1])
print(sorted_files)
