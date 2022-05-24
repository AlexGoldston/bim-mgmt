'''search given directory for .rvt files > log to file with path + filename'''

'''
search all projects on given directory for project folder Z-Current Drawings (all phases) and dump report of all pdfs out to csv
'''

import os
import sys
import shutil
import re
import time
from pprint import pprint
from pathlib import Path
from turtle import clear


'''___VARIABLES____'''
drive_x = r'X:\Projects'
drive_l = r'L:\PROJECTS\APAC'
drive_r = r'R:\\'
# drive_r = r'R:\10-7160-00_GoldCoast_Show'



if __name__ == '__main__':

    # for root, directories, filenames in os.walk(drive_r):
    #     for directory in directories:
    #         for filename in filenames:
    #             if filename.endswith('.rvt'):
    #                 print(directory)
    #                 print('______________  ',filename)


    rvt_files = []
    for dirpath, subdirs, files in os.walk(drive_r):
        for x in files:
            if x.endswith(".rvt"):
                rf = rvt_files.append(os.path.join(dirpath, x))
                if rf == None:
                    print(f'none found in {dirpath}')
                else:
                    print(rf)

    # for f in rvt_files:
    #     print(f)