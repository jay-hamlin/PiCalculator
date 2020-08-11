## assumes python3
import time
import math as mt

##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##
#   Calculate Pi by hand
#
#   The area of a cicle is:
#       A = Pi*r^2   --> Pi r squared.  (if r is 1 then the area = Pi)
#   The equation of a circle is:
#       r^2 = (x^2 + y^2)
#       solving for y
#       y = sqrt(r^2 - x^2)
#
#   We will calculate the area under the curve for the 1st quadrant and
#   then multiply the result by 4 to get the total area.
#   With r=1, area = Pi.
#
#   x goes from 0 to 1 in some number of slices (n)
#   We calculate the area of each slice and sum them.
#       area = width * height
#       width = r/n  (radius divided by the number of slices)
#   for height we use the average y of f(x) of the left side of the slice and f(x)
#   for the right side of the slice. This is more accurate than just picking one or the other.
#       height = (f(x-1)+f(x))/2.  ("x-1" means x of i-1)
#
##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##

##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##
#   From wikipedia, the first 50 digits of Pi are:
#       3.14159265358979323846264338327950288419716939937510
#
#  Testing results
#   slices vs. tested accuracy
#   10     - 1 decimal place  (3.10451833)
#   100    - 2 decimal places (3.14041703)
#   1000   - 4 decimal places (3.14155547)
#   10000  - 5 decimal places (3.14159148)
#   100000 - 7 decimal places (3.14159262)
#   1000000- 8 decimal places (3.141592652414)
#   10000000-10 decimal places (3.141592653553)
#
##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##

radius        = 1.0000
radiusSquared = 1.0000
slices = 1000000
index = 0

timeIn = time.time()

sliceWidth  = (radius / slices)
sliceAreaSum = 0.0000

y0 = mt.sqrt(radiusSquared - (index/slices)**2)

while(index < slices):
    index += 1
    y1 = mt.sqrt(radiusSquared - (index/slices)**2)
    sliceAreaSum += sliceWidth*(y0+y1)/2
    y0 = y1  # bump y0 ready for the next loop
    
# we have calculated 1 quadrant. multiply by 4 to get the entire circle
sliceAreaSum *= 4.0000

print(" With %d"%slices+" iterations, calculated Pi is %.12f"%sliceAreaSum)

timeOut = time.time()

print("Elapsed time= %4.4f"%(timeOut-timeIn)+" seconds")
