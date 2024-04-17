import turtle
import pandas

screen = turtle.Screen()
screen.title("Bulgaria Cities Game")

image = "bulgaria_blank_map.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(1.0, 1.0)

data = pandas.read_csv("cities.csv")
all_cities = data.city.to_list()
#print(len(all_cities))
guessed_cities = []

while len(guessed_cities) < 27:
    answer_city = screen.textinput(title=f"{len(guessed_cities)}/27 Cities Correct",
                                   prompt="What's another city's name?").title()
    #print(answer_city)
    if answer_city == "Exit":
        missing_cities = [city for city in all_cities if city not in guessed_cities]
        # for city in all_cities:
        #     if city not in guessed_cities:
        #         missing_cities.append(city)
        #print(missing_cities)
        new_data = pandas.DataFrame(missing_cities)
        new_data.to_csv("cities_to_learn.csv")
        break

    if answer_city in all_cities:
        guessed_cities.append(answer_city)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        city_data = data[data.city == answer_city]
        t.goto(int(city_data.x), int(city_data.y))
        t.write(city_data.city.item())











#def get_mouse_click_coor(x, y):
    #print(x, y)


#turtle.onscreenclick(get_mouse_click_coor)

#turtle.mainloop()

#screen.exitonclick()
