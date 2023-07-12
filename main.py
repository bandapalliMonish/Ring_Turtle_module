import turtle as t
import random
tim = t.Turtle()
t.colormode(255)
directions = [0, 90, 180, 270]
# tim.pensize(10)
tim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    r_color = (r, g, b)
    return r_color


def draw_spirograph(size):
    no_of_circles = int(360 / size)
    for turns in range(no_of_circles):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size)


draw_spirograph(5)


# for turns in range(100):
#     tim.color(random_color())
#     tim.forward(50)
#     tim.setheading(random.choice(directions))

# for shape in range(3, 11):
#     for _ in range(shape):
#         t.pensize(10)
#         t.color(choice(colors))
#         t.forward(50)
#         t.right(360 / shape)

screen = t.Screen()
screen.exitonclick()
