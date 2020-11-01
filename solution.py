#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 10:03:47 2020

@author: Akira DeMoss
"""
import json
import csv
import os
import tkinter
import tkinter.filedialog
from collections import deque 


#Store column data for file in queue to reduce space complexity
order_id, weight, volume = deque(),deque(),deque()

#Converts a file to csv format
def transform_to_csv(): 
    fpath = __get_fpath()
    get_col_data(fpath)
    fpath = __get_new_fpath(fpath, ".csv")
    #Write columns to .csv file
    with open(fpath, "w") as file:
        csv_file = csv.writer(file)
        csv_file.writerow(["order_id", "weight (lbs)", "volume (in3)"])    
        for i in range(len(order_id)):
            csv_file.writerow([order_id.popleft(), weight.popleft(), volume.popleft()])
    print("transformation complete, file located at: ", fpath)

#Gets data for .csv format
def get_col_data(fpath):
    global order_id, weight, volume
    with open(fpath, "r") as file:
        for line in file:
            line = line.replace('\'','\"')
            data = json.loads(line)
            order_id.append(data['order_id'])
            __is_imperial(data['package']['weight'],data['package']['volume'],data['package']['imperial_unit'])
            
#Helper method for get_col_data. If imperial is false, converts units to imperial before appending.  
def __is_imperial(weight_kg, vol_cm3, imperial_unit):
    global order_id, weight, volume
    if imperial_unit == "false":
        converters = {}
        converters['lbs'] = lambda x: '{}'.format(round(x*2.2,1))
        converters['in3'] = lambda x: '{}'.format(round(x*0.0610237441,1))
        weight_kg = converters['lbs'](weight_kg)
        vol_cm3 = converters['in3'](vol_cm3)
    weight.append(float(weight_kg))
    volume.append(float(vol_cm3))            
        
#Helper method that gets the file path of the file you want to transform
def __get_fpath():
    root = tkinter.Tk()
    while True:
        print("Please select a file to transform")
        fpath = tkinter.filedialog.askopenfilename()
        if fpath == None or fpath == "":
            print("You must select a file.")
            continue
        break
    root.destroy()
    return fpath

#Helper method that returns the new filepath based on extension looking to write. e.g. ext = ".csv"
def __get_new_fpath(fpath,file_ext):
    dir_path = os.path.dirname(fpath) 
    fname = os.path.basename(fpath)   
    finfo = os.path.splitext(fname)
    new_fpath = dir_path + "/" + finfo[0] + file_ext
    return new_fpath

if __name__ == '__main__':
    transform_to_csv()

    

