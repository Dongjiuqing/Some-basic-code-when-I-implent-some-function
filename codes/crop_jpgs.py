import os
import os.path
from PIL import Image

for classnum in range(46,61):
    rootdir = "/Users/Dong/Desktop/ntu_jpg/A"+str(classnum).rjust(3,"0")
    # print(rootdir)
    for root, dirs, files in os.walk(rootdir):

        for file in files:
            if file.endswith(".jpg"):

                img_path = os.path.join(root,file)
                img = Image.open(img_path)
                # (900, 675) = 4 : 3   resize (320, 240)  =  2.8125 倍
                cropped = img.crop((500, 200, 1400, 875))  # (left, upper, right, lower)
                cropped_resize = cropped.resize((320, 240))

                #cropped_path = root.replace("ntu_jpg", "ntu_jpg_crop")
                cropped_resize_path = root.replace("ntu_jpg", "ntu_jpg_crop_resize")

                #if not os.path.exists(cropped_path):
                #    os.makedirs(cropped_path)
                #    print("ok")
                if not os.path.exists(cropped_resize_path):
                    os.makedirs(cropped_resize_path)
                    print("cropped_resize_path", cropped_resize_path)

                #cropped_path = os.path.join(cropped_path, file)
                cropped_resize_path = os.path.join(cropped_resize_path, file)

                #cropped.save(cropped_path)
                cropped_resize.save(cropped_resize_path)