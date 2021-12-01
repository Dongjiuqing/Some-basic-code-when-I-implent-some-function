import os
import timeit
i = 0
action_set = [1, 2, 3, 10, 11, 12, 16, 17, 28, 29, 30, 31, 32, 41, 44, 47]

for pathname,dirnames,filenames in os.walk('/Volumes/FILES/2s-AGCN-master16/dataset/nturgb+d_skeletons/'):
    for filename in filenames:
        action_class = int(filename[filename.find('A') + 1:filename.find('A') + 4])
        print(filename)

        if action_class not in action_set:
            i+=1
            file = os.path.join(pathname, filename)
            os.remove(file)
            print("OK")
print(i)
print(56880 - i)