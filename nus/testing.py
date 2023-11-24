import math
import time as t

width = 10
position = 0 # 1 2 3 4
breite = 5
for timer in range(50):
    zahl =  (-1)**(math.floor(timer/breite))
    print("timer", timer, "zahl", zahl)
# breite = 0
# x = 0
x = 0
y = 0
def ball(x,y):
    pass
# x = x (-1)**(math.floor(timer/breite))

if(x<200):
    ball(x, y)
if(200 <= x <= 400):
    ball(200-x, y)
if(400 < x < 500):
    ball(x-400, y)
if(x > 500):
    ball(100, y)

x = function(timer)