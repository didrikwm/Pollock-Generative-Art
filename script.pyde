import random
import math

size_x = 1920
size_y = 1080

bg_transparency = 60

bg_color = [174, 54, 27]

colors = [
          [237, 234, 204], # White
          [237, 234, 204],
          [37, 37, 37], # Black
          [37, 37, 37],
          [37, 37, 37]         
        ]        

def setup():
    size(size_x, size_y)
    noLoop()
    
def bg(w, h, transp):
    background(bg_color[0], bg_color[1], bg_color[2])
    x_point = 0.0
    y_point = 0.0
    inc = 0.04
    
    for y in range(1, size_y):
        for x in range(1, size_x):
            gray = noise(x_point, y_point) * 255
            stroke(gray, transp)
            point(x, y)
            x_point = x_point + inc
        x_point = 0
        y_point = y_point + inc

def irregular(x_center, y_center, arcs_num, min_rad, max_rad):
    color = colors[random.randint(0, len(colors)-1)]
    angle = 0
    noStroke()
    beginShape()
    
    for i in range(1, arcs_num):
        mutator = random.randint(-3, 3) # Adds some minor variations to the color
        color_variant = [color[0] + mutator, color[1] + mutator, color[2] + mutator]
        fill(color_variant[0], color_variant[1], color_variant[2])
        
        angle = 360 * i / arcs_num
        radius = random.randint(min_rad, max_rad)
        x = x_center + radius * math.cos(angle)
        y = y_center + radius * math.sin(angle)
        curveVertex(x, y)
        
    endShape()

def lines(x_center, y_center, segments, min_weight, max_weight, radius):
    pos_x = x_center
    pos_y = y_center
    angle = random.uniform(0, 2 * math.pi)
    
    color = colors[random.randint(0, len(colors)-1)]
    mutator = random.randint(-5, 5) # Adds some minor variations to the color
    color_variant = [color[0] + mutator, color[1] + mutator, color[2] + mutator]
    opacity = random.randint(230, 255) # Minor variations in opacity
    
    for i in range(1, segments):
        next_pos_x = pos_x + math.cos(angle) * radius
        next_pos_y = pos_y + math.sin(angle) * radius
        stroke_weight = random.uniform(min_weight, max_weight)
        strokeWeight(stroke_weight)
        
        stroke(color_variant[0], color_variant[1], color_variant[2], opacity)
        
        line(pos_x, pos_y, next_pos_x, next_pos_y)
        
        if random.randint(0,4) == 0: # Adds some splashes near the lines
            noStroke()
            fill(color_variant[0], color_variant[1], color_variant[2], random.randint(230, 255))
            edge = -stroke_weight if random.randint(0,1) == 0 else stroke_weight # Takes the line thickness into account
            size = random.uniform(0.6, 7)
            ellipse(pos_x + (edge + random.uniform(-6.0, 6.0)), pos_y + (edge + random.uniform(-6.0, 6.0)), size + random.uniform(-0.8, 0.8), size + random.uniform(-0.8, 0.8))
            
        pos_x = next_pos_x
        pos_y = next_pos_y
        angle = angle + random.uniform(-0.3, 0.3)
    
def draw(): # Main    
    bg(size_x, size_y, bg_transparency) # Background
    
    for i in range(0, random.randint(size_y/8, size_y/6)): # Irregular shapes
        color = colors[random.randint(0, len(colors)-1)]
        fill(color[0], color[1], color[2])
        
        x_pos = random.randint(1, size_x)
        y_pos = random.randint(1, size_y)
        arcs = random.randint(10, 20)
        min_rad = size_x / 150
        max_rad = size_x / 30
        
        irregular(x_pos, y_pos, arcs, min_rad, max_rad)
    
    for i in range(0, random.randint(size_y/4, size_y/3)): # Lines
        x_pos = random.randint(1, size_x)
        y_pos = random.randint(1, size_y)
        segments = random.randint(size_y/10, size_x/10) # In reality this determines the length of each line
        base_weight = random.uniform(0.5, 15) # Lines will have varying weight,
        min_weight = base_weight * 0.5 # and each line will have small variations near its weight
        max_weight = base_weight * 1.5
        radius = 10
        
        if random.randint(0,3) == 0: # Ensures some thin lines that are more even in thickness
            min_weight, max_weight = 2, 4
            
        lines(x_pos, y_pos, segments, min_weight, max_weight, radius)
    
def keyPressed():
    try:
        key_int = int(key)
        if key_int in range(0, 9):
            save("artwork" + key + ".jpg")
    except:
        print("Please enter a number.")
    
        
