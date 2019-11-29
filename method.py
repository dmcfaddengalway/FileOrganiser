from os import listdir
from os.path import isfile, join
from datetime import datetime
import os
import shutil


def is_hidden(filepath):
    name = os.path.basename(os.path.abspath(filepath))
    return name.startswith('.')

def organise():

  files = [f for f in listdir(my_path) if isfile(join(my_path, f)) and not is_hidden(join(my_path, f))]

  file_type_variation_list = []
  folder_list = []
  filetype_to_folder_dict = {}

  now = datetime.now()
  year = now.strftime('%Y')
  print(year)

  for file in files:
    file_type = file.split('.')[1]
    if file_type not in file_type_variation_list:
      file_type_variation_list.append(file_type)
      new_folder_name = my_path + '/' + file_type
      filetype_to_folder_dict[str(file_type)] = str(new_folder_name)
      if os.path.isdir(new_folder_name) == True:
        continue
      else:
        print('Making folder of name: ' + new_folder_name )
        os.mkdir(new_folder_name)

  print('filetype_to_folder_dict', filetype_to_folder_dict)

  for file in files:
    src_path = my_path + '/' + file
    file_type = file.split('.')[1]
    if file_type in filetype_to_folder_dict.keys():
      dest_path = filetype_to_folder_dict[str(file_type)]
      shutil.move(src_path, dest_path)
      print(src_path + ' >>> ' + dest_path)

my_path = '/Users/dannymcfadden/Desktop/newFolder'
organise()
