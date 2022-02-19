import os, sys
sys.path.append(os.getcwd())

from subprocess import run
from lib.core.case_create import CreateCase
import lib.config.config as config

def init():
    disfiles = os.listdir(config.TESTCASES_PATH)
    for file in disfiles:
        if os.path.isfile(config.TESTCASES_PATH + file):
            os.remove(config.TESTCASES_PATH + file)

    create = CreateCase()
    create.create()
    
    run('pytest')

if __name__ == '__main__':
    init()
