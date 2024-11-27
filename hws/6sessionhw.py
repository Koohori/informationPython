'''import turtle as t

def polygon(n,s):
    angle = 360/n
    for i in range(n):
        t.forward(s)
        t.left(angle)

number=int(input('number of sides:'))
size=int(input('size of each side: '))

polygon(number,size)

t.done()
'''


import turtle

def circle(r):
    # Create a turtle object
    t = turtle.Turtle()

    # Set the speed of drawing (optional, you can adjust it)
    t.speed(0)


    t.penup()  # Lift pen to move to starting position
    t.goto(0, -r)  # Move to the starting point (centered at (0,0))
    t.pendown()  # Lower pen to start drawing
    t.circle(r)  # Draw the circle with radius r

    # Draw 5 concentric circles with decreasing radii
    for i in range(1, 6):
        new_radius = r - i * (r // 6)  # Decrease the radius by a fraction
        t.penup()
        t.goto(0, -new_radius)  # Move to the new starting position
        t.pendown()
        t.circle(new_radius)  # Draw the concentric scircle

    turtle.done()  # Finish drawing and show the window

# Example usage:
circle(100)
