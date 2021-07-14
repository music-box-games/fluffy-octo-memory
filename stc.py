import os
import argparse
import time
import glob

def rename_file(oldpath, newpath):
  os.rename(oldpath, newpath)


def collect_filepaths(path, recurse):
  filelist = []
  if recurse:
    for root, dirs, files in os.walk(path):
      for file in files:
        if file.find(' ') != -1:
          filelist.append(os.path.join(root, file))
  else:
    templist = []
    for filename in glob.iglob(path + '**/**', recursive=True):
      templist.append(os.path.join(path, filename))
    for f in templist:
      if f.find(' ') != -1:
        filelist.append(os.path.join(path,f))
  
  return filelist

def main():
  parser = argparse.ArgumentParser(description='Converts spaces to a given character.')
  parser.add_argument('path', help='Target path to search.', type=str)
  parser.add_argument('character', help='Character(s) to replace spaces with.', type=str)
  parser.add_argument('-r', '--recursive', help='Searches subfolders.', action='store_true')
  args = parser.parse_args()
  start_time = time.perf_counter()
  print('Working...')
  paths = collect_filepaths(args.path, args.recursive) # collect path to each file with space in name
  for p in paths:
    oldfile = p
    newfile = os.path.join(os.path.dirname(p), os.path.basename(p).replace(' ', args.character))
    rename_file(oldfile, newfile)
  end_time = time.perf_counter()
  print(f'Took {end_time-start_time:0.4f} seconds to rename {len(paths)} files.')




if __name__ == '__main__':
  main()
