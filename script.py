import turtle
import random as r


print("*"*50)
print("대한민국 대선 레이싱: 대한민국의 운명이 달렸다!")
print("*"*50)

def start_screen():
    screen.clearscreen()
    screen.bgpic("/Users/yuniinuy/Downloads/bg_start.gif")
    screen.onkeypress(select_screen(), "space")

def select_screen():
    screen.clearscreen()
    screen.bgpic("/Users/yuniinuy/Downloads/select.gif")

def play():
    first_snale.forward(r.randint(1,15))
    second_snale.forward(r.randint(1,15))
    third_snale.forward(r.randint(1,15))
    if first_snale.pos()[0] > 450:
        print("Blue Win")
    if second_snale.pos()[0] > 450:
        print("Red Win")
    if third_snale.pos()[0] > 450:
        print("Yellow Win")
    if first_snale.pos()[0] < 450 and second_snale.pos()[0] < 450 and third_snale.pos()[0] < 450:
        turtle.ontimer(play, 100)



def play_screen():

    screen.clearscreen()
    screen.bgpic("/Users/yuniinuy/Downloads/bg.gif")
    turtle.register_shape("/Users/yuniinuy/Downloads/red_snale.gif")
    turtle.register_shape("/Users/yuniinuy/Downloads/blue_snale.gif")
    turtle.register_shape("/Users/yuniinuy/Downloads/yellow_snale.gif")  # .gif 파일 등록

    # 첫 번째 거북이 (이미지 모양)

    first_snale.shape("/Users/yuniinuy/Downloads/red_snale.gif")
    first_snale.speed(0)
    first_snale.penup()
    first_snale.goto(-500, -100)
    first_snale.setheading(0)

    # 두 번째 거북이 (기본 모양)

    second_snale.shape("/Users/yuniinuy/Downloads/blue_snale.gif")
    second_snale.speed(0)
    second_snale.penup()
    second_snale.goto(-500, 75)
    second_snale.setheading(0)

    # 세 번째 거북이 (기본 모양)

    third_snale.shape("/Users/yuniinuy/Downloads/yellow_snale.gif")
    third_snale.speed(0)
    third_snale.penup()
    third_snale.goto(-500, -300)
    third_snale.setheading(0)

    play()

def result_screen():


# 스크린 설정
screen = turtle.Screen()
screen.setup(width=1280, height=853)
screen.title("snale")
start_screen()

screen.onkey(play_screen, "space")

# 사용자 정의 이미지 등록
first_snale = turtle.Turtle()
second_snale = turtle.Turtle()
third_snale = turtle.Turtle()

screen.listen()
start_screen()
turtle.exitonclick()