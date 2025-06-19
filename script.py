import turtle
import random as r
import time
import hashlib
import pygame

userid = ""
isPlaying = False

def hash_password(password): #비밀번호 암호화용 함수, hashlib 사용
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return hashed_password

def save_user(username, password): #회원가입 함수
    password = hash_password(password) #비밀번호 암홍화
    new_user = username + ":" + password + "\n" #저장 형식대로 수정
    with open("/Users/yuniinuy/PyCharmMiscProject/user.pkl", "a") as f:
        f.write(new_user) #사용자 저장
    with open("/Users/yuniinuy/PyCharmMiscProject/gamedata.data", "a") as gamedata:
        gamedata.write(f"{username}:0\n") #게임 데이터 초기값 설정

def login(): #로그인 함수
    print("\nLogin")
    username = input("ID: ")
    password = input("PW: ")
    password = hash_password(password) #저장된 비밀번호화 비교하기 위해 암호화
    with open("/Users/yuniinuy/PyCharmMiscProject/user.pkl", "r") as f:
        users = f.read().split("\n") #user.pkl 읽어오기
    for i in users:
        user = list(i.split(":"))
        if username == user[0] and password == user[1]: #만약 user와 password가 저장된 데이터와 같다면
            print("로그인 성공")
            global userid
            userid = user[0] #현재 로그인된 유저 아이디 저장
            f.close()
            return
    print("로그인 실패") #로그인 실패 시
    login_logic() #초기화면으로 돌아감

def register(): #회원가입 함수
    print("\nRegister")
    username = input("ID: ")
    is_duplicate = False
    with open("/Users/yuniinuy/PyCharmMiscProject/user.pkl", "r") as f:
        users = f.read().split("\n") #user.pkl읽어오기
    for i in users:
        user = list(i.split(":"))
        if username == user[0]: #만약 username이 user.pkl안에 있다면(이미 등록된 사용자가 있다면)
            print("이미 등록된 사용자 입니다")
            is_duplicate = True #중복 플래그 True
    f.close()
    if not is_duplicate:#중복이 아니라면
        password = input("PW: ")
        save_user(username, password) #데이터 저장
        login()
    else: #중복이면
        login_logic() #초기화면

def login_logic():
    print("1. 로그인\n2. 회원가입\n3. 종료")
    select = int(input("Select: ")) #선택(로그인, 회원가입, 종료)
    if select == 1:
        login()
    elif select == 2:
        register()
    else:
        exit_game()

def get_point(): #로컬 데이터에서 포인트 가져오는 함수
    with open("/Users/yuniinuy/PyCharmMiscProject/gamedata.data", "r") as data:
        for i in data: #테이터에서
            user, point = i.split(":")
            if user == userid: #유저 아이디에 맞는 데이터 찾고
                return int(point) #변수에 저장
        return "사용자 데이터가 없습니다." #데이터가 없다면 오류메시지 리턴

def save_point(point): #포인트 저장 함수
    with open("/Users/yuniinuy/PyCharmMiscProject/gamedata.data", "r") as data:
        lines = data.readlines() #전체 파일 읽어오기
    for i in range(len(lines)):
        if lines[i].split(":")[0] == userid: #사용자에 해당하는 라인 찾으면
            lines[i] = userid + ":" + str(point) + "\n" #수정
    data.close()

    with open("/Users/yuniinuy/PyCharmMiscProject/gamedata.data", "w") as data:
        data.writelines(lines) #수정한 데이터로 덮어씌우기

def exit_game(): #게임 종료 함수
    print("게임이 정상 종료되었습니다.")
    exit()

def restart(): #재시작 함수
    global end_flag
    global isPlaying
    end_flag = False
    isPlaying = False
    start_screen()

def gotoplay(bongbong): #선택된 봉봉을 저장하고 다음 화면을 띄우는 함수
    global isPlaying
    if isPlaying:
        return
    else:
        isPlaying = True
    global selected_bongbong
    selected_bongbong = bongbong
    play_screen()

def start_screen(): #초기화면 함수
    screen.clearscreen()
    screen.bgpic("/Users/yuniinuy/Downloads/bg_start.gif")
    time.sleep(2)
    screen.onkeypress(select_screen, "space")
    screen.onkeypress(exit_game, "x")

def select_screen(): #봉봉 선택화면 함수
    screen.clearscreen()
    screen.bgpic("/Users/yuniinuy/Downloads/select.gif")
    screen.onkeypress(lambda: gotoplay("Blue"), "1")
    screen.onkeypress(lambda: gotoplay("Red"), "2")
    screen.onkeypress(lambda: gotoplay("Yellow"), "3")

def play(): #플레이 함수
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

def turtle_setup(): #Turtle(봉봉) 초기 세팅용 함수
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

def play_screen(): #플레이 화면 세팅 화면
    screen.clearscreen()
    screen.bgpic("/Users/yuniinuy/Downloads/bg.gif")
    turtle.register_shape("/Users/yuniinuy/Downloads/red_snale.gif")
    turtle.register_shape("/Users/yuniinuy/Downloads/blue_snale.gif")
    turtle.register_shape("/Users/yuniinuy/Downloads/yellow_snale.gif")  # .gif 파일 등록

    turtle_setup()
    play()

def result_screen(win_color): #결과 화면 함수
    global point
    added_point = point

    #이긴 봉봉에 따른 배경 설정
    if win_color == "Blue":
        screen.bgpic("/Users/yuniinuy/Downloads/result_blue.gif")

    elif win_color == "Red":
        screen.bgpic("/Users/yuniinuy/Downloads/result_red.gif")

    elif win_color == "Yellow":
        screen.bgpic("/Users/yuniinuy/Downloads/result_yellow.gif")

    first_snale.shape("/Users/yuniinuy/Downloads/blue_snale.gif")
    second_snale.shape("/Users/yuniinuy/Downloads/red_snale.gif")
    third_snale.shape("/Users/yuniinuy/Downloads/yellow_snale.gif")

    #선택한 봉봉을 띄우기
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

    point = added_point #포인트 업데이트
    save_point(point) #포인트 저장

    screen.onkeypress(exit_game, "x") #x == 종료함수 실행
    screen.onkeypress(restart, "space") #space == 재시작 함수 실행

def play_sound(file, num = -1):
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(num)

def stop_bgm():
    pygame.mixer.music.stop()

#__________main___________

file = "/Users/yuniinuy/Downloads/dadadametenshi.mp3"


print("*"*50)
print("대한민국 대선 레이싱: 대한민국의 운명이 달렸다!")
print("*"*50)

login_logic()  #로그인 로직 실행

selected_bongbong = "None" #초기값 세팅
end_flag = False
point = get_point()

screen = turtle.Screen() #스크린 세팅
screen.setup(width=1280, height=853)
screen.title("snale")


first_snale = turtle.Turtle() #터틀 세팅
second_snale = turtle.Turtle()
third_snale = turtle.Turtle()
text_turtle = turtle.Turtle()

play_sound(file)
start_screen() #스크린 띄우기
screen.listen() #키보드 대기