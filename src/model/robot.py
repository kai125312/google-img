# ディレクトリからjsonを削除するプログラム
# 新規のものをoutputに吐き出す
import os
import glob
import shutil

import time

from src.vision import vision

ai = vision.Ai_hello()

class Googlerobot():
    def hello(self):
        ai.start()

    def img_move(self):
        INPUT_DIR = "./input"
        OUTPUT_DIR = "./output"
        a = os.listdir(INPUT_DIR)
        input_dir = os.listdir(f"./input/{a[0]}")
        #ディレクトリの作成
        timestamp = time.strftime('%Y%m%d%H%M%S')
        output_dir = f'{OUTPUT_DIR}/{timestamp}_takeout'
        os.mkdir(output_dir)
        kai = 0
        for dir in input_dir:
            img_path = f'{INPUT_DIR}/{a[0]}/{dir}'
            if os.path.isdir(img_path):
                copy_dir = f'{output_dir}/{dir}'
                os.mkdir(copy_dir)
                files = glob.glob(f"{img_path}/*")  
                for file in files:
                    fname = os.path.basename(file)
                    if not fname.endswith('.json'):
                        if not fname.endswith('.heic'):
                            shutil.copyfile(file, f'{copy_dir}/{fname}')
                            kai += 1
        ai.file_count(kai)
        
    def by(self):
        ai.end()
