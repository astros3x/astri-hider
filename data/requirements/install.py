import subprocess
import sys

with open('requirements.txt', 'r') as f:
    lines = f.readlines()
    for l in lines:
        package = l.strip()
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
        except Exception as e:
            print(f'\n\n{e}')