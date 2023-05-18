
import os
from menu import HERE
from pathlib import Path
import shutil

print(os.path.exists('temp/cbarker12/bike'))
shutil.rmtree(HERE / "temp/cbarker12/bike/red")
shutil.rmtree(HERE / "temp/fjones34/bird/green")