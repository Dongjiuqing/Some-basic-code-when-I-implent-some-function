import os
import os.path
import shutil

rootdir = "/Users/Dong/Desktop/data_ntu5"

def ListFilesToTxt(dir, file, wildcard, recursion):

    exts = wildcard.split(" ")
    files = os.listdir(dir)
    for name in files:
        fullname = os.path.join(dir, name)
        if (os.path.isdir(fullname) & recursion):
            ListFilesToTxt(fullname, file, wildcard, recursion)
        else:
            for ext in exts:
                print("name",name)
                if (name.endswith(ext)):
                    if "P001" in name or "P002" in name:
                        file.write(name + " 1 " + "\n")
                        break
                    if "P003" in name:
                        file.write(name + " 2 " + "\n")
                        break

def Test():
    for root, dirs, files in os.walk(rootdir):
        for dir in dirs:
            dir_path = os.path.join(rootdir, dir)  # 文件路径
            outfile = "/Users/Dong/Desktop/splits/{}.txt".format(dir)  # 写入的txt文件名
            wildcard = ".avi"  # 要读取的文件类型；
            file = open(outfile, "w")
            if not file:
                print("cannot open the file %s for writing" % outfile)

            ListFilesToTxt(dir_path, file, wildcard, 1)
            file.close()

Test()