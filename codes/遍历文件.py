import os
import os.path
import shutil

rootdir = "/Users/Dong/Desktop/video"
movedir = "/Users/Dong/Desktop/video_test"

'''
for root, dirs, files in os.walk(rootdir):
    for name in files:
        for f in range(1,61):
            classname = "A" + str(f).rjust(3, "0")
            movepath = os.path.join(movedir, classname)
            if classname in name:
                filepath = os.path.join(root, name)
                move_to_path = os.path.join(movepath, name)
                shutil.copyfile(filepath, move_to_path)
                print(move_to_path)
'''