#!/usr/local/cs/bin/python3

import os as o
import os.path as p

def main():
    curDir = o.getcwd()
    while(not p.isdir(curDir + '/.git')):
        curDir = p.dirname(curDir)
        if(curDir == '/'):
            print("Not inside a Git repository")
            exit(1)
    print(".git is inside " + curDir)        

if __name__ == "__main__":
    main()
