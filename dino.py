import pyautogui
from PIL import Image, ImageGrab
import time

def presskey(key):
    pyautogui.keyDown(key)

def iscolide(data):
    # for i in range(235,255):#width
    #     for j in range(280,355):#height
    #         if data[i,j]< 90:
    #             presskey('down')
    #             return True

    for i in range(255,305):#width
        for j in range(375,455):#height
            if data[i,j]< 90:
                presskey('up')
                return True
    return False


if __name__ == "__main__":
    time.sleep(1)
    presskey('up')
    while True:
        image=ImageGrab.grab().convert('L')
        data = image.load()
        iscolide(data)

        # #cactus
        # for i in range(205,305):#width
        #     for j in range(375,455):#height
        #         data[i,j]=0

        # # birds
        #     for j in range(280,355):#height
        #         for i in range(235,255):#width
        #             data[i,j]=70
            
        # image.show()
        # break