# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 14:16:06 2016

@author: hmcshan
"""
#Holley McShan
#Weather Report: Weather Aggregator

import sys
import my_weather_reader
import datetime
import os.path


#Define a function to indicate current hour in military time
def get_hour():
    """
    Function returns current hour in military time.
    
    Returns: current hour in military time
    """
    now = datetime.datetime.now()
    return str(now.hour)

#Define a function to indicate current date   
def get_date():
    """
    Function returns current date.
    
    Returns: current date (month-day-year)
    """
    now = datetime.datetime.now()
    return str(now.month) + "-" + str(now.day) + "-" + str(now.year)

#Define a function that prints usage of file
def print_usage():
    """Print usage"""
    print("weather_aggregator.py <file> <zip_code>")



#Define a function to write temperature for given hour/date into a file 
def write_temp_to_file(temp, file, zip_code):
    """
    Append/ write temperature to a file. Append if file exists; write new file
    if one does not.

    Args: temperature, filename, zip code
    """
    if os.path.exists(file) == False:
        with open(file, "w") as file:            
            file.write("\n" + str(get_date()) + " "+str(get_hour()) + " " \
            + zip_code + " " + temp)
    else:    
        with open(file, "a") as file:            
            file.write("\n" + str(get_date()) + " "+str(get_hour()) + " " \
            + zip_code + " " + temp)    



#Define a function to indicate if there is already entry for that date/hour    
def is_there(file):
    """ 
    Function returns boolean indicating if entry for that date/hour already
    exists in file.
    
    Args: file name
    
    Returns: boolean indicating if it's present
    """
    with open(file, "r") as file:

        search_string = get_date() + " " + get_hour() + " " + zip_code
        answer = False
        for line in file:
            # Assuming one word per line

            if line.find(search_string) != -1:
                answer = True
            
    return answer
                




if __name__ == "__main__":  
    #checking to see if has enough arguments/that zip code is 5 digits       
    if len(sys.argv) != 3 or len(sys.argv[2]) != 5:
        print_usage()   
    else:
        zip_code = sys.argv[2]
        file = sys.argv[1]
        temp = weather_reader.get_temperature(zip_code)
        print(temp) 
        if is_there(file) == False:
            write_temp_to_file(temp, file, zip_code)