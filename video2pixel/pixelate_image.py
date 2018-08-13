# coding=utf-8

from PIL import Image
import os
import subprocess

# The code of pixel()function is copyed from https://github.com/sahildua2305/pixelate_image.py.git
# pixel()函数的代码来自https://github.com/sahildua2305/pixelate_image.py.git
def pixel(jpg):
    jpg = str(jpg)
    image = Image.open(jpg)
    x = 100
    y = 100
    w, h = image.size
    x = w / 3
    y = h / 3
    sqx = int(w / x)
    sqy = int(h / y)
    sqx2 = int(sqx // 2)
    sqy2 = int(sqy // 2)
    #print(w, h)
    backgroundColor = (255,) * 3

    pix = image.load()

    for x in range(0, w - sqx, sqx):
        for y in range(0, h - sqy, sqy):
            R, G, B = image.getpixel((x + sqx2, y + sqy2))
            # print R,G,B

            for p in range(x, x + sqx):
                for q in range(y, y + sqy):
                    # pix[p,q] = (R,G,B)
                    if R > 90 and G > 90 and B > 90:
                        # LED OFF
                        pix[p, q] = (255, 255, 255)
                    else:
                        # LED ON
                        pix[p, q] = (0, 0, 0)

    pixel = image.load()
    for i in range(0, w, sqx):
        for j in range(0, h, sqy):
            for r in range(sqx):
                # print i,j,r
                if i + r < w and j + r < h:
                    pixel[i + r, j] = backgroundColor
                    pixel[i, j + r] = backgroundColor
    jpg = jpg
    image.save(jpg)
    

def pic2pix(path='./img_out'):
    print('converting pictures to pixels 图像像素化处理中……')
    path = str(path)
    files = os.listdir(path)
    for file in files:
        file = path + '/' + file
        pixel(file)

def v2p(inFile):
    #inFile为需要转化的视频
    #ffmpeg = 填入本地ffmepg.exe的位置
    #ffmpeg = r'D:\ffmpeg-4.0.2-win64-static\bin\ffmpeg.exe'
    print('converting video to pictures 视频转图像ing')
    imgOut = './img_out/img_out_%03d.jpeg'
    action = [ffmpeg, '-i', inFile,'-r','1',imgOut]
    subprocess.call(action,shell = True)
    #subprocess.call('ffmpeg','-i','weisuoyuwei.mp4','-r','1','img_out/img_out_%%03d.jpeg')

def p2v ():
    print('this part may take time, be patient. 正在合成视频，请稍后')
    #strcmd = "ffmpeg -i " + path + " -r  -f image2 " + './img_out/img' + "%06d.jpg"
    imgOut = './img_out/img_out_%03d.jpeg'
    action = [ffmpeg, '-r','5', '-i',imgOut,'outPut.mp4']
    #f = 'ffmpeg -f image2 -i ./img_out/img_out_%03d.jpeg outPut.mp4'
    subprocess.call(action)
    print('Done, now check outPut.mp4 完成,请查看outPut.mp4文件 :)')

def converter(inFile):
    v2p(inFile)
    pic2pix()
    p2v()


ffmpeg = str(input('input the path of ffmpeg on your device 填入本地ffmepg的位置'))
inFile =  str(input('input the video you want to convert 输入你想要转换的视频: '))
converter(inFile)

