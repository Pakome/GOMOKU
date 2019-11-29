import os

os.system("pip install pyinstaller")
os.system("pyinstaller main.py brain_commands.py --name pbrain-STG-LardHon.exe --onefile")
os.system('copy .\\dist\\pbrain-STG-LardHon.exe .')
