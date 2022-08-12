import os

TAGTOO_PROJECTS_SITE = os.environ.get("TAGTOO_PROJECTS_SITE")

class Project:

    def __init__(self):
        self.projects_site = TAGTOO_PROJECTS_SITE or '/Users/wcl/Desktop/tagtoo'  


'''
import subprocess, platform

if platform.system()=="Windows":
    subprocess.Popen("cls", shell=True).communicate() #I like to use this instead of subprocess.call since for multi-word commands you can just type it out, granted this is just cls and subprocess.call should work fine 
else: #Linux and Mac
    print("\033c", end="")
'''