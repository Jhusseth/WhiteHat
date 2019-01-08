import os
#import Permissions_Android
#from Generator import Manifest
from os import listdir
from os.path import isfile
import optparse
from static_analysis import Manifest


""" Author:  Christian Urcuqui
    Last update: 24 November 2018
    Description: This project makes a dataset with features from static analysis and 
    dynamic analysis. It is neccesary to use this tool with root privileges    
"""
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$_$$$$$$$$$$$$$$$$_$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$__$$$$$$$$$$$$$$_$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$_______________$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$___________________$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$____$$$_________$$$____$$$$$$$$$$$$$
# $$$$$$$$$$$$$_____$$$_________$$$_____$$$$$$$$$$$$
# $$$$$$$$$$$$___________________________$$$$$$$$$$$
# $$$$$$$$$$$$___________________________$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$_____$$$____________________________$$$____$$$
# $$$$_____$$$____________________________$$______$$
# $$$$_____$$$____________________________$$______$$
# $$$$_____$$$____________________________$$______$$
# $$$$_____$$$____________________________$$______$$
# $$$$_____$$$____________________________$$______$$
# $$$$_____$$$____________________________$$______$$
# $$$$______$$____________________________$$______$$
# $$$$_____$$$____________________________$$______$$
# $$$$$___$$$$____________________________$$$___$$$$
# $$$$$$$$$$$$____________________________$$$$$$$$$$
# $$$$$$$$$$$$____________________________$$$$$$$$$$
# $$$$$$$$$$$$___________________________$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$______$$$$$$_____$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$______$$$$$$_____$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$______$$$$$$_____$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$______$$$$$$_____$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$______$$$$$$_____$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$



apktool_dir = "/usr/local/bin/apktool.bat"
"""apktool_dir = "sudo apktool"""
dir_apk = "cd .."
package_output = "output"


def menu():
    # This is the command menu
    s = "\n"
    log = (" ___   ___    __   ____  ___    ___    __    __               ",
           "|   | /  |   |  |  |  |  |  |  /  |   |  |  |  |      [0][1][0]   ",
           "|       /    |  |  |  |  |       /    \   \_/  /      [1][1][1]   ",
           "|      /     |  |  |  |  |      /      \  \_/ /       [1][1][1]   ",
           "|  |\  \     |  '--'  |  |  |\  \       \    /        Android     ",
           "| _| `.__\   |________|  | _| `.__\      |___|                    ")
    out = s.join(log)
    print(out)
    parser = optparse.OptionParser("Make dataset -d <dictionary> -a <analysis>")
    parser.add_option("-d", dest="dname", type="string", help="APK dictionary")
    parser.add_option("-a", dest="aname", type="string", help="type of analysis")
    (options, args) = parser.parse_args()
    if(options.dname is None) | (options.dname is None):
        print(parser.usage)
        exit(0)
    else:
        aname = options.aname
        dname = options.dname
        print(dname)
        if aname == "static":
            m = Manifest()
            m.start(dname)



if __name__ == "__main__":
    menu()

