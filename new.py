#! /usr/bin/env python
import os.path
import time
from time import strftime
import os
import sys
import shutil

FILE = 'todo.md'

def date_to_append():
    return strftime("%m-%d-%Y", time.gmtime(os.path.getctime(FILE)))

def rename_file(the_file):
    base = os.path.basename(the_file)
    split_up = os.path.splitext(base)
    file_name = os.path.splitext(base)[0]
    file_extension = split_up[1]
    new_file_name = "%s%s%s" % (file_name, date_to_append(), file_extension)
    os.rename(the_file, new_file_name)

def move_old_todo():
    for filename in os.listdir("."):
        if filename.startswith('todo'):
            shutil.move(filename, 'Archive')

def create_new_todo():
    open(FILE, 'w')

rename_file(FILE)
move_old_todo()
create_new_todo()
