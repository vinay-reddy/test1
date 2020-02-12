
import pandas as pd
import subprocess
import os, re, json
import tarfile
import numpy as np
import concurrent.futures

ro = re.compile(r'\d{4}\t')
#path = '/Users/vinayreddy/Desktop/logs/chandra-long/6_7/tmpgfR9Qo'
#path = '/Users/vinayreddy/Desktop/logs/kushal/tmp505h5X/'
#path = '/Users/vinayreddy/Desktop/logs/rohit-1/tmpDAUyYu'
path = '/Users/vinayreddy/Documents/Log_Analyzer_Root/media/Logs/'

def full_path(filename):
    for f, sf, files in os.walk(path):
        if filename in files:
            return f + '/' + filename

def extracting_lines(start_line, end_line, filepath):
    with open(filepath) as inf:
        grab = False
        for l in inf:
            if start_line in l.strip():
                grab = True
                print(l.strip())
            elif l.startswith(end_line) and grab is True:
                print(l.strip())
                break
            elif grab:
                print(l.strip())




# event viewer
event_viewer_file = full_path('tips-system-events.txt')
columns = ['Time', 'Source', 'Level', 'Category', 'Description', 'Action']
df_ev = pd.read_csv(event_viewer_file, header=None, skiprows=1, sep='|', names=columns)

filtered_df = df_ev[(df_ev['Level'].str.strip() == 'ERROR')|(df_ev['Level'].str.strip() == 'WARN')]

