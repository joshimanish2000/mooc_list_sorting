#! /usr/bin/env python3

import os
import csv
import sys

file = sys.argv[1]  #get the csv file from command line
mooc_dic1 = {}
mooc_dic2 = {}
hours_dic = {}

with open(file,'r') as f:
  csv_f = csv.reader(f)
  for line in csv_f:
    course1, hours1, course2, hours2 = line[5].lower().lstrip(), line[8], line[10].lower().lstrip(), line[13]
    mooc_dic1[course1] = mooc_dic1.get(course1,0)+1
    mooc_dic1[course2] = mooc_dic1.get(course2,0)+1
    mooc_dic1_view = [(v,k) for k,v in mooc_dic1.items()]
    hours_dic[hours1] = hours_dic.get(hours1, 0)+1
    hours_dic[hours2] = hours_dic.get(hours1, 0)+1
    hours_dic_view = [(a,b) for b,a in hours_dic.items()]
    hours_dic_view.sort(reverse=True)
    #mooc_dic2_view = [(v,k) for k,v in mooc_dic2.items()]
    mooc_dic1_view.sort(reverse=True)
    #mooc_dic2_view.sort(reverse=True)

  print("course: no. of students")
  for v,k in mooc_dic1_view:
    print("{}: {}".format(k,v))
  print("\n")
  print("hours: no. of courses")
  for m,n in hours_dic_view:
    print("{}: {}".format(n,m))
  #print(mooc_dic1.sort(), sorted(mooc_dic2.values()))
