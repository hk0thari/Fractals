from shapes import *
import random


def fibonacci(n):
    
    if n == 2:
        return 1
    
    if n == 1:
        return 0
    
    return fibonacci(n-1) + fibonacci(n-2)


def bunny_ears(n): # n=3
    
    x = 0    
    
    if n == 1:
        x = 2
    
    elif n % 2 == 0:
        
        x = bunny_ears(n-1) + 3
    
    else:
        
        x = bunny_ears(n-1) + 2  # b(2) + 2 = (b(1) + 3) + 2
    
    return x


def pythagoras_tree(s):
    
    if s < 4:
        square(s, lefty=False)  # Draws an extra square at the end
        return
    
    square(s, lefty=False)
    fd(s)
    lt(45)
    
    # By pythagoras theorem.
    
    s1 = s/math.sqrt(2)
    pythagoras_tree(s1)
    
    #penUp() # depends on what you want to do with the function
    rt(90)
    fd(s1)
    #penDown()
    
    pythagoras_tree(s1)
    
    # Fulfill the promise of going back to original place in original orientation.
    
    #penUp()
    back(s1)
    lt(45)
    back(s)
    #penDown()


def tree(s):
    
    if s < 5:
        return
    
    fd(s)
    s1 = s*0.6
    lt(45)
    tree(s1)
    rt(90)
    tree(s1)
    lt(45)
    back(s)


def snowflake_2(s):

    # Snowflake like fractal
    
    if s < 1:
        return
    
    s1 = s/3
    
    for _ in range(6):
        
        fd(s)
        snowflake_2(s1)
        back(s)
        rt(60)


def fractal_tree(s):
    
    if s < 5:
        return
    
    x, y = pos()
    h = heading()
    p_width = pensize()

    r = random.random()
    
    # Multiplying by 2*vary_num makes the range from 0 to 2*vary_num.
    # Subtracting vary_num makes range from -vary_num to vary_num.
    
    vary_num = 0.25
    variation = (r * 2 - 1) * vary_num
    
    r1 = random.random()
    # For desert like trees, angle variation should decrease with s
    angle_vary_num = 0.2  # for trees with large canopies, angle variation should increase with s

    angle_variation = (2*r1-1)*angle_vary_num
    
    a = s/3 * (1 + variation)
    b = s/6 * (1 + variation)
    c = s/3 * (1 + variation)

    # Pen_sizes
    p1 = max(int(a/8), 1)
    p2 = max(int(b/8), 1)
    p3 = max(int(c/8), 1)
    
    angle_a = 40 * (1+angle_variation)
    angle_b = 25 * (1+angle_variation)
    angle_c = 20 * (1+angle_variation)
    angle_d = 15 * (1+angle_variation)

    scale_var_a = 0.04*(random.random()*2-1)
    scale_var_b = 0.04*(random.random()*2-1)
    scale_var_c = 0.04*(random.random()*2-1)
    scale_var_d = 0.04*(random.random()*2-1)

    pensize(p1)
    fd(a)
    
    lt(angle_a)
    fractal_tree(s*0.6*(1+scale_var_a)) #0.66
    rt(angle_a)

    pensize(p2)
    fd(b)
    rt(angle_b)
    fractal_tree(s*0.5*(1+scale_var_b)) # 0.5
    
    rt(angle_c)

    pensize(p3)
    fd(c)
    fractal_tree(s*0.5*(1+scale_var_c))
    
    back(c)
    lt(angle_c + angle_b)
    # back(s/2)

    pensize(p1)
    back(a)
    rt(angle_d)
    fractal_tree(s*0.7*(1+scale_var_d))
    lt(angle_d)
    pensize(p2)
    back(b)

    pensize(p_width)
    
    # setPos(x, y)
    # heading(h)


def snowflake(l):

    # Koch Curve
    
    if l < 1:
        
        fd(l)
        return
    
    # Break curve in to 3, 2nd part is equilateral triangle missing base.

    snowflake(l / 3)
    
    lt(60)
    snowflake(l / 3)
    rt(120)
    snowflake(l / 3)
    
    lt(60)
    snowflake(l / 3)


if __name__ == "__main__":
    tracer(0)

    # Realistic randomised tree

    # lt(90)
    # s = 300
    # pu()
    # setpos(0, -s/2)
    # pd()
    # fractal_tree(s)

    # Pythagoras Tree

    # lt(90)
    # ht()
    # s = 100
    # pu()
    # setpos(-0.5 * s, -s*2)
    # pd()
    # pythagoras_tree(s)

    # Koch's snowflake curve

    # s = 300
    # lt(30)
    # pu()
    # setpos(-s/2, 0)
    # pd()
    # for _ in range(4):
    #
    #     snowflake(s)
    #     rt(120)

    # Second type of snowflake

    # snowflake_2(150)

    # Basic tree

    # s = 220
    # lt(90)
    # pu()
    # setpos(0, -s)
    # pd()
    # tree(s)

    # star(1000)
    # lt(90)
    # fd(30)
    # flower(5, "black", "red", "brown", 10)

    # import time
    # pu()
    # setpos(0, -150)
    # pd()
    # step = 1
    # angle = 72
    # length = 5
    # total_length = 0
    #
    # pencolor("black")
    # clear()
    # for angle in range(361):
    #
    #     while length < 250 * step:
    #
    #         fd(length)
    #         rt(angle)
    #
    #         length += step
    #     update()
    #     time.sleep(0.04 * (1+ 1-abs(angle-180)/360))
    #     pu()
    #     home()
    #     pd()
    #     lt(90)
    #     clear()
    #     length = 5

    # update()
    mainloop()
