from PIL import Image


def blend_two_images():
    img1 = Image.open("/Users/Dong/Desktop/med_phys_latex_template 2/case8-1.jpg")
    img1 = img1.convert('RGBA')
    img2 = Image.open("/Users/Dong/Desktop/med_phys_latex_template 2/case8-5.jpg")
    img2 = img2.convert('RGBA')

    img = Image.blend(img1, img2, 0.5)
    r, g, b, a = img.split()
    img = Image.merge("RGB", (r, g, b))
    # img.save("/Users/Dong/Desktop/case8-1-5.jpg")
    return


def blend_two_images2():
    img1 = Image.open("/Users/Dong/Desktop/med_phys_latex_template 2/case8-1.jpg")
    img1 = img1.convert('RGBA')
    img2 = Image.open("/Users/Dong/Desktop/med_phys_latex_template 2/case8-2.jpg")
    img2 = img2.convert('RGBA')

    r, g, b, alpha = img2.split()
    alpha = alpha.point(lambda i: i > 0 and 204)

    img = Image.composite(img2, img1, alpha)
    img.show()
    img.save("blend2.png")
    return


blend_two_images()



