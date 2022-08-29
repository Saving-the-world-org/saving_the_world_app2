# -*- coding: utf-8 -*-
"""crawler utility. Various iterative functions"""

import os
from os import listdir
from pathlib import Path

def get_collection(i):
    """
        Args:
            input_folder (string): The folder to begin crawling.

        Returns:
            A dictionary of items found during the crawl.
            collection(['0001', '0002', '0003', etc...])
    
    """

    # if not os.path.exists(i):
    #     return "No Folder exists at that location."
    #     os.mkdir(i)

    mylist = []
    mylist = os.listdir(i)
    mylist.sort()
    return mylist

def get_images(i):
    """
        Args:     input_folder (string) - only returns files of type set by `ext`

        Returns:  A list of files
 
    """
    mylist = []
    mylist = os.listdir(i)
    mylist.sort()
    ext = ('.png','.jpg')
    files = []
    for file in mylist:
        if file.endswith(ext):
            files.append(file)
        else:
            continue
    return(files)

def prd_get_init_image(i):
    """
        Args:     input_path (string) - only returns files of type set by `ext`

        Returns:  A single file
 
    """
    mylist = []
    mylist = os.listdir(i)
    mylist.sort()
    ext = ('.png','.jpg')
    files = []
    for file in mylist:
        if file.endswith(ext):
            files.append(file)
        else:
            continue
    return(files)