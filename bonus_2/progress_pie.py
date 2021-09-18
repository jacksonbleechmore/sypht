import math
import numpy as np
import sys

class circle:
    centre = {'x':50,'y':50}
    radius = 50


def percent_to_radians(percent):
    return ((percent/100) * 2*np.pi)

def radius_y_cord(theta,x):
    return 1/(math.tan(theta))*(x-circle.centre['x']) + circle.centre['y']

def in_circle(x,y):
    #evalueate the y value on circumference 
    y_circ = math.sqrt((circle.radius)**2 - (x - circle.centre['x'])**2) + circle.centre['y']
    return abs(y) < y_circ


def is_right_hemisphere(x):
    return x >= circle.centre['x']

def is_black_side_of_radius(percent, x, y):
    theta = percent_to_radians(percent)
    y_radius = radius_y_cord(theta, x)
    if percent <=50:
        retVal = y > y_radius
    else:
        retVal = y < y_radius
    return retVal 



def in_segment(percent, x, y):
    retVal = False
    if percent <=50:
        if is_right_hemisphere(x):
            retVal = is_black_side_of_radius(percent,x,y)
        else:
            retVal = False
    else:
        if is_right_hemisphere(x):
            retVal = True
        else:
            retVal = is_black_side_of_radius(percent,x,y)
    return retVal



def is_black(percent, x, y):
    if in_circle(x,y) and in_segment(percent, x, y):
        return True
    else:
        return False
        

def read_input_from_file(file_name):
    f = open(file_name, 'r')
    input_text = f.read()
    lines = input_text.split('\n')
    input_list = []
    for line in lines[1:]:
        try:
            str_line = line.split(' ')
            int_line = [int(a) for a in str_line]
            input_list.append(int_line)
        except:
            continue
    return input_list
    

def main():
    input_list = read_input_from_file('/Users/jackson/Sypth/bonus_2/input.txt')
    for i in input_list:
        if i[0]!=0 and is_black(i[0],i[1],i[2]):
            print('Case #{}: black'.format(i))
        else:
            print('Case #{}: white'.format(i))
        

main()

