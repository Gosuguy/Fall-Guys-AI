import win32api as wapi
import time

keyList = ["\b"]
# for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789,.'$/\\":
for char in "ABDEHSW $/\\":
    keyList.append(char)

def key_check():
    keys = []
    for key in keyList:
        if wapi.GetAsyncKeyState(ord(key)):
            keys.append(key)
            # print("Keys Pressed: ", keys)
    if (len(keys) > 0):
        return keys
    else:
        return ['']
    # if 'H' in keys:
    #     return 'H'
    # elif 'B' in keys:
    #     return 'B'
    # elif 'W' in keys:
    #     return 'W'
    # elif 'A' in keys:
    #     return 'A'
    # elif 'D' in keys:
    #     return 'D'
    # elif 'S' in keys:
    #     return 'S'
    # elif ' ' in keys:
    #     return ' '
    # elif 'E' in keys:
    #     return 'E'
    # else:
    #     return ''
