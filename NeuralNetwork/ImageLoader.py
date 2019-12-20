from PIL import Image
import os

def loadImage():    
    threshold=137
    imagedir='image'  #存放图片的文件夹
    IMG_EXTENSIONS = ['.jpg', '.JPG', '.jpeg', '.JPEG',     #图片后缀名
    '.png', '.PNG', '.bmp', '.BMP',]
    files= os.listdir(imagedir)
    images=[]
    bwimgs=[]
    for file in files: #遍历文件夹
        if not os.path.isdir(file):             #是否为文件夹
            filename = os.path.join(imagedir, file)
            if any(filename.endswith(extension) for extension in IMG_EXTENSIONS):   #是否为图像
                img=Image.open(filename)
                images.append(img)
    
    for im in images:
        im = im.convert("L")  # 转换为灰度图像
        im = im.point(lambda x: 255 if x > threshold else 0) #代表数字的像素值置0，黑色
        im = im.convert('1') # 黑白二值图像
        bwimgs.append(im)
    digits8_8=to_8_8(bwimgs)

def to_8_8(images):
    digits8_8=[]
    for im in images:
        im = im.convert("L")
        w, h = im.size
        xrow = []
        ycol = []
        for i in range(w):
            for j in range(h):
                pixel = im.getpixel((i, j))  # 返回某一点的像素值
                if (pixel < 1):
                    xrow.append(i)
                    ycol.append(j)
        xLength = max(xrow) - min(xrow) + 1
        yLength = max(ycol) - min(ycol) + 1  # 得到字符的长度宽度
        box = (min(xrow), min(ycol), max(xrow) + 1, max(ycol) + 1)
        t = im.crop(box).copy()  # 从当前的图像中返回一个矩形区域的拷贝。变量box是一个四元组，定义了左、上、右和下的像素坐标
                
        xStart = (8 - xLength) // 2
        yStart = (8 - yLength) // 2  # 居中
        bg = Image.new('RGB', (8, 8), 'white')
        bg.paste(t, (xStart, yStart))  # 将一张图粘贴到另一张图像上
        digits8_8.append(bg)
    return digits8_8