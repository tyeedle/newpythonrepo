import os
import time

def loadingBar(length : int,symbol : str,delay : int):
    bar = []
    percent = 0
    for i in range(length):
        percent += 1
        print(f'[{"".join(bar)}>] \n {round(percent / length * 100)}%')
        bar.append(symbol)
        
        time.sleep(delay)
        os.system('clear')

loadingBar(100, "=", 0.05)

def loadingBarV2(length : int ,symbol : str ,delay : int):
    bar = []
    percent = 0
    
    for i in range(length):
        bar.append("-")
    
    for i,v in enumerate(bar):
        percent += 1
        bar[i] = symbol
        
        print(f"[{''.join(bar)}] \n {round(percent / length * 100)}%")
        time.sleep(delay)
        os.system('clear')

loadingBarV2(100, "=", 0.05)