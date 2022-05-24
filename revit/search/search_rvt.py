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



if __name__ == '__main__':

    for root, directories, filenames in os.walk(drive_r):
        for directory in directories:
            for filename in filenames:
                if filename.endswith('.rvt'):
                    print(directory)
                    print('______________  ',filename)
