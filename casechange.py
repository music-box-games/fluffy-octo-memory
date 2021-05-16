import argparse
import os
import glob
import time

def collect_filepaths(path, recurse):
  filelist = []
  if recurse:
    for root, dirs, files in os.walk(path):
      for file in files:
        filelist.append(os.path.join(root, file))
  else:
    templist = []
    for filename in glob.iglob(path + '**/**', recursive=True):
      templist.append(os.path.join(path, filename))
    for f in templist:
      filelist.append(os.path.join(path,f))
  
  return filelist

def main():
  parser = argparse.ArgumentParser(description='Changes the case of filenames.')
  parser.add_argument('path', help='Path to search in.', type=str)
  parser.add_argument('-r', '--recursive', help='Search subdirs.', action='store_true')
  group = parser.add_mutually_exclusive_group()
  group.add_argument('-l', '--lowercase', help='Change filenames to be lowercase.', action='store_true')
  group.add_argument('-u', '--uppercase', help='Change filenames to be uppercase.', action='store_true')

  args = parser.parse_args()
  if not args.lowercase and not args.uppercase:
    print('Must specify either lowercase or uppercase.')
    return 1

  print('Working...')
  start_time = time.perf_counter()
  print('Collecting filepaths...')
  filelist = collect_filepaths(args.path, args.recursive)
  count = 0
  print('Renaming files...')
  for file in filelist:
    # this could be better
    fname = os.path.basename(file)
    if args.lowercase:
      fname = fname.lower()
    elif args.uppercase:
      fname = fname.upper()
    fname = os.path.join(os.path.dirname(file), fname)
    os.rename(file, fname)
    count += 1
  end_time = time.perf_counter()
  print(f'Renamed {count} files in {end_time-start_time:0.4f} seconds.')
  return 0

if __name__ == "__main__":
  ret = main()
  exit(ret)