from setuptools import setup
from os import system
import platform

USER_PLATFORM = platform.system()

if __name__ == "__main__":
    system('pip install -r requirements.txt')
    system('pip install pyinstaller')

    if USER_PLATFORM == 'Windows':
        system('pyinstaller src/main.py')
    elif USER_PLATFORM == 'Linux':
        system('pyinstaller -D -F -n Viruses_Destroyer -c "src/main.py"')
    setup()

