import random
import time

from utils.getkeys import key_check
import pydirectinput
import keyboard
import time
import cv2
import fastai
from utils.grabscreen import grab_screen
from utils.directkeys import PressKey, ReleaseKey, W, D, A
from fastai.vision.all import *

# def label_func(x): return x.parent.name
def get_y(r): return parent_label(r).split(' ') # For pickle file to load correctly
path = "../data/"

use_cuda = torch.cuda.is_available()
print("Using Cuda: ", use_cuda)
# print("Cuda version: ", torch.version.cuda)
# a=torch.cuda.FloatTensor()

# learn_inf = load_learner(path + "General.pkl")

# learn_inf = load_learner(path + "BigFans.pkl") 
# learn_inf = load_learner(path + "DizzyHeights.pkl") 
# learn_inf = load_learner(path + "DoorDash.pkl") 
# learn_inf = load_learner(path + "FullTilt.pkl") 
# learn_inf = load_learner(path + "GateCrash.pkl") 
# learn_inf = load_learner(path + "HitParade.pkl") 
# learn_inf = load_learner(path + "KnightFever.pkl") 
# learn_inf = load_learner(path + "LilyLeapers.pkl") 
# learn_inf = load_learner(path + "PartyPromenade.pkl") 
# learn_inf = load_learner(path + "RollOn.pkl") 
# learn_inf = load_learner(path + "SeeSaw.pkl") 
# learn_inf = load_learner(path + "SkylineStumble.pkl") 
# learn_inf = load_learner(path + "TheWhirlygig.pkl") 
# learn_inf = load_learner(path + "TreetopTumble.pkl") 
# learn_inf = load_learner(path + "TundraRun.pkl") 

# learn_inf = load_learner(path + "BigFansMulti.pkl", cpu=not use_cuda) 
# learn_inf = load_learner(path + "DizzyHeightwdsMulti.pkl", cpu=not use_cuda) 
# learn_inf = load_learner(path + "DoorDashMulti.pkl", cpu=not use_cuda) 
# learn_inf = load_learner(path + "FullTiltMulti.pkl", cpu=not use_cuda) 
# learn_inf = load_learner(path + "GateCrashMulti.pkl", cpu=not use_cuda) 
# learn_inf = load_learner(path + "HitParadeMulti.pkl", cpu=not use_cuda) 
# learn_inf = load_learner(path + "KnightFeverMulti.pkl", cpu=not use_cuda) 
# learn_inf = load_learner(path + "LilyLeapersMulti.pkl", cpu=not use_cuda) 
# learn_inf = load_learner(path + "PartyPromenadeMulti.pkl", cpu=not use_cuda) 
# learn_inf = load_learner(path + "RollOnMulti.pkl", cpu=not use_cuda) 
# learn_inf = load_learner(path + "SeeSawMulti.pkl", cpu=not use_cuda) 
# learn_inf = load_learner(path + "SkylineStumbleMulti.pkl", cpu=not use_cuda) 
# learn_inf = load_learner(path + "TheWhirlygigMulti.pkl", cpu=not use_cuda) 
# learn_inf = load_learner(path + "TreetopTumbleMulti.pkl", cpu=not use_cuda) 
# learn_inf = load_learner(path + "TundraRunMulti.pkl", cpu=not use_cuda) 

print("loaded learner")

# Sleep time after actions
sleepy = 0.0 # 0.1

# Wait for me to push B to start.
# keyboard.wait('b')
time.sleep(sleepy)
while True:
    # start_time = time.time()
    # print ("Start: ", time.time())
    image = grab_screen(region=(50, 100, 1279, 569))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.Canny(image, threshold1=200, threshold2=300)
    image = cv2.resize(image,(224,224))
    # print ("Processed Image: ", time.time())
    # cv2.imshow("Fall", image)
    # cv2.waitKey(1)
    # start_time = time.time()
    result = learn_inf.predict(image)
    # print ("Predicted: ", time.time())
    # print ("Tensor: ", result[2])
    keyboard.release("space")
    keyboard.release("e")
    keyboard.release("a")
    keyboard.release("d")
    keyboard.release("w")
    keyboard.release("s")
    # for action in result[0]:
    if result[2][2]>0.01:#action == "Jump":
        # print(f"JUMP! - {result[1]}")
        keyboard.press("space")
    if result[2][2]>0.2 and result[2][0]>0.001:#action == "Dive":
        # print(f"Dive! - {result[1]}")
        keyboard.press("e")
    if result[2][6]>0.2:#action == "Up":
        # print(f"Up! - {result[1]}")
        keyboard.press("w")
    if result[2][3]>0.2:#action == "Left":
        # print(f"LEFT! - {result[1]}")
        keyboard.press("a")
    if result[2][5]>0.2:#action == "Right":
        # print(f"Right! - {result[1]}")
        keyboard.press("d")
    if result[2][1]>0.1:#action == "Down":
        # print(f"Down! - {result[1]}")
        keyboard.press("s")

    # print ("Input Done: ", time.time())
    time.sleep(sleepy)
    # print ("End: ", time.time())

    # End simulation by hitting h
    # keys = key_check()
    # if keys == "h":
    #     break
