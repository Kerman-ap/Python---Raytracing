# Raytracer in python

import matplotlib as plt
import numpy as np
import random

def normalise(vector): 
    return vector / np.linalg.norm(vector)

def castrays(width, height, triangles):
    camera_origin = np.array([0, 0, 0])
    
    for y in range(height):
        for x in range(width):
            pass

def getmidpoint(triangle):
    return np.array([(triangle[0][0] + triangle[1][0] + triangle[2][0])/3, (triangle[0][1] + triangle[1][1] + triangle[2][1])/3, (triangle[0][2] + triangle[1][2] + triangle[2][2])/3,])

def createtriangle(x1, y1, z1, x2, y2, z2, x3, y3, z3):
    vertex1 = np.array([x1, y1, z1])
    vertex2 = np.array([x2, y2, z2])
    vertex3 = np.array([x3, y3, z3])
    return np.array([vertex1, vertex2, vertex3])

def randomtriangles(n):
    triangles = []
    for i in range(n):
        triangles.append(createtriangle(random.randint(-10, 10), random.randint(-10, 10), random.randint(-10, 10), random.randint(-10, 10), random.randint(-10, 10), random.randint(-10, 10), random.randint(-10, 10), random.randint(-10, 10), random.randint(-10, 10)))
    return np.array(triangles)

triangles = randomtriangles(1)

print(triangles)
print(getmidpoint(triangles[0]))


# The dot product of two perpendicular vectors is always equal to 0
# P = O + tR
#, Where P is the point of intersection, O is the ray origin, t is the distance from the ray origin to the point of intersection, and R is the direction of the ray.