import glob
import os

for file in glob.glob('*.jpg'):
     os.rename(file, file[:-3] +'png')