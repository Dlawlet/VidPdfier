import datetime
import os
import random
import shutil
import numpy as np
import cv2
from glob import glob
from fpdf import FPDF

def create_dir(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError:
        print(f"ERROR: creating directoring with name {path}")

def remove_dir(path):
    try: 
        if  os.path.exists(path):
            shutil.rmtree(path)
    except OSError:
        print(f"ERROR: deleting directoring with name {path}")
             
def save_frame(video_path, save_dir, gap=1000, pp = 1):
    name = video_path.split("/")[-1].split(".")[0]
    save_path =  os.path.join(save_dir, name)
    create_dir(save_path)
    gap=int(gap)
    pdf = FPDF()

    cap =cv2.VideoCapture(video_path)
    idx = 0

    cperpage = 0
    perpage = int(pp)
    pdf.add_page()

    while True:
        ret, frame = cap.read()

        if ret == False:
            cap.release()
            break
        if idx % gap == 0:
            cv2.imwrite(f"{save_path}/{idx}.png", frame)
            if cperpage == perpage:
                pdf.add_page()
                cperpage = 0
            pdf.image(f"{save_path}/{idx}.png",10,cperpage*120+10,190,100)
            cperpage+=1
        
        idx += 1
    remove_dir(save_path)
    pdf.output(f"{name}_{random.randint(0,123345)}.pdf", "F")
