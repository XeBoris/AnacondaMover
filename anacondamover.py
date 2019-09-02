#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""A simple script to move your Anaconda base directory
   to another directory after the full installation.
   This includes the created environments.

   Author: Boris Bauermeister
   Email: Boris.Bauermeister@gmail.com
   First Commit: 02.09.2019
"""

import os
import sys
import argparse
import re
import shutil

def get_folders(path):
    folder = []
    for root, dirs, files in os.walk(path):
        folder.extend(dirs)
        break
    return folder
    
def get_files(path):
    files = []
    for root, dirs, files in os.walk(path):
        files.extend(files)
        break
    return files
    

def replace(filename, text_to_search, replacement_text):
    #Replace with RE package, inspired by Stackoverflow
    file_handle = open(filename, 'r')
    file_string = file_handle.read()
    file_handle.close()

    file_string = (re.sub(text_to_search, replacement_text, file_string))

    file_handle = open(filename, 'w')
    file_handle.write(file_string)
    file_handle.close()


def set_function(path, old_path=None, new_path=None):
    
    #get all files from main
    all_files = get_files(path)
    
    for i_file in all_files:
        p_file = os.path.join(path, i_file)

        #skip if not a file
        if not os.path.isfile(p_file):
            continue
        
        #try to look the requested string (slow,... but ok)
        try:
            with open(p_file, 'r') as the_file:
                all_data = [line.strip() for line in the_file.readlines()]
        except:
            all_data = ""
        
        k_in = False
        for i_line in all_data:
            if i_line.find(old_path) >=0:
                k_in = True
        
        if k_in == False:
            continue
        
        #Change file:        
        try:
            print("Change: {0} from {1} to {2}".format(p_file, old_path, new_path))
            
            replace(p_file, old_path, new_path)
        except:
            print("file replacement failed")

def copyconda(from_path, to_path):
    try:
        print()
        print("Start to copy Anaconda directory")
        shutil.copytree(from_path, to_path)
        print("Finished")
        print()
    except:
        print("Something wrong with copying the directory")
                    

    
def main():
    parser = argparse.ArgumentParser(description="Hello; I move your Anaconda environment")

    parser.add_argument('--input', dest='input_', type=str, default=None,
                        help="Specify your input directory")
    parser.add_argument('--output', dest='output_', type=str, default=None,
                        help="Specify your output directory")
    parser.add_argument('--skip-copy', dest='skip_copy', action='store_true')
    
    
    args = parser.parse_args()
    anaconda_old = args.input_
    anaconda_new = args.output_
    
    anaconda_old_abs = os.path.abspath(anaconda_old)
    anaconda_new_abs = os.path.abspath(anaconda_new)
    
    anaconda_old = anaconda_old+"/"
    anaconda_in = anaconda_new+"/"
    
    print()
    print("Hello; I move your Anaconda environment")
    print("---------------------------------------")
    print()
    print("Absolute paths")
    print("In: {0}".format(anaconda_old_abs))
    print("Out: {0}".format(anaconda_new_abs))
    print("----")
    print(" Search and replace patterns:")
    print("Search for: {0}".format(anaconda_old))
    print("Replace by: {0}".format(anaconda_in))
    
    #Decide if the Anaconda folder is copied by this script or if
    #you have done it manually.
    if args.skip_copy == False:
        copyconda(anaconda_old_abs, anaconda_new_abs)
    else:
        print("Skip to copy the environment")
    
    print("Re-prefix of the copied Anaconda environment")
    
    #get folders
    if os.path.isdir(anaconda_in):
        main_dir_overview = get_folders(anaconda_in)
        if 'envs' in main_dir_overview:
            additional_environments = get_folders(os.path.join(anaconda_in, "envs"))
            
    else:
        print("Something wrong with ", anaconda_in, " exit here")
        exit()
        
    #main path:
    set_function(os.path.join(anaconda_in, "bin"), anaconda_old, anaconda_in)
    
    #go over environments:
    for i_env in additional_environments:
        p_full = os.path.join(anaconda_in, "envs", i_env, "bin")
        set_function(p_full, anaconda_old, anaconda_in)
    
    print("done")
    exit(0)
    
if __name__ == '__main__':
    main()
