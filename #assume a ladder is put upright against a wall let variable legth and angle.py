#assume a ladder is put upright against a wall let variable legth and angle
#store the lenght of the ladder and the angle it form on the ground write a
#python program to compute the height reach by the ladder on the wall.
import math
l=int(input("enter the lenght"))
angle=int(input("enter the angle"))
ang_radian=math.radians(angle)
height=l*math.sin(ang_radian)
print("height",height)
