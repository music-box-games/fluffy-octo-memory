import os
import argparse
import time
import glob
import logging
from PIL import Image

def resize_list(file_list, width, height, dsonly):
  changed_files = 0
  ignored_files = 0

  for file in file_list:
    try:
      im = Image.open(file)
      # ignore files that are the same size already
      if im.size == (width, height):
        ignored_files += 1
      # ignore files that are smaller to told to
      if dsonly:
        if im.size[0] < width or im.size[1] < height:
          ignored_files += 1
      im.resize((width, height))
      im.save(file)
      changed_files += 1
    except IOError:
      pass

  return changed_files, ignored_files

def collect_filepaths(path, recurse):
  filelist = []
  if recurse:
    for root, dirs, files in os.walk(path):
      for file in files:
        filelist.append(os.path.join(root, file))
  else:
    for filename in glob.iglob(path + '**/**', recursive=True):
      filelist.append(os.path.join(path, filename))
  return filelist

def main():
  parser = argparse.ArgumentParser(description='Resizes image files in the given folder to a given size.')
  parser.add_argument('path', type=str, help='Path to search. Must end with "/"')
  parser.add_argument('width', type=int, help='Width to resize to')
  parser.add_argument('height', type=int, help='Height to resize to')
  parser.add_argument('-r', '--recursive', help='Searches subfolders', action='store_true')
  parser.add_argument('-v', '--verbose', help='Verbose output mode', action='store_true')
  parser.add_argument('--downscale_only', help='Prevents the program from upscaling images that are smaller than the given resolution.', action='store_true')
  args = parser.parse_args()
  print('Working...')
  fl = collect_filepaths(args.path, args.recursive)
  start_time = time.perf_counter()
  change_count, ignore_count = resize_list(fl, args.width, args.height, args.downscale_only)
  stop_time = time.perf_counter()
  print(f'Resized {change_count} files in {stop_time-start_time:0.4f} seconds (an additional {ignore_count} files were ignored).')

if __name__ == "__main__":
  main()