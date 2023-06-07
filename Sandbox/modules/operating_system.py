#!/usr/bin/python3

if __name__ != "__main__":

    import os
    import glob
    import shutil
    import sys
    import argparse

    def pwd():
        print(os.getcwd())

    def module_functions(value):
        for i in dir(value):
            print(i)

    def module_help(value):
       print(help(value))

    def get_glob(value):
        for i,v in enumerate(glob.glob('*.'+value)):
            print(i,v)

    def args():
        print(sys.argv)

    def parse_args():
        parser = argparse.ArgumentParser(
            prog='top',
            description="show top line from each file"
        )

        parser.add_argument("filenames",nargs="+")
        parser.add_argument("-l","--lines",type=int,default=10)
        arg = parser.parse_args()
        print(arg)
