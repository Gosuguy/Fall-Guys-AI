import cv2
import numpy as np
import os

listing = os.listdir("C:/Users/Juna/Desktop/AI/Personal Projects/Fall-Guys/data/Tundra Run/")


for j in range(int(len(listing) / 2)):

    data = np.load("C:/Users/Juna/Desktop/AI/Personal Projects/Fall-Guys/data/Tundra Run/training_data" + str(j+1) + ".npy", allow_pickle=True)
    targets = np.load("C:/Users/Juna/Desktop/AI/Personal Projects/Fall-Guys/data/Tundra Run/target_data" + str(j+1) + ".npy", allow_pickle=True)

    print(f'Image Data Shape: {data.shape}')
    print(f'targets Shape: {targets.shape}')

    # Lets see how many of each type of move we have.
    # unique_elements, counts = np.unique(targets, return_counts=True)
    # print(np.asarray((unique_elements, counts)))

    # Store both data and targets in a list.
    # We may want to shuffle down the road.

    holder_list = []
    for i, image in enumerate(data):
        holder_list.append([data[i], targets[i]])

    count_nothing = 0
    count_up = 0
    count_left = 0
    count_right = 0
    count_down = 0
    count_jump = 0
    count_dive = 0
    count = 0

    for data in holder_list: # Version 3 and 4, multi-class classification
        # print(data[1], len(data[1]) > 0) 
        inputs = []
        for input_val in data[1]:  
            if len(data[1]) > 0:
                if input_val == ' ':
                    inputs.append('Jump')
                if input_val == 'W':
                    inputs.append('Up')
                if input_val == 'A':
                    inputs.append('Left')
                if input_val == 'D':
                    inputs.append('Right')
                if input_val == 'S':
                    inputs.append('Down')
                if input_val == 'E':
                    inputs.append('Dive')
                if input_val == '':
                    inputs.append('Nothing')
        count += 1
        folder_name = ' '.join(inputs)
        isdir = os.path.isdir(f"E:/Bidio/FallGuys/{folder_name}")
        # print ("FILE IS: ", f"E:/Bidio/FallGuys/{folder_name}/{j}-{count}.png")
        # print("DIR EXISTS: ", isdir)
        if isdir == False:
            print("CREATING FILE: ", f"E:/Bidio/FallGuys/{folder_name}/{j}-{count}.png")
            os.mkdir(f"E:/Bidio/FallGuys/{folder_name}")
        cv2.imwrite(f"E:/Bidio/FallGuys/{folder_name}/{j}-{count}.png", data[0]) # j is game number, count is pic count so far for this course

    # for data in holder_list: # Version 1 and 2, single-class classification
    #     # print(data[1], len(data[1]) > 0) 

    #     if len(data[1]) > 0:
    #         if data[1][0] == ' ' or (len(data[1]) == 2 and data[1][1] == ' ') or (len(data[1]) == 3 and data[1][2] == ' '):
    #             count_jump += 1
    #             cv2.imwrite(f"E:/Bidio/FallGuys/Jump/j{j}-{count_jump}.png", data[0])             
    #         elif data[1][0] == 'W':
    #             count_up += 1
    #             cv2.imwrite(f"E:/Bidio/FallGuys/Up/u{j}-{count_up}.png", data[0]) 
    #         elif data[1][0] == 'A':
    #             count_left += 1
    #             cv2.imwrite(f"E:/Bidio/FallGuys/Left/l{j}-{count_left}.png", data[0]) 
    #         elif data[1][0] == 'D':
    #             count_right += 1
    #             cv2.imwrite(f"E:/Bidio/FallGuys/Right/r{j}-{count_right}.png", data[0]) 
    #         elif data[1][0] == 'S':
    #             count_down += 1
    #             cv2.imwrite(f"E:/Bidio/FallGuys/Down/d{j}-{count_down}.png", data[0])     
    #         elif data[1][0] == 'E' or (len(data[1]) == 2 and data[1][1] == 'E') or (len(data[1]) == 3 and data[1][2] == 'E'):
    #             count_dive += 1
    #             cv2.imwrite(f"E:/Bidio/FallGuys/Dive/di{j}-{count_dive}.png", data[0]) 
    #         elif data[1][0] == '':
    #             count_nothing += 1
    #             cv2.imwrite(f"E:/Bidio/FallGuys/Nothing/n{j}-{count_nothing}.png", data[0]) 