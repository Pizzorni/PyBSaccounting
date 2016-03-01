import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("-y","--year",nargs='*',type=int, 
                    help="list of years")
parser.add_argument("-m","--month",nargs='*',type=int,
                    help="list of months")
parser.add_argument("-d","--day",nargs ='*',type=int,
                    help="list of days")
parser.add_argument("-u", "--user",nargs ='*',type=str,
                    help="list of users")
parser.add_argument("-A","--all",help="use all log files", 
                    action="store_true")
args = parser.parse_args()


if not (args.year or args.month or args.day or args.all):
  parser.error('No dates specified')

if (args.year):
  year = args.year
  if any(y < 2010 or y > 2016 for y in year):  
    raise argparse.ArgumentTypeError("Year invalid")
if (args.month):
  month = args.month
  if any(m < 1 or m > 12 for m in month): 
    raise argparse.ArgumentTypeError("Month invalid")
if (args.day):
  day = args.day
  if any(d < 1 or d > 31 for d in day):
    raise argparse.ArgumentTypeError("Day invalid")
if (args.user):
  user = args.user

