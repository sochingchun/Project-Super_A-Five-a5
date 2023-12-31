from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import winsound
#show-window2--------------------------

def main():
    global window,stop_to_stop
    window.destroy()
    window = Tk()
    window.title('window2')
    app_width = window.winfo_screenwidth()
    app_height = window.winfo_screenheight()
    window.geometry(f'{app_width}x{app_height}')
    frame = Frame(window, width=app_width, height=app_height)
    frame.pack()
    canvas = Canvas(frame, width=app_width, height=app_height)
    canvas.pack()
    bg_image = Image.open("image/tree2.png")
    bg_image = bg_image.resize((app_width, app_height))
    background = ImageTk.PhotoImage(bg_image)
    canvas.create_image(0, 0, image=background, anchor=NW)
    canvas.create_text(650, 170, text="Super A Five", fill="blue", font=('DRAGON HUNTER', 50))

    button_back = Button(canvas, text="Play",font=90, command=window3, bg='blue',border=25)
    button_back.pack()
    button_back.place(x=550, y=250, width=250)
    
    button_back2 = Button(canvas, text="Display",font=90 ,command=Display, bg='blue',border=25)
    button_back2.pack()
    button_back2.place(x=550, y=370, width=250)

    button_back3 = Button(canvas, text="Story",font=90, command=show_story, bg='blue',border=25)
    button_back3.pack()
    button_back3.place(x=550, y=490, width=250)
    def play():
        winsound.PlaySound('./sound/8bit-music-for-game-68698.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
    play()
    def stop_sound():
        winsound.PlaySound(None, winsound.SND_PURGE)
    def stop_to_stop():
        stop_sound()
    window.mainloop()

#show-window3--------------------------------------

def window3():
    global window
    window.destroy() 
    window = Tk()
    window.title('av')
    app_width = window.winfo_screenwidth()
    app_height = window.winfo_screenheight()
    window.geometry(f'{app_width}x{app_height}')
    frame = Frame(window, width=app_width, height=app_height)
    frame.pack()
    canvas = Canvas(frame, width=app_width, height=app_height)
    canvas.pack()
    bg_image = Image.open("image/tree.png")
    bg_image = bg_image.resize((app_width, app_height))
    background = ImageTk.PhotoImage(bg_image)
    canvas.create_image(0, 0, image=background, anchor=NW)
    button_back = Button(canvas, text="Back",font=40, command=main, bg='red',border=10)
    button_back.pack()
    button_back.place(x=50, y=50, width=90)

    button_back = Button(canvas, text="Hard",font=90, command=Hard, bg='blue',border=25)
    button_back.pack()
    button_back.place(x=550, y=220, width=250)
    
    button_back2 = Button(canvas, text="Normal",font=90, command=Normal, bg='blue',border=25)
    button_back2.pack()
    button_back2.place(x=550, y=340, width=250)

    button_back3 = Button(canvas, text="Easy",font=90, command=Easy, bg='blue',border=25)
    
    button_back3.pack()
    button_back3.place(x=550, y=460, width=250)
    # window.after(1000, window4)
    window.mainloop()


#show-window4-----------------------------------------

def window4():
    global window
    window.destroy() 
    windows4 = Tk()
    windows4.title('v')
    app_width = windows4.winfo_screenwidth()
    app_height = windows4.winfo_screenheight()
    windows4.geometry(f'{app_width}x{app_height}')
    frame = Frame(windows4, width=app_width, height=app_height)
    frame.pack()
    canvas = Canvas(frame, width=app_width, height=app_height)
    canvas.pack()
    bg_image = Image.open("image/window4.png")
    bg_image = bg_image.resize((app_width, app_height))
    background = ImageTk.PhotoImage(bg_image)
    canvas.create_image(0, 0, image=background, anchor=NW)
    windows4.mainloop()

# show window for button story------------

def show_story():
    global window
    window.destroy() 
    window = Tk()
    window.title('show story')
    app_width = window.winfo_screenwidth()
    app_height = window.winfo_screenheight()
    window.geometry(f'{app_width}x{app_height}')
    frame = Frame(window, width=app_width, height=app_height)
    frame.pack()
    canvas = Canvas(frame, width=app_width, height=app_height)
    canvas.pack()
    bg_image = Image.open("image/story.png")
    bg_image = bg_image.resize((app_width, app_height))
    background = ImageTk.PhotoImage(bg_image)
    canvas.create_image(0, 0, image=background, anchor=NW)
    button_back = Button(canvas, text="Back",font=40, command=main, bg='red',border=10)
    button_back.pack()
    button_back.place(x=50, y=50, width=90)    
    cteat_img = Image.open("image/Player.png")
    cteat_img = cteat_img.resize((300, 300))
    background1 = ImageTk.PhotoImage(cteat_img)
    canvas.create_image(180, 350, image=background1, anchor=NW)
    
    window.mainloop()


#--show window for display-----------

def Display():
    global window
    window.destroy() 
    window = Tk()
    window.title('show story')
    app_width = window.winfo_screenwidth()
    app_height = window.winfo_screenheight()
    window.geometry(f'{app_width}x{app_height}')
    frame = Frame(window, width=app_width, height=app_height)
    frame.pack()
    canvas = Canvas(frame, width=app_width, height=app_height)
    canvas.pack()
    bg_image = Image.open("image/display.png")
    bg_image = bg_image.resize((app_width, app_height))
    background = ImageTk.PhotoImage(bg_image)
    canvas.create_image(0, 0, image=background, anchor=NW)
    button_back = Button(canvas, text="Back",font=40, command=main, bg='red',border=10)
    button_back.pack()
    button_back.place(x=50, y=50, width=90)    

    window.mainloop()

#Easy Game--------------------------------

def Easy():
    global window,x,position_enemy2,y,position_enemy3,a,position_enemy4,b,player,keyPressed
    window.destroy() 
    window = Tk()
    window.title('Easy')
    app_width = window.winfo_screenwidth()
    app_height = window.winfo_screenheight()

    window.geometry(f'{app_width}x{app_height}')
    frame = Frame(window, width=app_width, height=app_height)
    frame.pack()
    canvas = Canvas(frame, width=app_width, height=app_height)
    canvas.pack()
    #-------------hero----------
    keyPressed = []
    SPEED = 7 
    TIME = 10
    GRAVITY_FORCE=9
    def check_movement(dx=0, dy=0):
            ball_coords = canvas.bbox(player)
            new_x1 = ball_coords[0] + dx
            new_y1 = ball_coords[1] + dy
            new_x2 = ball_coords[2] + dx
            new_y2 = ball_coords[3] + dy
            overlapping_objects = canvas.find_overlapping(new_x1, new_y1, new_x2, new_y2)
            for wall_id in canvas.find_withtag("wall"):
                if wall_id in overlapping_objects:
                    return False
            return True

    def start_move(event):
            if event.keysym not in keyPressed:
                print(event.keysym)
                keyPressed.append(event.keysym)
                if len(keyPressed) == 1:
                    move()

    def stop_move(event):
            global keyPressed
            if event.keysym in keyPressed:
                keyPressed.remove(event.keysym)

    def jump(force):
            if force > 0:
                if check_movement(0, -force):
                    canvas.move(player, 0, -force)
            window.after(TIME, jump, force - 1)

    def move():
            if not keyPressed == []:
                x = 0
                if "Left" in keyPressed:
                    x = -SPEED
                    #add
                    canvas.itemconfig(player,image=hero3)
                if "Right" in keyPressed:
                    x = SPEED
                    canvas.itemconfig(player,image=play_1)
                if check_movement(x, 0):
                    canvas.move(player, x, 0)
                if "space" in keyPressed and not check_movement(0, GRAVITY_FORCE):
                    jump(30)
                window.after(TIME, move)

    def gravity():
        if check_movement(0, GRAVITY_FORCE):
            canvas.move(player, 0, GRAVITY_FORCE)
        window.after(TIME, gravity)
    bg_image = Image.open("image/bg.png")
    bg_image = bg_image.resize((app_width, app_height))
    background = ImageTk.PhotoImage(bg_image)
    canvas.create_image(0, 0, image=background, anchor=NW)
    #add more
    hero_4 = Image.open("image/image 16.png")
    hero_4 = hero_4.resize((40, 40))
    hero3 = ImageTk.PhotoImage(hero_4)
    button_back = Button(canvas, text="Back",font=40, command=window3, bg='red',border=10)
    button_back.pack()
    button_back.place(x=50, y=50, width=90)

    bg_image = Image.open("image/bg.png")
    bg_image = bg_image.resize((app_width, app_height))
    background = ImageTk.PhotoImage(bg_image)
    canvas.create_image(0, 0, image=background, anchor=NW)
    button_back = Button(canvas, text="Back",font=40, command=window3, bg='red',border=10)
    button_back.pack()
    button_back.place(x=50, y=50, width=90)    
    # ---------add Wall of window4------   
    canvas.create_rectangle(0, 630, 400, 810, fill="black", tags="wall")
    canvas.create_rectangle(0, 0, 20, 810, fill="black", tags="wall")
    canvas.create_rectangle(0, 0, 1400, 20, fill="black", tags="wall")
    canvas.create_rectangle(1250, 0, 1300, 1200, fill="black", tags="wall")
    canvas.create_rectangle(500, 630, 1536, 810, fill="black", tags="wall")
    canvas.create_rectangle(500, 530, 550, 810, fill="black", tags="wall")
    canvas.create_rectangle(600, 570, 550, 810, fill="black", tags="wall")
    canvas.create_rectangle(650, 595, 550, 810, fill="black", tags="wall")
    canvas.create_rectangle(400, 530, 350, 810, fill="black", tags="wall")
    canvas.create_rectangle(400, 570, 300, 810, fill="black", tags="wall")
    canvas.create_rectangle(400, 600, 250, 810, fill="black", tags="wall")

    # -----add wall 2-------
    canvas.create_rectangle(400, 350, 200, 380, fill="black", tags="wall")
    canvas.create_rectangle(900, 350, 800, 380, fill="black", tags="wall")
    canvas.create_rectangle(1000, 470, 750, 440, fill="black", tags="wall")
    canvas.create_rectangle(1100, 550, 700, 520, fill="black", tags="wall")

    # -------add wall the end--------

    canvas.create_rectangle(1400, 120, 1000, 90, fill="black", tags="wall")
    canvas.create_rectangle(980, 190, 850, 160, fill="black", tags="wall")


    canvas.create_rectangle(400, 350, 200, 380, fill="black", tags="wall")
    canvas.create_rectangle(600, 320, 450, 290, fill="black", tags="wall")
    canvas.create_rectangle(730, 260, 640, 230, fill="black", tags="wall")
    canvas.create_rectangle(780, 320, 750, 290, fill="black", tags="wall")
    canvas.create_rectangle(810, 210, 780, 180, fill="black", tags="wall")
    canvas.create_rectangle(200, 310, 100, 280, fill="black", tags="wall")
    #-----------hero-----------
    player_left = Image.open("image/hero.png")
    player_left = player_left.resize((50, 50))
    play_1 = ImageTk.PhotoImage(player_left)
    player = canvas.create_image(80, 500, image=play_1, anchor=NW) 
    gravity()                     
    window.bind("<Key>", start_move)
    window.bind("<KeyRelease>", stop_move)

    # -----------add key----------
    image4 = Image.open('./image/key.png')
    imageTk4 = ImageTk.PhotoImage(image4)
    canvas.create_image(795, 152,image=imageTk4)

    # -------------add heart-------------
    image5 = Image.open('./image/heart.png')
    imageTk5 = ImageTk.PhotoImage(image5)
    canvas.create_image(625, 50,image=imageTk5)
    #-----------enemy-----------
    enemy1 = Image.open("image/enemy.png")
    enemy1 = enemy1.resize((70, 70))
    background1 = ImageTk.PhotoImage(enemy1)
    position_enemy1=canvas.create_image(180, 300, image=background1, anchor=NW)

    x = 3
    def movebird1():
        global x

        canvas.move(position_enemy1, x, 0)

        (leftPos, topPos, rightPos, bottomPos) = canvas.bbox(position_enemy1)
        if leftPos <= 180 or rightPos >= 410:
            x = -x
        print(x)
        canvas.after(30, movebird1)
    canvas.after(30, movebird1)


    enemy2 = Image.open("image/enemy.png")
    enemy2 = enemy2.resize((70, 70))
    background2 = ImageTk.PhotoImage(enemy2)
    position_enemy2=canvas.create_image(630, 580, image=background2, anchor=NW)
    y=3
    def movebird2():
        global y

        canvas.move(position_enemy2, y, 0)

        (leftPos, topPos, rightPos, bottomPos) = canvas.bbox(position_enemy2)
        if leftPos <= 630 or rightPos >= 1250:
            y = -y
        print(y)
        canvas.after(30, movebird2)
    canvas.after(30, movebird2)


    enemy2 = Image.open("image/enemy.png")
    enemy2 = enemy2.resize((70, 70))
    background3 = ImageTk.PhotoImage(enemy2)
    position_enemy3=canvas.create_image(730, 390, image=background3, anchor=NW)
    a=3
    def movebird3():
        global a

        canvas.move(position_enemy3, a, 0)

        (leftPos, topPos, rightPos, bottomPos) = canvas.bbox(position_enemy3)
        if leftPos <= 730 or rightPos >= 1020:
            a = -a
        print(a)
        canvas.after(30, movebird3)
    canvas.after(30, movebird3)



    enemy3 = Image.open("image/enemy.png")
    enemy3 = enemy3.resize((70, 70))
    background4 = ImageTk.PhotoImage(enemy3)
    position_enemy4=canvas.create_image(830, 110, image=background4, anchor=NW)
    b=3
    def movebird4():
        global b

        canvas.move(position_enemy4, b, 0)

        (leftPos, topPos, rightPos, bottomPos) = canvas.bbox(position_enemy4)
        if leftPos <= 830 or rightPos >= 1000:
            b = -b
        print(b)
        canvas.after(40, movebird4)
    canvas.after(30, movebird4)

    
    # --------add door--------

    image = Image.open('./image/door.png')
    imageTk = ImageTk.PhotoImage(image)
    canvas.create_image(1220, 59,image=imageTk)

    # ----------add coint -------

    
    image2 = Image.open('./image/coint.png')
    imageTk2 = ImageTk.PhotoImage(image2)
    canvas.create_image(1050, 69,image=imageTk2)
    canvas.create_image(169, 259,image=imageTk2)
    canvas.create_image(129, 259,image=imageTk2)
    canvas.create_image(529, 268,image=imageTk2)
    canvas.create_image(759, 500,image=imageTk2)
    canvas.create_image(859, 500,image=imageTk2)
    canvas.create_image(959, 500,image=imageTk2)
    canvas.create_image(1059, 500,image=imageTk2)
    stop_to_stop()



    window.mainloop()

    

#Normal Game--------------------------------

def Normal():
    global window,c,position_enemy6,d,position_enemy7,e,position_enemy8,f,player,keyPressed
    window.destroy() 
    window = Tk()
    window.title('Normal')
    app_width = window.winfo_screenwidth()
    app_height = window.winfo_screenheight()
    window.geometry(f'{app_width}x{app_height}')
    frame = Frame(window, width=app_width, height=app_height)
    frame.pack()
    canvas = Canvas(frame, width=app_width, height=app_height)
    canvas.pack()
    #------------horo-normal----------
    keyPressed = []
    SPEED = 7 
    TIME = 10
    GRAVITY_FORCE=9
    def check_movement(dx=0, dy=0):
            ball_coords = canvas.bbox(player)
            new_x1 = ball_coords[0] + dx
            new_y1 = ball_coords[1] + dy
            new_x2 = ball_coords[2] + dx
            new_y2 = ball_coords[3] + dy
            overlapping_objects = canvas.find_overlapping(new_x1, new_y1, new_x2, new_y2)
            for wall_id in canvas.find_withtag("wall"):
                if wall_id in overlapping_objects:
                    return False
            return True

    def start_move(event):
            if event.keysym not in keyPressed:
                print(event.keysym)
                keyPressed.append(event.keysym)
                if len(keyPressed) == 1:
                    move()

    def stop_move(event):
            global keyPressed
            if event.keysym in keyPressed:
                keyPressed.remove(event.keysym)

    def jump(force):
            if force > 0:
                if check_movement(0, -force):
                    canvas.move(player, 0, -force)
            window.after(TIME, jump, force - 1)

    def move():
            if not keyPressed == []:
                x = 0
                if "Left" in keyPressed:
                    x = -SPEED
                    #add
                    canvas.itemconfig(player,image=hero3)
                if "Right" in keyPressed:
                    x = SPEED
                    canvas.itemconfig(player,image=play_2)
                if check_movement(x, 0):
                    canvas.move(player, x, 0)
                if "space" in keyPressed and not check_movement(0, GRAVITY_FORCE):
                    jump(30)
                window.after(TIME, move)

    def gravity():
        if check_movement(0, GRAVITY_FORCE):
            canvas.move(player, 0, GRAVITY_FORCE)
        window.after(TIME, gravity)
    bg_image = Image.open("image/bg.png")
    bg_image = bg_image.resize((app_width, app_height))
    background = ImageTk.PhotoImage(bg_image)
    canvas.create_image(0, 0, image=background, anchor=NW)
    #add more
    hero_4 = Image.open("image/image 16.png")
    hero_4 = hero_4.resize((40, 40))
    hero3 = ImageTk.PhotoImage(hero_4)
    button_back = Button(canvas, text="Back",font=40, command=window3, bg='red',border=10)
    button_back.pack()
    button_back.place(x=50, y=50, width=90)

    bg_image = Image.open("image/normal.png")
    bg_image = bg_image.resize((app_width, app_height))
    background = ImageTk.PhotoImage(bg_image)
    canvas.create_image(0, 0, image=background, anchor=NW)
    button_back = Button(canvas, text="Back",font=40, command=window3, bg='red',border=10)
    button_back.pack()
    button_back.place(x=50, y=50, width=90)    


     # ---------add Wall of window4------   
    canvas.create_rectangle(150, 630, 0, 810, fill="black", tags="wall")
    canvas.create_rectangle(0, 0, 20, 810, fill="black", tags="wall")
    canvas.create_rectangle(0, 0, 1400, 20, fill="black", tags="wall")
    canvas.create_rectangle(1250, 0, 1300, 1200, fill="black", tags="wall")
    canvas.create_rectangle(800, 630, 400, 810, fill="black", tags="wall")

    canvas.create_rectangle(450, 530, 400, 810, fill="black", tags="wall")
    canvas.create_rectangle(500, 570, 450, 810, fill="black", tags="wall")
    canvas.create_rectangle(550, 595, 500, 810, fill="black", tags="wall")

    canvas.create_rectangle(300, 530, 250, 810, fill="black", tags="wall")
    canvas.create_rectangle(300, 570, 200, 810, fill="black", tags="wall")
    canvas.create_rectangle(300, 600, 150, 810, fill="black", tags="wall")

    canvas.create_rectangle(900, 530, 850, 810, fill="black", tags="wall")
    canvas.create_rectangle(900, 570, 800, 810, fill="black", tags="wall")
    canvas.create_rectangle(800, 600, 750, 810, fill="black", tags="wall")


    canvas.create_rectangle(1050, 530, 1000, 810, fill="black", tags="wall")
    canvas.create_rectangle(1100, 570, 1050, 810, fill="black", tags="wall")
    canvas.create_rectangle(1150, 600, 1100, 810, fill="black", tags="wall")

    canvas.create_rectangle(1400, 630, 1150, 810, fill="black", tags="wall")

    # --------add wall 2---------

    canvas.create_rectangle(710, 120, 580, 90, fill="black", tags="wall")
    # canvas.create_rectangle(330, 0, 300, 90, fill="black", tags="wall")

    canvas.create_rectangle(700, 470, 600, 440, fill="black", tags="wall")
    canvas.create_rectangle(700, 500, 560, 470, fill="black", tags="wall")
    canvas.create_rectangle(740, 500, 600, 470, fill="black", tags="wall")

    # -----wall right-----
    canvas.create_rectangle(860, 410, 800, 380, fill="black", tags="wall")
    canvas.create_rectangle(960, 350, 900, 320, fill="black", tags="wall")
    canvas.create_rectangle(1280, 290, 1000, 260, fill="black", tags="wall")

    canvas.create_rectangle(930, 210, 900, 180, fill="black", tags="wall")
    canvas.create_rectangle(820, 170, 790, 140, fill="black", tags="wall")

    # ------wall left-------
    canvas.create_rectangle(480, 410, 420, 380, fill="black", tags="wall")
    canvas.create_rectangle(380, 350, 320, 320, fill="black", tags="wall")
    canvas.create_rectangle(280, 290, 0, 260, fill="black", tags="wall")

    canvas.create_rectangle(370, 210, 340, 180, fill="black", tags="wall")
    canvas.create_rectangle(490, 170, 460, 140, fill="black", tags="wall")
    #------hero-normal-----------
    player_left = Image.open("image/hero.png")
    player_left = player_left.resize((50, 50))
    play_2 = ImageTk.PhotoImage(player_left)
    player = canvas.create_image(80, 500, image=play_2, anchor=NW) 
    gravity()                     
    window.bind("<Key>", start_move)
    window.bind("<KeyRelease>", stop_move)

    #-----------enemy-normal--------
    enemy4 = Image.open("image/enemy.png")
    enemy4 = enemy4.resize((70, 70))
    background5 = ImageTk.PhotoImage(enemy4)
    position_enemy5=canvas.create_image(980, 210, image=background5, anchor=NW)
    c=3
    def movebird5():
        global c

        canvas.move(position_enemy5, c, 0)

        (leftPos, topPos, rightPos, bottomPos) = canvas.bbox(position_enemy5)
        if leftPos <= 980 or rightPos >= 1270:
            c = -c
        print(c)
        canvas.after(30, movebird5)
    canvas.after(30, movebird5)

    enemy5 = Image.open("image/enemy.png")
    enemy5 = enemy5.resize((70, 70))
    background6 = ImageTk.PhotoImage(enemy5)
    position_enemy6=canvas.create_image(0, 210, image=background6, anchor=NW)
    d=3
    def movebird6():
        global d

        canvas.move(position_enemy6, d, 0)

        (leftPos, topPos, rightPos, bottomPos) = canvas.bbox(position_enemy6)
        if leftPos <= 0 or rightPos >= 300:
            d = -d
        print(d)
        canvas.after(40, movebird6)
    canvas.after(30, movebird6)

    enemy6 = Image.open("image/enemy.png")
    enemy6 = enemy6.resize((70, 70))
    background7 = ImageTk.PhotoImage(enemy6)
    position_enemy7=canvas.create_image(580, 390, image=background7, anchor=NW)
    e=3
    def movebird7():
        global e

        canvas.move(position_enemy7, e, 0)

        (leftPos, topPos, rightPos, bottomPos) = canvas.bbox(position_enemy7)
        if leftPos <= 580 or rightPos >= 720:
            e = -e
        print(e)
        canvas.after(80, movebird7)
    canvas.after(30, movebird7)


    enemy7 = Image.open("image/enemy.png")
    enemy7 = enemy7.resize((70, 70))
    background8 = ImageTk.PhotoImage(enemy7)
    position_enemy8=canvas.create_image(530, 580, image=background8, anchor=NW)
    f=3
    def movebird8():
        global f

        canvas.move(position_enemy8, f, 0)

        (leftPos, topPos, rightPos, bottomPos) = canvas.bbox(position_enemy8)
        if leftPos <= 530 or rightPos >= 770:
            f = -f
        print(f)
        canvas.after(30, movebird8)
    canvas.after(30, movebird8)
    # -----------door 2-------------
    image = Image.open('./image/door.png')
    imageTk = ImageTk.PhotoImage(image)
    canvas.create_image(645, 59,image=imageTk)

    # -----------add key2----------
    image4 = Image.open('./image/key.png')
    imageTk4 = ImageTk.PhotoImage(image4)
    canvas.create_image(650, 570,image=imageTk4)

    # -------------add heart-------------
    image5 = Image.open('./image/heart.png')
    imageTk5 = ImageTk.PhotoImage(image5)
    canvas.create_image(235, 50,image=imageTk5)

    # ------------coins 2--------------
    image2 = Image.open('./image/coint.png')
    imageTk2 = ImageTk.PhotoImage(image2)

    # -------------coins right------------
    canvas.create_image(1100, 220,image=imageTk2)
    canvas.create_image(1140, 220,image=imageTk2)
    canvas.create_image(1180, 220,image=imageTk2)
    canvas.create_image(1220, 220,image=imageTk2)

    canvas.create_image(915, 160,image=imageTk2)
    canvas.create_image(805, 120,image=imageTk2)

    canvas.create_image(1220, 450,image=imageTk2)
    canvas.create_image(1180, 450,image=imageTk2)
    canvas.create_image(1140, 450,image=imageTk2)
    canvas.create_image(1140, 490,image=imageTk2)
    canvas.create_image(1180, 490,image=imageTk2)
    canvas.create_image(1220, 490,image=imageTk2)

    # ---------------coins left-------------
    canvas.create_image(55, 220,image=imageTk2)
    canvas.create_image(95, 220,image=imageTk2)
    canvas.create_image(135, 220,image=imageTk2)
    canvas.create_image(175, 220,image=imageTk2)

    canvas.create_image(355, 160,image=imageTk2)
    canvas.create_image(475, 120,image=imageTk2)

    canvas.create_image(135, 480,image=imageTk2)
    canvas.create_image(95, 480,image=imageTk2)
    canvas.create_image(55, 480,image=imageTk2)
    canvas.create_image(55, 440,image=imageTk2)
    canvas.create_image(95, 440,image=imageTk2)
    canvas.create_image(135, 440,image=imageTk2)

    # ----------------coins center-----------------
    canvas.create_image(612, 330,image=imageTk2)
    canvas.create_image(652, 330,image=imageTk2)
    canvas.create_image(692, 330,image=imageTk2)
    canvas.create_image(612, 290,image=imageTk2)
    canvas.create_image(652, 290,image=imageTk2)
    canvas.create_image(692, 290,image=imageTk2)
    stop_to_stop()

   



    window.mainloop()

#Hard Game--------------------------------

def Hard():
    global window,g,position_enemy10,h,position_enemy11,i,position_enemy12,j,position_enemy13,k,player,keyPressed
    window.destroy() 
    window = Tk()
    window.title('Hard')
    app_width = window.winfo_screenwidth()
    app_height = window.winfo_screenheight()
    window.geometry(f'{app_width}x{app_height}')
    frame = Frame(window, width=app_width, height=app_height)
    frame.pack()
    canvas = Canvas(frame, width=app_width, height=app_height)
    canvas.pack()
    #---------hero-hard------------
    keyPressed = []
    SPEED = 7 
    TIME = 10
    GRAVITY_FORCE=9
    def check_movement(dx=0, dy=0):
            ball_coords = canvas.bbox(player)
            new_x1 = ball_coords[0] + dx
            new_y1 = ball_coords[1] + dy
            new_x2 = ball_coords[2] + dx
            new_y2 = ball_coords[3] + dy
            overlapping_objects = canvas.find_overlapping(new_x1, new_y1, new_x2, new_y2)
            for wall_id in canvas.find_withtag("wall"):
                if wall_id in overlapping_objects:
                    return False
            return True

    def start_move(event):
            if event.keysym not in keyPressed:
                print(event.keysym)
                keyPressed.append(event.keysym)
                if len(keyPressed) == 1:
                    move()

    def stop_move(event):
            global keyPressed
            if event.keysym in keyPressed:
                keyPressed.remove(event.keysym)

    def jump(force):
            if force > 0:
                if check_movement(0, -force):
                    canvas.move(player, 0, -force)
            window.after(TIME, jump, force - 1)

    def move():
            if not keyPressed == []:
                x = 0
                if "Left" in keyPressed:
                    x = -SPEED
                    #add
                    canvas.itemconfig(player,image=hero3)
                if "Right" in keyPressed:
                    x = SPEED
                    canvas.itemconfig(player,image=play_3)
                if check_movement(x, 0):
                    canvas.move(player, x, 0)
                if "space" in keyPressed and not check_movement(0, GRAVITY_FORCE):
                    jump(30)
                window.after(TIME, move)

    def gravity():
        if check_movement(0, GRAVITY_FORCE):
            canvas.move(player, 0, GRAVITY_FORCE)
        window.after(TIME, gravity)
    bg_image = Image.open("image/bg.png")
    bg_image = bg_image.resize((app_width, app_height))
    background = ImageTk.PhotoImage(bg_image)
    canvas.create_image(0, 0, image=background, anchor=NW)
    #add more
    hero_4 = Image.open("image/image 16.png")
    hero_4 = hero_4.resize((40, 40))
    hero3 = ImageTk.PhotoImage(hero_4)
    button_back = Button(canvas, text="Back",font=40, command=window3, bg='red',border=10)
    button_back.pack()
    button_back.place(x=50, y=50, width=90)

    bg_image = Image.open("image/bg3.jpg")
    bg_image = bg_image.resize((app_width, app_height))
    background = ImageTk.PhotoImage(bg_image)
    canvas.create_image(0, 0, image=background, anchor=NW)
    button_back = Button(canvas, text="Back",font=40, command=window3, bg='red',border=10)
    button_back.pack()
    button_back.place(x=50, y=50, width=90)  

    # ----------Wall Of Hard----------
    canvas.create_rectangle(150, 630, 0, 810, fill="black", tags="wall")
    canvas.create_rectangle(0, 0, 20, 810, fill="black", tags="wall")
    canvas.create_rectangle(0, 0, 1400, 20, fill="black", tags="wall")
    canvas.create_rectangle(1250, 0, 1300, 1200, fill="black", tags="wall")

    # -------------wall center--------------
    canvas.create_rectangle(750, 500, 550, 470, fill="black", tags="wall")

    canvas.create_rectangle(750, 170, 550, 140, fill="black", tags="wall")

    # ---------------wall left-------------------
    canvas.create_rectangle(390, 550, 360, 520, fill="red", tags="wall")
    canvas.create_rectangle(490, 550, 460, 520, fill="red", tags="wall")

    canvas.create_rectangle(470, 430, 440, 400, fill="black", tags="wall")
    canvas.create_rectangle(400, 390, 370, 360, fill="black", tags="wall")
    canvas.create_rectangle(330, 350, 300, 320, fill="black", tags="wall")      
    canvas.create_rectangle(260, 310, 0, 280, fill="black", tags="wall") 

    canvas.create_rectangle(180, 200, 0, 170, fill="black", tags="wall")    

    canvas.create_rectangle(460, 240, 360, 210, fill="black", tags="wall")  

    # ----------------wall right-------------------
    canvas.create_rectangle(940, 550, 910, 520, fill="red", tags="wall")
    canvas.create_rectangle(840, 550, 810, 520, fill="red", tags="wall")

    canvas.create_rectangle(850, 430, 820, 400, fill="black", tags="wall")
    canvas.create_rectangle(920, 390, 890, 360, fill="black", tags="wall")
    canvas.create_rectangle(990, 350, 960, 320, fill="black", tags="wall")
    canvas.create_rectangle(1360, 310, 1030, 280, fill="black", tags="wall")

    canvas.create_rectangle(1360, 200, 1100, 170, fill="black", tags="wall")

    canvas.create_rectangle(920, 240, 820, 210, fill="black", tags="wall")
    

    canvas.create_rectangle(300, 530, 250, 810, fill="black", tags="wall")
    canvas.create_rectangle(300, 570, 200, 810, fill="black", tags="wall")
    canvas.create_rectangle(300, 600, 150, 810, fill="black", tags="wall")


    canvas.create_rectangle(1050, 530, 1000, 810, fill="black", tags="wall")
    canvas.create_rectangle(1100, 570, 1050, 810, fill="black", tags="wall")
    canvas.create_rectangle(1150, 600, 1100, 810, fill="black", tags="wall")

    canvas.create_rectangle(1400, 630, 1150, 810, fill="black", tags="wall")
    #-------------hero-hard------
    player_left = Image.open("image/hero.png")
    player_left = player_left.resize((50, 50))
    play_3 = ImageTk.PhotoImage(player_left)
    player = canvas.create_image(80, 500, image=play_3, anchor=NW) 
    gravity()                     
    window.bind("<Key>", start_move)
    window.bind("<KeyRelease>", stop_move)

    #----------enemy-----------
    enemy8 = Image.open("image/enemy.png")
    enemy8 = enemy8.resize((70, 70))
    background9= ImageTk.PhotoImage(enemy8)
    position_enemy9=canvas.create_image(530, 420, image=background9, anchor=NW)
    g=3
    def movebird9():
        global g
        canvas.move(position_enemy9, g, 0)
        (leftPos, topPos, rightPos, bottomPos) = canvas.bbox(position_enemy9)
        if leftPos <= 530 or rightPos >= 770:
            g = -g
        print(g)
        canvas.after(30, movebird9)
    canvas.after(30, movebird9)
    enemy9 = Image.open("image/enemy.png")
    enemy9 = enemy9.resize((70, 70))
    background10= ImageTk.PhotoImage(enemy9)
    position_enemy10=canvas.create_image(1010, 230, image=background10, anchor=NW)
    h=3
    def movebird10():
        global h
        canvas.move(position_enemy10, h, 0)
        (leftPos, topPos, rightPos, bottomPos) = canvas.bbox(position_enemy10)
        if leftPos <= 1010 or rightPos >= 1270:
            h = -h
        print(h)
        canvas.after(30, movebird10)
    canvas.after(30, movebird10)
    enemy10 = Image.open("image/enemy.png")
    enemy10 = enemy10.resize((70, 70))
    background11= ImageTk.PhotoImage(enemy10)
    position_enemy11=canvas.create_image(0, 230, image=background11, anchor=NW)
    i=3
    def movebird11():
        global i
        canvas.move(position_enemy11, i, 0)
        (leftPos, topPos, rightPos, bottomPos) = canvas.bbox(position_enemy11)
        if leftPos <= 0 or rightPos >= 280:
            i = -i
        print(i)
        canvas.after(30, movebird11)
    canvas.after(30, movebird11)
    enemy11 = Image.open("image/enemy.png")
    enemy11 = enemy11.resize((70, 70))
    background12= ImageTk.PhotoImage(enemy11)
    position_enemy12=canvas.create_image(340, 160, image=background12, anchor=NW)
    j=3
    def movebird12():
        global j
        canvas.move(position_enemy12, j, 0)
        (leftPos, topPos, rightPos, bottomPos) = canvas.bbox(position_enemy12)
        if leftPos <= 340 or rightPos >= 480:
            j = -j
        print(j)
        canvas.after(100, movebird12)
    canvas.after(30, movebird12)
    enemy12 = Image.open("image/enemy.png")
    enemy12 = enemy12.resize((70, 70))
    background13= ImageTk.PhotoImage(enemy12)
    position_enemy13=canvas.create_image(800, 160, image=background13, anchor=NW)
    k=3
    def movebird13():
        global k
        canvas.move(position_enemy13, k, 0)
        (leftPos, topPos, rightPos, bottomPos) = canvas.bbox(position_enemy13)
        if leftPos <= 800 or rightPos >= 940:
            k = -k
        print(k)
        canvas.after(100, movebird13)
    canvas.after(30, movebird13)
    
    # -----------door 3-------------

    image = Image.open('./image/door3.png')
    imageTk = ImageTk.PhotoImage(image)
    canvas.create_image(645, 108,image=imageTk)

    # ------------add key3--------------
    image4 = Image.open('./image/key.png')
    imageTk4 = ImageTk.PhotoImage(image4)
    canvas.create_image(1200, 590,image=imageTk4)

    # -------------add heart-------------
    image5 = Image.open('./image/heart.png')
    imageTk5 = ImageTk.PhotoImage(image5)
    canvas.create_image(645, 50,image=imageTk5)

    # ------------coins 3--------------
    image2 = Image.open('./image/coint.png')
    imageTk2 = ImageTk.PhotoImage(image2)

    # ---------------center coins---------------
    canvas.create_image(700, 400,image=imageTk2)
    canvas.create_image(650, 400,image=imageTk2)
    canvas.create_image(600, 400,image=imageTk2)

    canvas.create_image(600, 360,image=imageTk2)
    canvas.create_image(650, 360,image=imageTk2)
    canvas.create_image(700, 360,image=imageTk2)

    canvas.create_image(700, 320,image=imageTk2)
    canvas.create_image(650, 320,image=imageTk2)
    canvas.create_image(600, 320,image=imageTk2)

    # -----------------right coins---------------
    canvas.create_image(870, 460,image=imageTk2)

    canvas.create_image(1150, 490,image=imageTk2)
    canvas.create_image(1190, 490,image=imageTk2)
    canvas.create_image(1230, 490,image=imageTk2)

    canvas.create_image(1150, 450,image=imageTk2)
    canvas.create_image(1190, 450,image=imageTk2)
    canvas.create_image(1230, 450,image=imageTk2)

    canvas.create_image(1150, 530,image=imageTk2)
    canvas.create_image(1190, 530,image=imageTk2)
    canvas.create_image(1230, 530,image=imageTk2)

    # ------------------coins on-----------------
    canvas.create_image(1150, 240,image=imageTk2)
    canvas.create_image(1190, 240,image=imageTk2)
    canvas.create_image(1230, 240,image=imageTk2)
    canvas.create_image(1110, 240,image=imageTk2)

    canvas.create_image(1150, 150,image=imageTk2)
    canvas.create_image(1190, 150,image=imageTk2)
    canvas.create_image(1230, 150,image=imageTk2)

    canvas.create_image(870, 150,image=imageTk2)


    # ---------------------left coins------------
    canvas.create_image(425, 460,image=imageTk2)

    canvas.create_image(43, 490,image=imageTk2)
    canvas.create_image(83, 490,image=imageTk2)
    canvas.create_image(123, 490,image=imageTk2)

    canvas.create_image(43, 450,image=imageTk2)
    canvas.create_image(83, 450,image=imageTk2)
    canvas.create_image(123, 450,image=imageTk2)

    canvas.create_image(43, 530,image=imageTk2)
    canvas.create_image(83, 530,image=imageTk2)
    canvas.create_image(123, 530,image=imageTk2)

    # -------------------coins on-----------------
    canvas.create_image(43,240,image=imageTk2)
    canvas.create_image(83, 240,image=imageTk2)
    canvas.create_image(123, 240,image=imageTk2)
    canvas.create_image(163, 240,image=imageTk2)

    canvas.create_image(43, 150,image=imageTk2)
    canvas.create_image(83, 150,image=imageTk2)
    canvas.create_image(123, 150,image=imageTk2)

    canvas.create_image(410, 150,image=imageTk2)
    stop_to_stop()



    window.mainloop()
    
#show-of start window--------------

window = Tk()
app_width = window.winfo_screenwidth()
app_height = window.winfo_screenheight()
window.geometry(f'{app_width}x{app_height}')
bg_image = Image.open("./image/bg2.jpg")
bg_image = bg_image.resize((app_width, app_height))
background = ImageTk.PhotoImage(bg_image)

frame = Frame(window, width=app_width, height=app_height)
frame.pack()

canvas = Canvas(frame, width=app_width, height=app_height)
canvas.pack()
canvas.create_image(0, 0, image=background, anchor=NW)

splash_label = Label(window, text="Power A-five", font=("Robus", 60, "bold"))
splash_label.pack()
splash_label.place(relx=0.5, rely=0.3, anchor='center')
window.title("Progress Bar in Tk")
progressbar = ttk.Progressbar(mode="indeterminate")
progressbar.place(x=550, y=390, width=240)
progressbar.start()
window.after(2000, main) 
def play():
    winsound.PlaySound('./sound/086354_8_bit_arcade_video_game_start_sound_effect_gun_reload_and.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
play()

window.mainloop()


