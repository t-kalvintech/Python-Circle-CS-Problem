# Create a program that randomly generates points on a graph using a rand function.
# For each point you call rand() twice, one for x-value and one for y-value.
# Then a imaginary square is drawn and the graph is in one corner of the square.
# Then a circle is drawn in the 'big' square.
# The program will try to create a formula that will estimate pi using the number of points in the circle divided by the number of points in the square or the area of the circle divided by the area of the square.
# basically it will try to estimate pi, given that you have random (0,1)
import random

def estimate_pi(n):
    num_point_circle = 0
    num_point_total = 0
    for _ in range(n):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        distance = x**2 + y**2
        if distance <= 1:
            num_point_circle += 1
        num_point_total += 1

    return 4 * num_point_circle/num_point_total
