import turtle

screen = turtle.Screen()
screen.title("Bulgaria Cities Game")

image = "bulgaria_blank_map.gif"
screen.addshape(image)
turtle.shape(image)


def get_mouse_click_coor(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()

screen.exitonclick()
