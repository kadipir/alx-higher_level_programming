#!/usr/bin/python3
#sorts a list of integers and finds the peak

def find_peak(list):
    if list:
        list.sort(reverse = True)
        return list[0]

