#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("year", type = int)
parser.add_argument("month", type = int)
parser.add_argument("day", type = int)
parser.add_argument("--all", help = "use all log files in current 
                    directory", action = "store_true")
args = parser.parse_args()



