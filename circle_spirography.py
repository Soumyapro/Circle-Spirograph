import turtle as tur

# set the backgound color black
tur.bgcolor('black')
# use the line thickness 2
tur.pensize(2)

tur.speed(0)


def draw_cir_spiro(num):

    for i in range(6):

        for rang in ('red', 'magenta', 'blue',
                     'cyan', 'green', 'white',
                     'yellow'):

            tur.color(rang)
            # num is the radius of the circle
            tur.circle(num)
            tur.right(10)

    tur.hideturtle()  # making the turtle invisible


draw_cir_spiro(120)
