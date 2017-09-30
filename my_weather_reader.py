# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 13:13:53 2016

@author: hmcshan
"""
#Holley McShan
#Weather Report: Weather Reader

import sys
import urllib.request

URL_TEST = "http://www.cs.middlebury.edu/~mlinderman/courses/cs150/f16/labs/lab7-test-data.json"
KEY = "c53e22fb78f1b75497896644e172aa6d"
        
def get_temperature(zip_code):
    """
    Return current temperature for a given zip code
    
    Args:
        zip_code 
        
    Returns:
        Temperature
    """
    url = "http://api.openweathermap.org/data/2.5/weather?zip=<ZIP>,us&appid=c53e22fb78f1b75497896644e172aa6d&units=imperial"
    url = url.replace("<ZIP>", zip_code) 
    search_string = 'temp":'

    temp = None
        
    with urllib.request.urlopen(url) as webpage:
        for line in webpage:
            line = line.decode('utf-8', 'ignore')
            
            # Seach for instances of "temp:" in the line            
            begin_index = line.find(search_string)
            if begin_index != -1:
                begin_index += len(search_string)
                end_index = line.find(',', begin_index)
                temp = line[begin_index:end_index]                
        return temp    



if __name__ == "__main__": 
    if len(sys.argv) != 2:        
        print("my_weather_reader.py <ZIP_CODE>")
    else:
        zip_code = sys.argv[1] 
        print(get_temperature(zip_code))