from p5 import *

data = []
m = 1
d = 0


def draw():
    size(600, 600)
    background(10)

    if len(data) > 1:
        linear_regression()

    for i in data:
        fill(255)
        stroke(255)
        x = i[0]
        y = i[1]
        x = remap(x, (0, 1), (0, 600))
        y = remap(y, (0, 1), (600, 0))
        circle((x, y), 10)


def linear_regression():
    xsum = 0
    ysum = 0

    for i in data:
        xsum = xsum + i[0]
        ysum = ysum + i[1]

    xmean = xsum / len(data)
    ymean = ysum / len(data)

    numerator = 0
    denom = 0

    for i in data:
        xd = i[0]
        yd = i[1]
        numerator = numerator + (xd-xmean)*(yd-ymean)
        denom = denom + (xd-xmean) * (xd-xmean)

    m = numerator / denom
    print("slope", m)
    d = ymean - (m * xmean)

    x1 = 0
    x2 = 1
    y1 = (m * x1) + d
    y2 = (m * x2) + d

    x1 = remap(x1, (0, 1), (0, 600))
    x2 = remap(x2, (0, 1), (0, 600))
    y1 = remap(y1, (0, 1), (600, 0))
    y2 = remap(y2, (0, 1), (600, 0))
    print('y1 , y2 ,d',y1,y2,d)
    line((x1, y1), (x2, y2))


def mouse_pressed(event):
    x= int(event.x)
    y= int(event.y)

    x = remap(x, (0, 600), (0, 1))
    y = remap(y, (0, 600), (1, 0))

    data.append([x, y])

    linear_regression()


if __name__ == '__main__':
    run()
