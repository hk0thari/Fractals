import math
from turtle import *
import turtle


def draw_polygon(sides, lengths=100, poly_angles=None, pen_colors=None, fill_color=None, lefty=True, angle=0, reverse=False):

    original_color = pencolor()
    
    if not pen_colors:

        pen_colors = (pencolor(), ) * sides
    
    if type(lengths) in (int, float):
        
        lengths = (lengths, ) * sides
    
    if type(poly_angles) in (int, float):
        
        poly_angles = (poly_angles, ) * sides
    
    if type(pen_colors) is str:
        
        pen_colors = (pen_colors, ) * sides
    
    rt(angle)
    
    if fill_color:
        
        begin_fill()
        fillcolor(fill_color)
    
    for length, poly_angle, pcolor in zip(lengths, poly_angles, pen_colors):
        
        pencolor(pcolor)
        
        if lefty:
            segment(length, 360-poly_angle)
        
        else:            
            segment(length, poly_angle)
    
    if reverse:
        if lefty:
            rt(poly_angle)
        else:
            lt(poly_angle)
    
    if fill_color:
        
        end_fill()
    
    pencolor(original_color)


def draw_regular_polygon(sides, length=100, pen_colors=None, fill_color=None, lefty=True, angle=0, reverse=False):
    
    poly_angle = 360/sides
    draw_polygon(sides, length, poly_angle, pen_colors, fill_color, lefty, angle, reverse)


def square(length=100, pen_colors=("blue", )*4, fill_color=None, lefty=True, angle=0, reverse=False):
    
    draw_regular_polygon(4, length, pen_colors, fill_color, lefty, angle, reverse)


def triangle(lengths=None, poly_angles=None, pen_colors=None, fill_color=None, lefty=True, angle=0, reverse=False):
    
    draw_polygon(3, lengths, poly_angles, pen_colors, fill_color, lefty, angle, reverse)
    

def segment(s, w):
    
    fd(s)
    rt(w)


def arc(loop_length, length, pcolor, pwidth):
    
    original_color = pencolor()
    pencolor(pcolor)
    
    original_width = pensize()
    pensize(pwidth)
    
    for _ in range(loop_length):
        fd(length)
        rt(1)
    
    pencolor(original_color)
    pensize(original_width)


def circle(radius, pen_color=None, fill_color=None, lefty=True, angle=0):
    
    length = 2 * math.pi * radius / 360
    draw_regular_polygon(360, length, pen_color, fill_color, lefty, angle)


def petal(outline_color, fill_color):
    
    original_fill_color = fillcolor()
    begin_fill()
    fillcolor(fill_color)
    pwidth = pensize()
    
    arc(90, 2, outline_color, pwidth)
    rt(90)
    arc(90, 2, outline_color, pwidth)
    rt(90)
    end_fill()
    
    fillcolor(original_fill_color)
    

def flower(petals, outline_color, fill_color, stem_color, stem_width):
    
    for _ in range(petals):
        
        petal(outline_color, fill_color)
        rt(360/petals)
    
    #st()
    rt(145)
    arc(37, 8, stem_color, stem_width)


def star(sides):
    
    for _ in range(sides):
        
        angle = 360/sides
        
        segment(250/sides, 2 * angle)
        segment(250/sides, 360-angle)

