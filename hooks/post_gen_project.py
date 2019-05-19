import os
import shutil

def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


opensource_project = '{{cookiecutter.opensource_project}}' == 'y'

if not opensource_project:
    # Remove License file. Copyright will stay with Sparkgeo without a license. We should get a proper license though...
    remove('LICENSE.txt')