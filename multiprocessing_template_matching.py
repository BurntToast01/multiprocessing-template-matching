import gc
import os
import cv2 as cv
import pyautogui
from PIL import ImageGrab, Image
import numpy as np
import time
import multiprocessing
from multiprocessing import Event

def something():
    while True:
        image_gray = np.array(cv.cvtColor(cv.imread(
            "/run/media/marcos/8d82f6aa-2fc2-4eb7-ba62-e714d909f394/Old files/PycharmProjects/REDLIGHT_automation/Youtube.png"),
                                          cv.COLOR_RGB2GRAY))
        # a = np.array(ImageGrab.grab(bbox=(0, 0, 2560, 1440)))
        b = cv.cvtColor(np.array(ImageGrab.grab(bbox=(0, 0, 2560, 1440))), cv.COLOR_RGB2GRAY)
        h1, w1, = image_gray.shape[::-1]
        REGION = 796, 574, 1756, 973
        x, y, w, h = REGION
        result = cv.matchTemplate(
            image=b,
            templ=image_gray,
            method=cv.TM_CCORR_NORMED)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        # print('thread 1', max_val, )
        # cv.imshow('b', b)
        # print(f'thread one max value:{max_val}')
        while not event:
            break
        print(f'max value of thread one: {max_val}')
        if max_val >= 0.95:  # this was 0.79

            x1, y2 = (h1 / 2) + max_loc[0], (w1 / 2) + max_loc[1]
            try:
                pyautogui.moveTo(x=x1, y=y2)
                del result, min_val, max_val, min_loc, max_loc
                event.set()
                os.kill(t2, __signal=(exit()))

                break
            except RuntimeError:
                pass
            break

        event.set()


def something2():
    # checker1=z
    # print(processes[0])

    while True:
        image_gray = np.array(cv.cvtColor(cv.imread("/home/marcos/Pictures/reject_window.png"), cv.COLOR_RGB2GRAY))
        # a = np.array(ImageGrab.grab(bbox=(0, 0, 2560, 1440)))
        b = cv.cvtColor(np.array(ImageGrab.grab(bbox=(0, 0, 2560, 1440))), cv.COLOR_RGB2GRAY)
        h1, w1, = image_gray.shape[::-1]
        REGION = 796, 574, 1756, 973
        x, y, w, h = REGION
        result = cv.matchTemplate(
            image=b,
            templ=image_gray,
            method=cv.TM_CCORR_NORMED)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        # print('thread 2',max_val,)
        # del result

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
            # return var
            #test1()
            event.set()
            #t1.kill()

            os.kill(t1, exit())
            # exit()

            break
        if max_val <= 0.97:
            break


        # gc.collect()



if __name__ == "__main__":

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