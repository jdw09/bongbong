import turtle
import random as r
import time


print("*"*50)
print("대한민국 대선 레이싱: 대한민국의 운명이 달렸다!")
print("*"*50)

selected_bongbong = "None"
end_flag = False
point = 0

def exit_game():
    print("게임이 정상 종료되었습니다.")
    exit()

def restart():
    global end_flag
    end_flag = False
    start_screen()

def gotoplay(bongbong):
    global selected_bongbong
    selected_bongbong = bongbong
    play_screen()

def start_screen():
    screen.clearscreen()
    screen.bgpic("/Users/yuniinuy/Downloads/bg_start.gif")
    time.sleep(2)
    screen.onkeypress(select_screen, "space")
    screen.onkeypress(exit_game, "x")

def select_screen():
    screen.clearscreen()
    screen.bgpic("/Users/yuniinuy/Downloads/select.gif")
    screen.onkeypress(lambda: gotoplay("Blue"), "1")
    screen.onkeypress(lambda: gotoplay("Red"), "2")
    screen.onkeypress(lambda: gotoplay("Yellow"), "3")

def play():
    first_snale.forward(r.randint(1,15))
    second_snale.forward(r.randint(1,15))
    third_snale.forward(r.randint(1,15))
    global end_flag
    if first_snale.pos()[0] > 450:
        print("Blue Win")
        end_flag = True
        result_screen("Blue")
    elif second_snale.pos()[0] > 450:
        print("Red Win")
        end_flag = True
        result_screen("Red")
    elif third_snale.pos()[0] > 450:
        print("Yellow Win")
        end_flag = True
        result_screen("Yellow")
    if not end_flag:
        turtle.ontimer(play, 100)

def turtle_setup():
    global first_snale, second_snale, third_snale, text_turtle
    first_snale = turtle.Turtle()
    second_snale = turtle.Turtle()
    third_snale = turtle.Turtle()
    text_turtle = turtle.Turtle()

    first_snale.shape("/Users/yuniinuy/Downloads/blue_snale.gif")
    first_snale.speed(0)
    first_snale.penup()
    first_snale.goto(-500, 75)
    first_snale.setheading(0)
    first_snale.showturtle()

    second_snale.shape("/Users/yuniinuy/Downloads/red_snale.gif")
    second_snale.speed(0)
    second_snale.penup()
    second_snale.goto(-500, -100)
    second_snale.setheading(0)
    second_snale.showturtle()

    third_snale.shape("/Users/yuniinuy/Downloads/yellow_snale.gif")
    third_snale.speed(0)
    third_snale.penup()
    third_snale.goto(-500, -300)
    third_snale.setheading(0)
    third_snale.showturtle()

    text_turtle.hideturtle()
    text_turtle.penup()
    text_turtle.color("white")

def play_screen():
    screen.clearscreen()
    screen.bgpic("/Users/yuniinuy/Downloads/bg.gif")
    turtle.register_shape("/Users/yuniinuy/Downloads/red_snale.gif")
    turtle.register_shape("/Users/yuniinuy/Downloads/blue_snale.gif")
    turtle.register_shape("/Users/yuniinuy/Downloads/yellow_snale.gif")  # .gif 파일 등록

    turtle_setup()
    play()

def result_screen(win_color):
    global point
    added_point = point

    if win_color == "Blue":
        screen.bgpic("/Users/yuniinuy/Downloads/result_blue.gif")

    elif win_color == "Red":
        screen.bgpic("/Users/yuniinuy/Downloads/result_red.gif")

    elif win_color == "Yellow":
        screen.bgpic("/Users/yuniinuy/Downloads/result_yellow.gif")

    first_snale.shape("/Users/yuniinuy/Downloads/blue_snale.gif")
    second_snale.shape("/Users/yuniinuy/Downloads/red_snale.gif")
    third_snale.shape("/Users/yuniinuy/Downloads/yellow_snale.gif")

    if selected_bongbong == "Blue":
        first_snale.goto(-250, -50)
        second_snale.hideturtle()
        third_snale.hideturtle()
    elif selected_bongbong == "Red":
        first_snale.hideturtle()
        second_snale.goto(-250, -50)
        third_snale.hideturtle()
    elif selected_bongbong == "Yellow":
        first_snale.hideturtle()
        second_snale.hideturtle()
        third_snale.goto( -250, -50)

    print(selected_bongbong)

    text_turtle.goto(-350, -350)
    text_turtle.write(f"{point}점", font=("Arial", 30, "bold"))

    if selected_bongbong == win_color:
        earn_point = r.randint(100, 1000)
        added_point += earn_point

        text_turtle.goto(80, -350)
        text_turtle.write(f"{earn_point}점", font=("Arial", 30, "bold"))
        print("You Win! you earned ", earn_point, " points")
    else:
        lost_point = r.randint(-1000, -100)
        added_point += lost_point

        text_turtle.goto(80, -350)
        text_turtle.write(f"{lost_point}점", font=("Arial", 30, "bold"))
        print("You Lost! you lost ", lost_point, " points")

    text_turtle.goto(450, -350)
    text_turtle.write(f"{added_point}점", font=("Arial", 30, "bold"))

    point = added_point

    screen.onkeypress(exit, "x")
    screen.onkeypress(restart, "space")



screen = turtle.Screen()
screen.setup(width=1280, height=853)
screen.title("snale")


first_snale = turtle.Turtle()
second_snale = turtle.Turtle()
third_snale = turtle.Turtle()
text_turtle = turtle.Turtle()

start_screen()
screen.listen()
