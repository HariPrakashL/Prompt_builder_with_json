import pandas as pd
import numpy as np
import os
import json

#taking path from setup/path_prog.py to use in this program

from setup.path_prog import inputfdl, outputfdl, prog_fdl, setupfdl

#now should write code to read json file

print("checking the path of input folder")

with open(inputfdl / "singlecomp.json","r") as f:
    jsld=json.load(f)
#print(jsld)

print(jsld["study_id"])