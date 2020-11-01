# Overview
The goal of this challenge was to transform the data given in the ```records.log'``` file into a .csv wtih the following columns: ```order_id, weight (lbs), volume (in3)```. 

# Instructions for Use on Linux Ubuntu

### Prerequisites:

**1.) Create and activate a new virtual envelope**
```
python3 -m venv coding_challenge 
source ./coding_challenge/bin/activate
```

**2.) Install tkinter**
```
sudo apt-get install python3-tk tk-dev
```


### Implementation

**3.) Run the script and follow the propt to select a file to convert**
```
python3 solution.py
```
![usage_example1](https://user-images.githubusercontent.com/8731829/97803340-25d90980-1c0f-11eb-8a33-b5b3db070c3d.png)

###### **Figure 1.** When running the script, a file browsing GUI where you can select the file you would like to transform will pop up.

**4.) View converted file in same directory as original file**

![usage_example2](https://user-images.githubusercontent.com/8731829/97803348-2b365400-1c0f-11eb-9aec-dd38b8e2c074.png)

###### **Figure 2.** Upon successful conversion, the terminal will print the new file's location which will be in the same directory as the original file

### Challenge Reflection


**Problem Solving**

The main challenge I faced when writing this script was how to parse the data from the log file in a way that was both simple and intuitive.  After recognizing that the log file data was in the dictionary format, I began to look into ways to parse a text dictionary into a python dictionary data structure.  I found the simplest way to do this was to use the json library.  My solution opens the file the user wants to transform and reads the file line by line.  In order to parse the data using the ```json.loads(')``` method, I simply first replace the ```'``` character with the ```"``` character.  

**Design**

I wanted to make sure that the script was easy and intuitive to use so I designed it in a way that the user could choose the file they wished to transform using a GUI.  Additionaly for ease of use I designed the script to output the transformed file in the same path the original file was located.  In respect to the low-level design, I designed my functions in a way that could easily be added on to to support different types of file conversions.  Finally the column data is stored in a queue which is later popped so that the space complexity is O(1) making my solution easily upgradable to handling multiple files at once.

**Summary**

Overall I really enjoyed re-familiarizing myself with some of the common challenges that occur when working with data for machine learning.  I had a lot of fun with the problem solving and design aspects of this challenge and strongly believe that this excercise will help me with projects I complete in the future.
