import numpy as np
import cv2
import time
import os

from utils.grabscreen import grab_screen
from utils.getkeys import key_check


file_name = "C:/Users/Juna/Desktop/Machine Learning/Personal Projects/Fall-Guys/data/training_data.npy"
file_name2 = "C:/Users/Juna/Desktop/Machine Learning/Personal Projects/Fall-Guys/data/target_data.npy"


def get_data():

    if os.path.isfile(file_name):
        print('File exists, loading previous data!')
        image_data = list(np.load(file_name, allow_pickle=True))
        targets = list(np.load(file_name2, allow_pickle=True))
    else:
        print('File does not exist, starting fresh!')
        image_data = []
        targets = []
    return image_data, targets


def save_data(image_data, targets):
    np.save(file_name, image_data)
    np.save(file_name2, targets)


image_data, targets = get_data()
while True:
    keys = key_check()
    print("waiting press B to start")
    if keys[0] == "B":
        print("Starting")
        break


count = 0
while True:
    count +=1
    last_time = time.time()
    image = grab_screen(region=(50, 100, 1279, 569)) # left, top, x2, y2 = region. (50, 100, 799, 449) for 800 x 600. 749 x 399. I have 1280 x 720. so 1229 x 519.
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # simplify image

    image = cv2.Canny(image, threshold1=119, threshold2=250)

    image = cv2.resize(image, (224, 224)) 

    # Debug line to show image
    cv2.imshow("AI Peak", image)
    cv2.waitKey(1)

    # Convert to numpy array
    image = np.array(image) # store img as array
    image_data.append(image) # append image to list

    keys = key_check()
    targets.append(keys) # append key to list
    print("Pressing Key: ", keys)
    if keys[0] == "H":
        break

    print('loop took {} seconds'.format(time.time()-last_time))

save_data(image_data, targets)
