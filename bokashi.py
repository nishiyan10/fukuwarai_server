from PIL import Image
import cv2
import numpy as np

img = cv2.imread('ketugou.jpg')

IMG_PIXEL = 300
IMG_LINE = 300
RGB_CH = 3

BORDER_ODEKO = 150
BORDER_HANA = 210

BORDER_SIZE = 4

BORDER_CUT = 0

IMG_ORI =  [[[0 for pixel in range(IMG_PIXEL)] for line in range(IMG_LINE)] for ch in range(RGB_CH)]
#IMG_ORI[z][x][y]  z : range 3 RGB ch 0=R,1=G,2=B
for y in range(IMG_LINE):
    for x in range(IMG_PIXEL):
        pixelValue = img[y, x]
        #print('pixelValue = ' + str(pixelValue))
        IMG_ORI[0][y][x] = pixelValue[2] #赤 縦横
        IMG_ORI[1][y][x] = pixelValue[1] #緑
        IMG_ORI[2][y][x] = pixelValue[0] #青


print('-----------------------------------------')


for k in range(RGB_CH):
    for y in range(9):
        y = y + 146
        for x in range(IMG_PIXEL):
            a = BORDER_ODEKO - BORDER_SIZE
            b = IMG_ORI[k][BORDER_ODEKO - (BORDER_SIZE + 1)][x]
            c = BORDER_ODEKO + BORDER_SIZE
            d = IMG_ORI[k][BORDER_ODEKO + BORDER_SIZE][x]
            
            
            m = (int(b) - int(d)) / (a - c)
            
            p = int(b) - (m * a)
            
    #        print("切片" + str(p))
    #        print("変化量" + str(m))
    #        
    #        
    #        #print((m * y) + p)
    
            IMG_ORI[k][y][x] = (m * y) + p
            
    #       print(IMG_ORI[k][y][x])
    
for k in range(RGB_CH):
    for y in range(9):
        y = y + 206
        for x in range(IMG_PIXEL):
            a = BORDER_HANA - BORDER_SIZE
            b = IMG_ORI[k][BORDER_HANA - (BORDER_SIZE + 1)][x]
            c = BORDER_HANA + BORDER_SIZE
            d = IMG_ORI[k][BORDER_HANA + BORDER_SIZE][x]
            
            
            m = (int(b) - int(d)) / (a - c)
            
            p = int(b) - (m * a)
            
    #        print("切片" + str(p))
    #        print("変化量" + str(m))
    #        
    #        
    #        #print((m * y) + p)
    
            IMG_ORI[k][y][x] = (m * y) + p
            
    #       print(IMG_ORI[k][y][x])
            

img2 = Image.new("RGB",(IMG_PIXEL,IMG_LINE))


for y in range(IMG_LINE):
    for x in range(IMG_PIXEL):
        img2.putpixel((x,y),(int(IMG_ORI[0][y][x]) , int(IMG_ORI[1][y][x]) , int(IMG_ORI[2][y][x])))
        
        
img2.save("ketugou_bokashi.jpg")
