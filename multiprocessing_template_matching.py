import gc
import os
import cv2 as cv
import numpy
import pyautogui
from PIL import ImageGrab, Image
import numpy as np
import time
import multiprocessing
from multiprocessing import Event
import imutils

def something():
    while True:
        image_gray = np.array(cv.cvtColor(cv.imread(
            "/home/something/PycharmProjects/multiprocessing-template-matching/Screenshot from 2022-12-22 19-59-11.png"),
                                          cv.COLOR_RGB2GRAY))
        b = cv.cvtColor(np.array(ImageGrab.grab(bbox=(0, 0, 2560, 1440))), cv.COLOR_RGB2GRAY)
        h1, w1, = image_gray.shape[::-1]
        REGION = 796, 574, 1756, 973
        x, y, w, h = REGION
        result = cv.matchTemplate(
            image=b,
            templ=image_gray,
            method=cv.TM_CCORR_NORMED)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        # print(f'thread one max value:{max_val}')

        print(f'max value of thread one: {max_val}')
        if max_val >= 0.95:  # this was 0.79
            x1, y2 = (h1 / 2) + max_loc[0], (w1 / 2) + max_loc[1]
            try:
                pyautogui.moveTo(x=x1, y=y2)
                del result, min_val, max_val, min_loc, max_loc
                break
            except RuntimeError:
                pass



def something2():
    # checker1=z
    # print(processes[0])
    while True:
        image_gray = np.array(cv.cvtColor(cv.imread("/home/something/PycharmProjects/multiprocessing-template-matching/Screenshot from 2022-12-22 20-00-56.png"), cv.COLOR_RGB2GRAY))
        b = cv.cvtColor(np.array(ImageGrab.grab(bbox=(0, 0, 2560, 1440))), cv.COLOR_RGB2GRAY)
        h1, w1, = image_gray.shape[::-1]
        REGION = 796, 574, 1756, 973
        x, y, w, h = REGION
        result = cv.matchTemplate(
            image=b,
            templ=image_gray,
            method=cv.TM_CCORR_NORMED)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        # print(f'thread two max value:{max_val}')
        _FINISH = False
        print(f'something2 max value:{max_val}')
        if max_val >= 0.98:
            pyautogui.FAILSAFE=False
            # print('thread 2 found found the reject window')
            x1, y2 = (h1 / 2) + max_loc[0], (w1 / 2) + max_loc[1]
            try:
                pyautogui.moveTo(x=x1, y=y2)
                del result, min_val, max_val, min_loc, max_loc
                break
            except RuntimeError:
                pass
            del result, min_val, max_val, min_loc, max_loc
            break
        gc.collect()


def Phase1():
    while True:

        event = Event()
        t1 = multiprocessing.Process(target=something2, daemon=True)
        t2 = multiprocessing.Process(target=something, daemon=True)
        t1.start()
        t2.start()
        # For some odd reason adding this small 0.29 pauses causes the proper outcome. reducing the time any lower
        # results in program to fail
        time.sleep(0.29)
        print(f'checking if thread one is alive: {t1.is_alive()}\nchecking if thread two is alive: {t2.is_alive()}')
        # t2.join()
        # print(t1.is_alive())
        # print(t2.is_alive())
        #t1.join()
        #t2.join()
        t1.terminate()
        t2.terminate()

        try:
            if t2.is_alive() == False:
                if t1.is_alive() == True:
                    print('thread TWO found it,thread one was still running')
                    t1.terminate()

                    break
                print('thread TWO found it,thread one was still running')
                break
                # test1()
            if t2.is_alive() == True:
                if t1.is_alive() == False:
                    print('Thread ONE found it, thread two was still running')
                    #print(
                        #f'checking if thread one is alive: {t1.is_alive()}\nchecking if thread two is alive{t2.is_alive()}')
                    # print(t2.is_alive())
                    t2.terminate()
                    time.sleep(0.01)
                    print(t2.is_alive(), t1.is_alive())
                    print(f'checking if thread one is alive after termination: {t1.is_alive()}')
                    #test1()
                    break

                # t2.kill()
                # test2()
        except ValueError:
                pass
        gc.collect()

        # t1.join()
        # t1.terminate()

    # print(f'thread two status:{t2.is_alive()}')
    # print(f'thread one status:{t1.is_alive()}')
#Phase1()0,
def screen_shot():
    #1047,966 1633,1263
    ImageGrab.grab(bbox=(1040, 963, 1646, 1262)).save("/home/something/PycharmProjects"
                                                                 "/multiprocessing-template-matching/pyscreen"
                                                                 ".png")
    a = np.array(
        cv.cvtColor(cv.imread("/home/something/PycharmProjects/multiprocessing-template-matching/pyscreen.png"),
                    cv.COLOR_BGR2GRAY))
def testing():
    screen_shot()
    template_image = cv.imread('/home/something/PycharmProjects/multiprocessing-template-matching/pyscreen.png')

    # Convert the screenshot to a grayscale image that can be used with cv2.matchTemplate
    template_image_array = np.array(template_image)
    a = cv.cvtColor(template_image_array, cv.COLOR_RGB2GRAY)
    #screen_shot()

    while True:
        a = np.array(cv.cvtColor(cv.imread(
            '/home/something/PycharmProjects/multiprocessing-template-matching/pyscreen.png'), cv.COLOR_RGB2GRAY))
        screen = cv.cvtColor(np.array(ImageGrab.grab(bbox=(0, 0, 2560, 1440))), cv.COLOR_RGB2GRAY)
        start= time.time()
        for i in np.arange(0.0829 ,0.01,-0.001): # np.linspace(0.80,0.01,100): works just fine for this loop
            resized = cv.resize(a, None, fx=i, fy=i,interpolation=cv.TM_CCORR_NORMED)
            result = cv.matchTemplate(
                image=screen,
                templ=resized,
                method=cv.TM_CCORR_NORMED)
            min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
            _FINISH = False
            print(f'resized image template percentage probability:{max_val}\nScale down value is :{i}')
            #print(i)
            #cv.imshow('resized',resized)
            #cv.waitKey(10)
            if max_val >= 0.99 or max_val>= 0.96:
                pyautogui.FAILSAFE = False
                # print('thread 2 found found the reject window')
                h1, w1, = resized.shape[::-1]
                x1, y2 = (h1 / 2) + max_loc[0], (w1 / 2) + max_loc[1]
                try:
                    pyautogui.moveTo(x=x1, y=y2)
                    pyautogui.press('ctrl',presses=5)
                    end = time.time()
                    final = end - start
                    print(final)
                    del result, min_val, max_val, min_loc, max_loc
                    break
                except RuntimeError:
                    pass
                del result, min_val, max_val, min_loc, max_loc
                break
            if max_val <=0.93:
                #
                # h1, w1, = resized.shape[::-1]
                # x1, y2 = (h1 / 2) + max_loc[0], (w1 / 2) + max_loc[1]
                # pyautogui.moveTo(x=x1, y=y2,)
                # pyautogui.press('ctrl')
                end= time.time()
                final= end-start
                if final >=1:
                    print(final)
                    break
                #time.sleep(1)
        break

#testing()