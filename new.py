#! /usr/bin/env python

import os.path
import time
from time import strftime
import os
import sys
import shutil

FILE = 'todo.md'
template = 'template.md'

def date_to_append():
    return strftime("%m-%d-%Y", time.gmtime(os.path.getctime(FILE)))

def rename_file(the_file):
    base = os.path.basename(the_file)
    split_up = os.path.splitext(base)
    file_name = split_up[0]
    file_extension = split_up[1]
    new_file_name = "%s_%s%s" % (file_name, date_to_append(), file_extension)
    os.rename(the_file, new_file_name)

def move_old_todo():
    for filename in os.listdir("."):
        if filename.startswith('todo'):
            if file_already_exists(filename):
                print "Already Exists"
            else:
                shutil.move(filename, 'Archive')

def file_already_exists(thefile):
    archive_path = os.path.abspath('Archive')
    files_in_archive = os.listdir(archive_path)
    if thefile in files_in_archive:
        return True
    else:
        return False

def create_new_todo():
    f = open(template, 'r')
    contents = ''
    for line in f:
      if '<date>' in line:
        contents += line.replace('<date>', strftime('%m-%d-%Y'))
      else:
        contents += line
    f.close()
    f = open('todo.md', 'w')
    f.write(contents)
    f.close()

if os.path.isfile(FILE):
  rename_file(FILE)
  move_old_todo()

create_new_todo()
