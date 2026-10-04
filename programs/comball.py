import pandas as pd
import numpy as np
import os
import json

from setup.path_prog import inputfdl, outputfdl, prog_fdl, setupfdl
from programs.getjson import jsld
from programs.promptbuild import build_prom
p=build_prom(jsld)
print(p)