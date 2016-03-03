import argparse
import re
import datetime
from itertools import product

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('-y','--year',nargs='*',type=int, 
                      help='list of years')
  parser.add_argument('-m','--month',nargs='*',type=int,
                      help='list of months')
  parser.add_argument('-d','--day',nargs ='*',type=int,
                      help='list of days')
  parser.add_argument('-u', '--user',nargs ='*',type=str,
                      help='list of users')
  parser.add_argument('-A','--all',help='use all log files', 
                      action='store_true')
  args = parser.parse_args()

  
  # Require at least one
  if not (args.year or args.month or args.day or args.all):
    parser.error('No dates specified')

  year, month, day, user = validate_input(args)
  year, month, day =  normalize_input(year, month, day)
  file_names = generate_file_names(year,month,day)
  
  if(user):
    users = {u:0 for u in user}
  else:
    users = {}

  user_regex = r"user=(\w+)\b"
  user_patt = re.compile(user_regex)

  for file in file_names:
    try:
      with open(file) as f:
        for line in f:
          match = user_patt.findall(line)
          if len(match) > 0:
            if match[0] in users:
              users[match[0]] += 1
            elif len(user) == 0:
              users[match[0]] = 1
    except IOError as ignored:
      pass

  #print usr_list
  num_jobs = sum(users.values())
  user_keys = users.keys()
  user_keys.sort()
  print "Users,Jobs"
  for key in user_keys:
    print key + "," + str(users[key])
  print "Total number jobs: " + str(num_jobs)
      

def validate_input(args):
  year_list = [x for x in xrange(2010,2017)]
  month_list = [x for x in xrange(1,13)]
  day_list = [x for x in xrange(1,32)]
  user_list = []
  if (args.year):
    year_list = args.year
    if any(y < 2010 or y > 2016 for y in year_list):  
      raise argparse.ArgumentTypeError('Year invalid')
  if (args.month):
    month_list = args.month
    if any(m < 1 or m > 12 for m in month_list): 
      raise argparse.ArgumentTypeError('Month invalid')
  if (args.day):
    day_list = args.day
    if any(d < 1 or d > 31 for d in day_list):
      raise argparse.ArgumentTypeError('Day invalid')
  if (args.user):
    user_list = args.user

  return year_list, month_list, day_list, user_list

def normalize_input(year, month, day):
  year = map(str, year)
  month_tmp = map(str,month)
  day_tmp = map(str,day)
  month = []
  day = []
  for m in month_tmp:
    if len(m) != 2:
      month.append("0" + m)
    else:
      month.append(m)
  for d in day_tmp:
    if len(d) !=2:
      day.append("0" + d)
    else:
      day.append(d)
  return year, month, day

def generate_file_names(year, month, day):
  file_names = list((''.join(prod) for prod in 
              product(year,month,day)))
  return file_names
main()
