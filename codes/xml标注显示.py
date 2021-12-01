import xml.etree.ElementTree as ET
import cv2
import os


xml_path = '/Users/Dong/Desktop/test/dataset_aug/train_png_xml'     # 你的xml文件路径
img_path = '/Users/Dong/Desktop/test/dataset_aug/train_png'         # 图像路径
img_xml = '/Users/Dong/Desktop/test/dataset_aug/show_xml'           # 显示标注框保存该文件的路径
for name in os.listdir(xml_path):
    image_name = os.path.join(img_path, name.split('.')[0] + '.jpg')

    if os.path.exists(image_name):
        # 打开xml文档
        tree = ET.parse(os.path.join(xml_path,name))
        img = cv2.imread(image_name)
        box_thickness = int((img.shape[0] + img.shape[1])/600)
        if box_thickness < 1:   # 标注框的一个参数。本人图像大小不一致，在不同大小的图像上展示不同粗细的bbox
            box_thickness = 1

        if img.shape[1]<1000:
            text_size = 1       # 显示标注类别的参数。字体大小。这些不是重点。不想要可以删掉。
            text_thickness = 1
        elif img.shape[1]<2500:
            text_size = 2
            text_thickness = 2
        elif img.shape[1]<4000:
            text_size = 3
            text_thickness = 3
        else:
            text_size = 4
            text_thickness = 4
        font = cv2.FONT_HERSHEY_SIMPLEX

        # 得到文档元素对象
        root = tree.getroot()
        allObjects = root.findall('object')
        for i in range(len(allObjects)):    # 遍历xml标签，画框并显示类别。
            object = allObjects[i]
            objectName = object.find('name').text

            if objectName == 'blossom_end_rot':     # 把引号里的内容更改为自己的类别即可。
                xmin = int(object.find('bndbox').find('xmin').text)
                ymin = int(object.find('bndbox').find('ymin').text)
                xmax = int(object.find('bndbox').find('xmax').text)
                ymax = int(object.find('bndbox').find('ymax').text)
                cv2.putText(img, objectName, (xmin, ymax), font, text_size,
                            (255,255,0), text_thickness)
                cv2.rectangle(img,(xmin, ymin),(xmax, ymax),[255,255,0],box_thickness)

            if objectName == 'graymold':
                xmin = int(object.find('bndbox').find('xmin').text)
                ymin = int(object.find('bndbox').find('ymin').text)
                xmax = int(object.find('bndbox').find('xmax').text)
                ymax = int(object.find('bndbox').find('ymax').text)
                cv2.putText(img, objectName, (xmin, ymax), font, text_size,
                            (255,0,255), text_thickness)
                cv2.rectangle(img,(xmin, ymin),(xmax, ymax),[255,0,255],box_thickness)

            if objectName == 'powdery_mildew':
                xmin = int(object.find('bndbox').find('xmin').text)
                ymin = int(object.find('bndbox').find('ymin').text)
                xmax = int(object.find('bndbox').find('xmax').text)
                ymax = int(object.find('bndbox').find('ymax').text)
                cv2.putText(img, objectName, (xmin, ymax), font, text_size,
                            (0,255,255), text_thickness)
                cv2.rectangle(img,(xmin, ymin),(xmax, ymax),[0,255,255],box_thickness)

            if objectName == 'spider_mite':
                xmin = int(object.find('bndbox').find('xmin').text)
                ymin = int(object.find('bndbox').find('ymin').text)
                xmax = int(object.find('bndbox').find('xmax').text)
                ymax = int(object.find('bndbox').find('ymax').text)
                cv2.putText(img, objectName, (xmin, ymax), font, text_size,
                            (255,0,0), text_thickness)
                cv2.rectangle(img,(xmin, ymin),(xmax, ymax),[255,0,0],box_thickness)

            if objectName == 'spotting_disease':
                xmin = int(object.find('bndbox').find('xmin').text)
                ymin = int(object.find('bndbox').find('ymin').text)
                xmax = int(object.find('bndbox').find('xmax').text)
                ymax = int(object.find('bndbox').find('ymax').text)
                cv2.putText(img, objectName, (xmin, ymax), font, text_size,
                            (0,0,255), text_thickness)
                cv2.rectangle(img,(xmin, ymin),(xmax, ymax),[0,0,255],box_thickness)

            if objectName not in ['blossom_end_rot', 'graymold', 'powdery_mildew', 'spider_mite', 'spotting_disease']:
                xmin = int(object.find('bndbox').find('xmin').text)
                ymin = int(object.find('bndbox').find('ymin').text)
                xmax = int(object.find('bndbox').find('xmax').text)
                ymax = int(object.find('bndbox').find('ymax').text)
                cv2.putText(img, objectName, (xmin, ymax), font, text_size,
                            (0, 0, 255), text_thickness)
                cv2.rectangle(img, (xmin, ymin), (xmax, ymax), [0, 0, 0], box_thickness)
                print('objectName not in these labels. It is :', objectName)

            '''
            if objectName == 'angular_leafspot':
                xmin = int(object.find('bndbox').find('xmin').text)
                ymin = int(object.find('bndbox').find('ymin').text)
                xmax = int(object.find('bndbox').find('xmax').text)
                ymax = int(object.find('bndbox').find('ymax').text)
                cv2.putText(img, objectName, (xmin, ymax), font, text_size,
                            (255,255,0), text_thickness)
                cv2.rectangle(img,(xmin, ymin),(xmax, ymax),[255,255,0],box_thickness)

            if objectName == 'anthracnose_fruit_rot':
                xmin = int(object.find('bndbox').find('xmin').text)
                ymin = int(object.find('bndbox').find('ymin').text)
                xmax = int(object.find('bndbox').find('xmax').text)
                ymax = int(object.find('bndbox').find('ymax').text)
                cv2.putText(img, objectName, (xmin, ymax), font, text_size,
                            (255,0,255), text_thickness)
                cv2.rectangle(img,(xmin, ymin),(xmax, ymax),[255,0,255],box_thickness)

            if objectName == 'anthracnose_runner':
                xmin = int(object.find('bndbox').find('xmin').text)
                ymin = int(object.find('bndbox').find('ymin').text)
                xmax = int(object.find('bndbox').find('xmax').text)
                ymax = int(object.find('bndbox').find('ymax').text)
                cv2.putText(img, objectName, (xmin, ymax), font, text_size,
                            (0,255,255), text_thickness)
                cv2.rectangle(img,(xmin, ymin),(xmax, ymax),[0,255,255],box_thickness)

            if objectName == 'blossom_blight':
                xmin = int(object.find('bndbox').find('xmin').text)
                ymin = int(object.find('bndbox').find('ymin').text)
                xmax = int(object.find('bndbox').find('xmax').text)
                ymax = int(object.find('bndbox').find('ymax').text)
                cv2.putText(img, objectName, (xmin, ymax), font, text_size,
                            (255,0,0), text_thickness)
                cv2.rectangle(img,(xmin, ymin),(xmax, ymax),[255,0,0],box_thickness)

            if objectName == 'gray_mold':
                xmin = int(object.find('bndbox').find('xmin').text)
                ymin = int(object.find('bndbox').find('ymin').text)
                xmax = int(object.find('bndbox').find('xmax').text)
                ymax = int(object.find('bndbox').find('ymax').text)
                cv2.putText(img, objectName, (xmin, ymax), font, text_size,
                            (0,0,255), text_thickness)
                cv2.rectangle(img,(xmin, ymin),(xmax, ymax),[0,0,255],box_thickness)

            if objectName == 'leaf_spot':
                xmin = int(object.find('bndbox').find('xmin').text)
                ymin = int(object.find('bndbox').find('ymin').text)
                xmax = int(object.find('bndbox').find('xmax').text)
                ymax = int(object.find('bndbox').find('ymax').text)
                cv2.putText(img, objectName, (xmin, ymax), font, text_size,
                            (255,255,255), text_thickness)
                cv2.rectangle(img,(xmin, ymin),(xmax, ymax),[0,255,0],box_thickness)

            if objectName == 'powdery_mildew_fruit':
                xmin = int(object.find('bndbox').find('xmin').text)
                ymin = int(object.find('bndbox').find('ymin').text)
                xmax = int(object.find('bndbox').find('xmax').text)
                ymax = int(object.find('bndbox').find('ymax').text)
                cv2.putText(img, objectName, (xmin, ymax), font, text_size,
                            (0,255,0), text_thickness)
                cv2.rectangle(img,(xmin, ymin),(xmax, ymax),[0,0,0],box_thickness)

            if objectName == 'powdery_mildew_leaf':
                xmin = int(object.find('bndbox').find('xmin').text)
                ymin = int(object.find('bndbox').find('ymin').text)
                xmax = int(object.find('bndbox').find('xmax').text)
                ymax = int(object.find('bndbox').find('ymax').text)
                cv2.putText(img, objectName, (xmin, ymax), font, text_size,
                            (0,0,0), text_thickness)
                cv2.rectangle(img,(xmin, ymin),(xmax, ymax),[255,255,255],box_thickness)

            if objectName not in ['anthracnose_runner', 'gray_mold', 'blossom_blight',
                                  'leaf_spot', 'powdery_mildew_fruit', 'powdery_mildew_leaf',
                                  'anthracnose_fruit_rot','angular_leafspot']:
                xmin = int(object.find('bndbox').find('xmin').text)
                ymin = int(object.find('bndbox').find('ymin').text)
                xmax = int(object.find('bndbox').find('xmax').text)
                ymax = int(object.find('bndbox').find('ymax').text)
                cv2.putText(img, objectName, (xmin, ymax), font, text_size,
                            (0, 0, 255), text_thickness)
                cv2.rectangle(img, (xmin, ymin), (xmax, ymax), [64, 128, 256], box_thickness)
                print('objectName not in these labels. It is :', objectName)
            '''

        #cv2.imshow(name, img)
        #cv2.waitKey(1000)
        #cv2.destroyAllWindows()
        name = name.replace('xml', 'jpg')
        img_save_path = os.path.join(img_xml, name)
        cv2.imwrite(img_save_path, img)


    else:
        image_name = os.path.join(img_path, name.split('.')[0] + '.png')
        if os.path.exists(image_name):
            # 打开xml文档
            tree = ET.parse(os.path.join(xml_path, name))
            img = cv2.imread(image_name)
            box_thickness = int((img.shape[0] + img.shape[1]) / 600)
            if box_thickness < 1:
                box_thickness = 1

            if img.shape[1] < 1000:
                text_size = 1
                text_thickness = 1
            elif img.shape[1] < 2500:
                text_size = 2
                text_thickness = 2
            elif img.shape[1] < 4000:
                text_size = 3
                text_thickness = 3
            else:
                text_size = 4
                text_thickness = 4
            font = cv2.FONT_HERSHEY_SIMPLEX

            # 得到文档元素对象
            root = tree.getroot()
            allObjects = root.findall('object')
            for i in range(len(allObjects)):
                object = allObjects[i]
                objectName = object.find('name').text

                if objectName == 'blossom_end_rot':
                    xmin = int(object.find('bndbox').find('xmin').text)
                    ymin = int(object.find('bndbox').find('ymin').text)
                    xmax = int(object.find('bndbox').find('xmax').text)
                    ymax = int(object.find('bndbox').find('ymax').text)
                    cv2.putText(img, objectName, (xmin, ymax), font, text_size,
                                (255, 255, 0), text_thickness)
                    cv2.rectangle(img, (xmin, ymin), (xmax, ymax), [255, 255, 0], box_thickness)

                if objectName == 'graymold':
                    xmin = int(object.find('bndbox').find('xmin').text)
                    ymin = int(object.find('bndbox').find('ymin').text)
                    xmax = int(object.find('bndbox').find('xmax').text)
                    ymax = int(object.find('bndbox').find('ymax').text)
                    cv2.putText(img, objectName, (xmin, ymax), font, text_size,
                                (255, 0, 255), text_thickness)
                    cv2.rectangle(img, (xmin, ymin), (xmax, ymax), [255, 0, 255], box_thickness)

                if objectName == 'powdery_mildew':
                    xmin = int(object.find('bndbox').find('xmin').text)
                    ymin = int(object.find('bndbox').find('ymin').text)
                    xmax = int(object.find('bndbox').find('xmax').text)
                    ymax = int(object.find('bndbox').find('ymax').text)
                    cv2.putText(img, objectName, (xmin, ymax), font, text_size,
                                (0, 255, 255), text_thickness)
                    cv2.rectangle(img, (xmin, ymin), (xmax, ymax), [0, 255, 255], box_thickness)

                if objectName == 'spider_mite':
                    xmin = int(object.find('bndbox').find('xmin').text)
                    ymin = int(object.find('bndbox').find('ymin').text)
                    xmax = int(object.find('bndbox').find('xmax').text)
                    ymax = int(object.find('bndbox').find('ymax').text)
                    cv2.putText(img, objectName, (xmin, ymax), font, text_size,
                                (255, 0, 0), text_thickness)
                    cv2.rectangle(img, (xmin, ymin), (xmax, ymax), [255, 0, 0], box_thickness)

                if objectName == 'spotting_disease':
                    xmin = int(object.find('bndbox').find('xmin').text)
                    ymin = int(object.find('bndbox').find('ymin').text)
                    xmax = int(object.find('bndbox').find('xmax').text)
                    ymax = int(object.find('bndbox').find('ymax').text)
                    cv2.putText(img, objectName, (xmin, ymax), font, text_size,
                                (0, 0, 255), text_thickness)
                    cv2.rectangle(img, (xmin, ymin), (xmax, ymax), [0, 0, 255], box_thickness)

                if objectName not in ['blossom_end_rot', 'graymold', 'powdery_mildew', 'spider_mite',
                                      'spotting_disease']:
                    xmin = int(object.find('bndbox').find('xmin').text)
                    ymin = int(object.find('bndbox').find('ymin').text)
                    xmax = int(object.find('bndbox').find('xmax').text)
                    ymax = int(object.find('bndbox').find('ymax').text)
                    cv2.putText(img, objectName, (xmin, ymax), font, text_size,
                                (0, 0, 255), text_thickness)
                    cv2.rectangle(img, (xmin, ymin), (xmax, ymax), [0, 0, 0], box_thickness)
                    print('objectName not in these labels. It is :', objectName)

            name = name.replace('xml', 'jpg')
            img_save_path = os.path.join(img_xml, name)
            cv2.imwrite(img_save_path, img)
        else:
            print('img:{} does not exist.'.format(image_name))