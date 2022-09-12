import tkinter as tk
import math
import tkinter.messagebox as mb

pressflag=0
pressflaginfo = 0
globalxy = []
numbers='1234567890'
znaki = '*-+/'
maxx=maxy=k=0
miny=minx=9999999999
step=0.01
cel=[j for j in range(-50,51)]
f=[i for i in range(-50,51)]
x0=-12
xe=12 - step

while x0 <= xe:
    
    x0+=step
    f.append(x0)
    


class binds():

    def on_num0(e):
        config.num0['bg'] = '#CBCBCB'
        config.num0['fg'] = 'black'
    def on_num0l(e):
        config.num0['bg'] = '#373737'
        config.num0['fg'] = 'white'
    def on_num1(e):
        config.num1['bg'] = '#CBCBCB'
        config.num1['fg'] = 'black'
    def on_num1l(e):
        config.num1['bg'] = '#373737'
        config.num1['fg'] = 'white'
    def on_num2(e):
        config.num2['bg'] = '#CBCBCB'
        config.num2['fg'] = 'black'
    def on_num2l(e):
        config.num2['bg'] = '#373737'
        config.num2['fg'] = 'white'
    def on_num3(e):
        config.num3['bg'] = '#CBCBCB'
        config.num3['fg'] = 'black'
    def on_num3l(e):
        config.num3['bg'] = '#373737'
        config.num3['fg'] = 'white'
    def on_num4(e):
        config.num4['bg'] = '#CBCBCB'            #  '#EFEFEF'
        config.num4['fg'] = 'black'
    def on_num4l(e):
        config.num4['bg'] = '#373737'
        config.num4['fg'] = 'white'
    def on_num5(e):
        config.num5['bg'] = '#CBCBCB'
        config.num5['fg'] = 'black'
    def on_num5l(e):
        config.num5['bg'] = '#373737'
        config.num5['fg'] = 'white'
    def on_num6(e):
        config.num6['bg'] = '#CBCBCB'
        config.num6['fg'] = 'black'
    def on_num6l(e):
        config.num6['bg'] = '#373737'
        config.num6['fg'] = 'white'
    def on_num7(e):
        config.num7['bg'] = '#CBCBCB'
        config.num7['fg'] = 'black'
    def on_num7l(e):
        config.num7['bg'] = '#373737'
        config.num7['fg'] = 'white'
    def on_num8(e):
        config.num8['bg'] = '#CBCBCB'
        config.num8['fg'] = 'black'
    def on_num8l(e):
        config.num8['bg'] = '#373737'
        config.num8['fg'] = 'white'
    def on_num9(e):
        config.num9['bg'] = '#CBCBCB'
        config.num9['fg'] = 'black'
    def on_num9l(e):
        config.num9['bg'] = '#373737'
        config.num9['fg'] = 'white'


    def on_btnu1(e):
        config.btnu1['bg'] = '#CBCBCB'
        config.btnu1['fg'] = 'black'
    def on_btnu1l(e):
        config.btnu1['bg'] = '#6B6B6B'
        config.btnu1['fg'] = 'white'
    def on_btnu2(e):
        config.btnu2['bg'] = '#CBCBCB'
        config.btnu2['fg'] = 'black'
    def on_btnu2l(e):
        config.btnu2['bg'] = '#6B6B6B'
        config.btnu2['fg'] = 'white'
    def on_btnu3(e):
        config.btnu3['bg'] = '#CBCBCB'
        config.btnu3['fg'] = 'black'
    def on_btnu3l(e):
        config.btnu3['bg'] = '#6B6B6B'
        config.btnu3['fg'] = 'white'
    def on_btnu4(e):
        config.btnu4['bg'] = '#CBCBCB'
        config.btnu4['fg'] = 'black'
    def on_btnu4l(e):
        config.btnu4['bg'] = '#6B6B6B'
        config.btnu4['fg'] = 'white'
    def on_btnu5(e):
        config.btnu5['bg'] = '#CBCBCB'
        config.btnu5['fg'] = 'black'
    def on_btnu5l(e):
        config.btnu5['bg'] = '#6B6B6B'
        config.btnu5['fg'] = 'white'


    def on_btn2(e):
        config.btn2['bg'] = '#CBCBCB'
        config.btn2['fg'] = 'black'
    def on_btn2l(e):
        config.btn2['bg'] = '#6B6B6B'
        config.btn2['fg'] = 'white'
    def on_btn3(e):
        config.btn3['bg'] = '#CBCBCB'
        config.btn3['fg'] = 'black'
    def on_btn3l(e):
        config.btn3['bg'] = '#6B6B6B'
        config.btn3['fg'] = 'white'
    def on_btn1(e):
        config.btn1['bg'] = '#CBCBCB'
        config.btn1['fg'] = 'black'
    def on_btn1l(e):
        config.btn1['bg'] = '#6B6B6B'
        config.btn1['fg'] = 'white'


    def on_enterent(e):
        config.enter['bg'] = '#EFEFEF'
    def on_leaveent(e):
        config.enter['bg'] = '#CBCBCB'
    def on_enter(e):
        config.btn['bg'] = '#CBCBCB'
        config.btn['fg'] = 'black'
    def on_leave(e):
        config.btn['bg'] = '#6B6B6B'
        config.btn['fg'] = 'white'
    def on_entercall(e):
        config.funcall['bg'] = '#CBCBCB'
        config.funcall['fg'] = 'black'
    def on_leavecall(e):
        config.funcall['bg'] = '#373737'
        config.funcall['fg'] = 'white'
    def on_dotb(e):
        config.dotb['bg'] = '#CBCBCB'
        config.dotb['fg'] = 'black'
    def on_dotbl(e):
        config.dotb['bg'] = '#373737'
        config.dotb['fg'] = 'white'
    def on_plus(e):
        config.plus['bg'] = '#CBCBCB'
        config.plus['fg'] = 'black'
    def on_plusl(e):
        config.plus['bg'] = '#6B6B6B'
        config.plus['fg'] = 'white'
    def on_minus(e):
        config.minus['bg'] = '#CBCBCB'
        config.minus['fg'] = 'black'
    def on_minusl(e):
        config.minus['bg'] = '#6B6B6B'
        config.minus['fg'] = 'white'
    def on_umn(e):
        config.umn['bg'] = '#CBCBCB'
        config.umn['fg'] = 'black'
    def on_umnl(e):
        config.umn['bg'] = '#6B6B6B'
        config.umn['fg'] = 'white'
    def on_delete(e):
        config.delete['bg'] = '#CBCBCB'
        config.delete['fg'] = 'black'
    def on_deletel(e):
        config.delete['bg'] = 'gray'
        config.delete['fg'] = 'white'
    def on_clear(e):
        config.clear['bg'] = '#CBCBCB'
        config.clear['fg'] = 'black'
    def on_clearl(e):
        config.clear['bg'] = '#6B6B6B'
        config.clear['fg'] = 'white'
    def on_info(e):
        config.info['bg'] = '#CBCBCB'
        config.info['fg'] = 'black'
    def on_infol(e):
        config.info['bg'] = '#6B6B6B'
        config.info['fg'] = 'white'

class commands():

    def function():
        global pressflaginfo
        global globalxy
        global numbers 
        global f 
        global miny
        global minx
        global maxx
        global maxy

        maxx=maxy=0
        miny=minx=9999999999
        fx = config.enter.get()[8::]
        xx=[]
        xx.extend(f)
        odz = []
        sqrt = []
        deli = [] 
        globalxy.append([f'{fx}'])
        fx = fx.replace('x','(x)')
        fx = fx.replace('^','**')
        f1 = flagx = ff = mainflag = fdel = fdel1  = fdelx = firstx = False
        kx1 = kx2 = 0
        #st = st2 = tt = ''
        #k = ks1 = ks2 = 0
        if (fx.count('(') == fx.count(')')) and ('()' not in fx) and len(fx) > 0:

            for i in range(len(fx)): 

                if fx[i] in numbers and i != len(fx) - 1 and (fx[i+1] == '(' or fx[i+1] == '√'):
                    fx = fx[:i+1] + '*' + fx[i+1:]

                elif fx[i] in numbers and i != 0 and fx[i-1] ==')': 
                    fx = fx[:i] + '*' + fx[i:]

                elif fx[i] == '√':
                    ff = True 
                    sqrt.append('')

                elif fx[i] =='/':
                    fdel=True
                    deli.append('')

                

                if fdel == True:
                    for j in range(len(deli)):
                        if len(deli[j]) == 0:
                            if fx[i] != '/':
                                deli[j]+=fx[i]
                        else: deli[j]+=fx[i]

                    for a in range(len(deli)):
                        if len(deli[a]) != 0:
                            if deli[a].count('(') == deli[a].count(')'):
                                deli[a] += '!'
                                odz.append(deli[a])
                                deli = deli[:a] + deli[a+1:]

                    if fx[i] == 'x' and fdelx==False:
                        fdelx=True


                if ff == True:
                    for j in range(len(sqrt)):
                        if len(sqrt[j]) == 0:
                            if fx[i] != '√':
                                sqrt[j] += fx[i]
                        else: sqrt[j] += (fx[i])
                    
                    for a in range(len(sqrt)):
                        if len(sqrt[a])!=0:
                            if sqrt[a].count('(') == sqrt[a].count(')'):
                                odz.append(sqrt[a])
                                sqrt=sqrt[:a] + sqrt[a+1:]

                    if fx[i] == 'x' and flagx==False:
                        flagx=True

        else: mainflag = True

        if mainflag == False:
            fx = fx.replace('√','math.sqrt')   
            xxdop=[]
            for i in range(len(odz)):                              #отбор иксов
                odz[i] = odz[i].replace('√','math.sqrt')
                for j in range(len(xx)):
                    odz2=odz[i].replace('x',str(xx[j]))
                    if xx[j] not in xxdop:
                        if '!' not in odz2:
                            if (eval(odz2)) < 0:
                                xxdop.append(xx[j])
                        else:
                            if (eval(odz2.replace('!',''))) == 0:
                                xxdop.append(xx[j])

            for i in range(len(xxdop)):
                xx = xx[:(xx.index(xxdop[i]))] + xx[(xx.index(xxdop[i]))+1:]    

            #if -12 in xx:
                #xx.remove(-12)                      ####  проблема в первом while f.append 


            xx.sort()

        globalxy[len(globalxy)-1].append(xx)
        globalxy[len(globalxy)-1].append([])
        
        if len(xx) == 0:
            mainflag = True

        if mainflag == False:

            if 'x' in fx:
                if len(xx) >= 1:

                    for i in range(len(xx)):
                        fx2 = fx
                        fx2 = fx2.replace('x', str(xx[i]))
                        #print(fx2)
                        d = eval(fx2) 
                        miny = min(miny,d)
                        x = ((xx[i]) * 20) + 250 
                        y = (-d * 20) + 250
                        
                        globalxy[len(globalxy)-1][2].append(d)

                        if firstx == True and xx[i] <= 13:
                            config.canvas.create_line(x1,y1,x,y, fill = '#FF0000', width = 1)
                                                                                            ## дельта d
                            #if abs(d) <= 50:  
                            #    if abs(max(d,d1) - min(d,d1)) >= 1:
                            #        ST = f'{min(d,d1)} {max(d1,d)}' 
                            #        globalxy[len(globalxy)-1][2].append(ST) 

                            #    else:
                            #        globalxy[len(globalxy)-1][2].append(d)  
                            #        globalxy[len(globalxy)-1][2].append(d1) 

                        x1 = x 
                        y1 = y
                        #d1 = d
                        firstx = True

            else:
                config.canvas.create_line(-1,-(eval(fx))*20+250,501,-(eval(fx))*20+250)
                miny = min(miny,eval(fx))
            
            commands.press()
            if pressflaginfo == 1: commands.infopush()

        else: mb.showerror(title = 'Ошибка', message = 'Нет решений')  


    def deleted():
        value = config.enter.get()[:len(config.enter.get()) - 1:] 
        if len(value) > 7:
            config.enter.delete(0,tk.END)
            config.enter.insert(0,value)

    def add_digit(digit):
        value = config.enter.get() + digit
        config.enter.delete(0,tk.END)
        config.enter.insert(0,value)

    def press():
        global pressflag
        if pressflag==0:
            config.btn.place_forget()
            config.frameleft.place_forget()
            config.btn['text'] = '<<'
            config.btn.place(x=251,y=0,height = '26')
            config.frameleft.place(x=-225,y=0)
            #config.enter.place(x=450,y=550)
            pressflag=1

        else:
            global value
            config.btn.place_forget()
            config.frameleft.place_forget()
            config.btn['text'] = '>>'
            config.btn.place(x=0,y=0, height = '26')
            config.frameleft.place(x=-476,y=0)
            pressflag=0

    def clearing():
        global pressflag
        global pressflaginfo
        global globalxy
        globalxy=[]
        config.enter.delete(0,tk.END)
        config.enter.insert(0,' F(x) = ')
        config.canvas2.delete('all')
        config.canvas.delete('all')
        config.canvas.create_line(250,0,250,1000)
        config.canvas.create_line(0,250,1000,250)

        #arrow y 
        config.canvas.create_line(250,0,245,12)
        config.canvas.create_line(250,0,255,12)

        #arrow x
        config.canvas.create_line(500,251,490,255)
        config.canvas.create_line(500,250,490,245)
        x0=250
        y0=250
        f=0

        if pressflag == 0:
            commands.press()
        if pressflaginfo == 1:
            commands.infopush()

        ## создание штрихов
        for i in range(10,491,20):
            config.canvas.create_line(i,253,i,247)
            config.canvas.create_line(252,i,247,i)
            if f-12 < 0:
                config.canvas.create_text(i-2,258, text = str(f-12),font=('calibri',7,'normal'))
                if len(str(abs(f-12))) >= 2:
                    config.canvas.create_text(240,500-i, text = str(f-12),font=('calibri',7,'normal'))
                else:
                    config.canvas.create_text(242,500-i, text = str(f-12),font=('calibri',7,'normal'))
            elif f-12 == 0:
                config.canvas.create_text(i-5,255, text = str(f-12),font=('calibri',7,'normal'))

            else:
                config.canvas.create_text(i,258, text = str(f-12),font=('calibri',7,'normal'))
                if len(str(abs(f-12))) >= 2:
                    config.canvas.create_text(240,500-i, text = str(f-12),font=('calibri',7,'normal'))
                else: config.canvas.create_text(242,500-i, text = str(f-12),font=('calibri',7,'normal'))

            f+=1

    def infopush():
        global pressflaginfo
        global globalxy
        global cel
        first = False
        k=last=0
        h=10
        texth=23
        eh = 100
        df='D(f) = '
        ef='E(f) = '                 #⋃ ꝏ
        if pressflaginfo == 0:       #open
            if len(globalxy) > 0:
                for i in range(len(globalxy)):
                    config.canvas2.create_line(0, h, 500, h) 
                    config.canvas2.create_text(130,texth, text=f'f(x) = {globalxy[len(globalxy)-1][0]}', font = ('Calibri', 13, 'normal'))

                    ############################################################    D(f)
                    if type(min(globalxy[i][1])) == int: 
                        if (min(globalxy[i][1])) == -50:
                            df += '(-ꝏ;'
                        else:
                            df += f'[{min(globalxy[i][1])}; '

                    else:
                        df += f'({math.floor(min(globalxy[i][1]))}; '

                    a = max(min(cel),math.ceil(min(globalxy[i][1])))
                    b = min(max(cel), math.floor(max(globalxy[i][1])))

                    for j in range(cel.index(a)+1,cel.index(b)+1):
                        if first == False and cel[j] not in globalxy[i][1]:
                            df += f'{cel[j]}) '   
                            onfirst=cel[j]
                            first = True

                        elif cel[j] not in globalxy[i][1]:
                            k+=1
                            if k % 2 == 0:
                                df += f'⋃ ({last};{cel[j]}) '
                                fork=cel[j]

                            last = cel[j]


                    if max(globalxy[i][1]) == 50:
                            if k>0:
                                if k % 2 == 0:
                                    df += f'⋃ ({fork};+ꝏ)'
                                    #print(1)
                                else:
                                    df += f'⋃ ({fork};{last}) ⋃ ({last};+ꝏ)'
                                    #print(2)
                            else:
                                if first != True:
                                    df += '+ꝏ) '
                                else:
                                    df += f'⋃ ({onfirst};+ꝏ)'
                                #print(3)
                    else:
                        if type(max(globalxy[i][1])) == int:
                            if k>0:
                                if k % 2 == 0:
                                    df += f'⋃ ({fork};{max(globalxy[i][1])}]'
                                    #print(4)
                                else:
                                    df += f'⋃ ({fork};{last}) ⋃ ({last};{max(globalxy[i][1])}]'
                                    #print(5)
                            else:
                                if first != True:
                                    df += f'{max(globalxy[i][1])}]'
                                else: df += f'⋃ ({onfirst};{max(globalxy[i][1])}]'
                                #print(6)

                        else:
                            if k > 0:
                                if k % 2 == 0:
                                    df += f'⋃ ({fork};{math.ceil(max(globalxy[i][1]))})'
                                    #print(7)
                                else:
                                    df += f'⋃ ({fork};{last}) ⋃ ({last};{math.ceil(max(globalxy[i][1]))})'
                                    #print(8)
                            else:
                                if first != True:
                                    df += f'{max(globalxy[i][1])})'
                                else:
                                    df += f'⋃ ({onfisrt};{math.ceil(max(globalxy[i][1]))})'
                                #print(9)

                    config.canvas2.create_text(10,45, text= df, font = ('Calibri', 13, 'normal'), anchor = tk.W)
                    ############################################################  D(f)

                    ############################################################  E(f)
                    
                    dop = [] 
                    first = True
  
                    #for j in range(len(globalxy[i][2])):

                    #    if type(globalxy[i][2][j]) == str:

                    #        f = globalxy[i][2][j].split(' ')
                    #        #globalxy[i][2].pop(j) 

                    #        for g in range(math.floor(float(f[0])), math.ceil(float(f[1]))):
                    #            dop.append(g)

                    #    else:
                    #        for e in range(str(globalxy[i][2][j]).index('.')+1, len(str(globalxy[i][2][j]))):
                    #            if (str(globalxy[i][2][j]))[e] != '0':
                    #                first = False

                    #        if first == True:
                    #            if (int(globalxy[i][2][j])) not in dop:
                    #                dop.append(int(globalxy[i][2][j]))

                    #        first = True

                    #dop.sort()
                    #print(dop)
                    config.canvas2.create_text(10,65, text= ef, font = ('Calibri', 13, 'normal'), anchor = tk.W)
                    ############################################################  E(f)


            pressflaginfo = 1
            config.info.place_forget()               
            config.info['text'] = 'close>>'
            config.info.place(x=275,y=0, width = 50)
            config.frameright.place(x=275,y=0)

        else:
            pressflaginfo = 0
            config.info.place_forget()
            config.info['text'] = '<<info'
            config.frameright.place_forget()
            config.info.place(x=482,y=0, width = 42)


class config():

    win = tk.Tk()
    win.geometry('524x500')
    win.resizable(False,False)
    win.title('KompoMath')
    win.config(bg='white')

    #Создание холста
    canvas = tk.Canvas(win, height = 500, width=500)
    canvas.place(x=24,y=0)
    canvas.create_line(250,0,250,1000)
    canvas.create_line(0,250,1000,250)

    #arrow y 
    canvas.create_line(250,0,245,12)
    canvas.create_line(250,0,255,12)

    #arrow x
    canvas.create_line(500,251,490,255)
    canvas.create_line(500,250,490,245)
    x0=250
    y0=250
    f=0

    ## создание штрихов
    for i in range(10,491,20):
        canvas.create_line(i,253,i,247)
        canvas.create_line(252,i,247,i)
        if f-12 < 0:
            canvas.create_text(i-2,258, text = str(f-12),font=('calibri',7,'normal'))
            if len(str(abs(f-12))) >= 2:
                canvas.create_text(240,500-i, text = str(f-12),font=('calibri',7,'normal'))
            else:
                canvas.create_text(242,500-i, text = str(f-12),font=('calibri',7,'normal'))
        elif f-12 == 0:
            canvas.create_text(i-5,255, text = str(f-12),font=('calibri',7,'normal'))

        else:
            canvas.create_text(i,258, text = str(f-12),font=('calibri',7,'normal'))
            if len(str(abs(f-12))) >= 2:
                canvas.create_text(240,500-i, text = str(f-12),font=('calibri',7,'normal'))
            else: canvas.create_text(242,500-i, text = str(f-12),font=('calibri',7,'normal'))

        f+=1


    frameleft=tk.Frame(win, width=500, height = 417, bg ='gray') 
    frameinfo = tk.Frame(win, width = 500, height = 417, bg = 'gray')
    frameleftdown = tk.Frame(win, width = 500, height = 400, bg = '#EFEFEF')
    enter = tk.Entry(frameleft, bg = '#CBCBCB', font = ('Calibri', 13, 'normal'))
    enter.insert(0,' F(x) = ')
    enter.place(x=224,y=-1, width = 280, height = 90) 

    frameright = tk.Frame(win, width=500, height = 417, bg ='#CBCBCB') 
    framerighttext = tk.Label(frameright, text= 'Information', font = ('Calibri',13,'normal'), bg = '#CBCBCB')
    canvas2= tk.Canvas(frameright, height = 1000, width = 255, bg = '#CBCBCB') 
    canvas2.place(x=-5,y=25)

    ## Кнопки
    
    btn=tk.Button(win,text='>>', command = commands.press, bg='#6B6B6B', padx=5, font=('Calibri',7,'normal'))
    funcall = tk.Button(frameleft, text = '=', command = commands.function ,bg='#373737', padx=30, pady=20, font=('Calibri',10,'normal'), fg='white' )
    btn1=tk.Button(frameleft, text = 'X', command =lambda: commands.add_digit('x'),bg='#6B6B6B', padx=30, pady=5, font=('Calibri',10,'normal'), fg='white' )
    btn2=tk.Button(frameleft, text = '(', command =lambda: commands.add_digit('('),bg='#6B6B6B', padx=30, pady=5, font=('Calibri',10,'normal'), fg='white' )
    btn3=tk.Button(frameleft, text = ')', command =lambda: commands.add_digit(')'),bg='#6B6B6B', padx=30, pady=5, font=('Calibri',10,'normal'), fg='white' )

    btnu2=tk.Button(frameleft, text = '^', command =lambda: commands.add_digit('^'),bg='#6B6B6B', padx=17, pady=20, font=('Calibri',10,'normal'), fg='white' )
    btnu3=tk.Button(frameleft, text = '√', command =lambda: commands.add_digit('√'),bg='#6B6B6B', padx=17, pady=20, font=('Calibri',10,'normal'), fg='white' )
    btnu1=tk.Button(frameleft, text = '/', command =lambda: commands.add_digit('/'),bg='#6B6B6B', padx=18, pady=22, font=('Calibri',10,'normal'), fg='white' )
    btnu4=tk.Button(frameleft, text = '', command =lambda: commands.add_digit(''),bg='#6B6B6B', padx=17, pady=20, font=('Calibri',10,'normal'), fg='white' )
    btnu5=tk.Button(frameleft, text = '', command =lambda: commands.add_digit(''),bg='#6B6B6B', padx=17, pady=20, font=('Calibri',10,'normal'), fg='white' )

    num7=tk.Button(frameleft, text = '7', command =lambda: commands.add_digit('7'),bg='#373737', padx=30, pady=20, font=('Calibri',10,'normal'), fg='white' )
    num8=tk.Button(frameleft, text = '8', command =lambda: commands.add_digit('8'),bg='#373737', padx=30, pady=20, font=('Calibri',10,'normal'), fg='white' )
    num9=tk.Button(frameleft, text = '9', command =lambda: commands.add_digit('9'),bg='#373737', padx=30, pady=20, font=('Calibri',10,'normal'), fg='white' )
    num4=tk.Button(frameleft, text = '4', command =lambda: commands.add_digit('4'),bg='#373737', padx=30, pady=20, font=('Calibri',10,'normal'), fg='white' )
    num5=tk.Button(frameleft, text = '5', command =lambda: commands.add_digit('5'),bg='#373737', padx=30, pady=20, font=('Calibri',10,'normal'), fg='white' )
    num6=tk.Button(frameleft, text = '6', command =lambda: commands.add_digit('6'),bg='#373737', padx=30, pady=20, font=('Calibri',10,'normal'), fg='white' )
    num1=tk.Button(frameleft, text = '1', command =lambda: commands.add_digit('1'),bg='#373737', padx=30, pady=20, font=('Calibri',10,'normal'), fg='white' )
    num2=tk.Button(frameleft, text = '2', command =lambda: commands.add_digit('2'),bg='#373737', padx=30, pady=20, font=('Calibri',10,'normal'), fg='white' )
    num3=tk.Button(frameleft, text = '3', command =lambda: commands.add_digit('3'),bg='#373737', padx=30, pady=20, font=('Calibri',10,'normal'), fg='white' )
    num0=tk.Button(frameleft, text = '0', command =lambda: commands.add_digit('0'),bg='#373737', padx=30, pady=20, font=('Calibri',10,'normal'), fg='white' )
    dotb=tk.Button(frameleft, text = ',', command =lambda: commands.add_digit('.'),bg='#373737', padx=32, pady=20, font=('Calibri',10,'normal'), fg='white' )
    plus=tk.Button(frameleft, text = '+', command =lambda: commands.add_digit('+'),bg='#6B6B6B', padx=30, pady=5, font=('Calibri',10,'normal'), fg='white' )
    minus=tk.Button(frameleft, text = '-', command =lambda: commands.add_digit('-'),bg='#6B6B6B', padx=31, pady=5, font=('Calibri',10,'normal'), fg='white' )
    umn=tk.Button(frameleft, text = '*', command =lambda: commands.add_digit('*'),bg='#6B6B6B', padx=30, pady=5, font=('Calibri',10,'normal'), fg='white' )
    delete=tk.Button(frameleft, text = '⌫', command = commands.deleted,bg='gray', font=('Calibri',10,'normal'), fg='white')
    clear = tk.Button(win, text ='Clear', bg = '#6B6B6B', font=('Calibri',10,'normal'), command = commands.clearing, fg = 'white')
    info = tk.Button(win, text = '<<Info', bg = '#6B6B6B', font=('Calibri', 10, 'normal'), command = commands.infopush, fg = 'white')

    #Бинды

    num0.bind('<Enter>', binds.on_num0) 
    num0.bind('<Leave>', binds.on_num0l)
    num1.bind('<Enter>', binds.on_num1) 
    num1.bind('<Leave>', binds.on_num1l)
    num2.bind('<Enter>', binds.on_num2) 
    num2.bind('<Leave>', binds.on_num2l)
    num3.bind('<Enter>', binds.on_num3) 
    num3.bind('<Leave>', binds.on_num3l)
    num4.bind('<Enter>', binds.on_num4) 
    num4.bind('<Leave>', binds.on_num4l)
    num5.bind('<Enter>', binds.on_num5) 
    num5.bind('<Leave>', binds.on_num5l)
    num6.bind('<Enter>', binds.on_num6) 
    num6.bind('<Leave>', binds.on_num6l)
    num7.bind('<Enter>', binds.on_num7) 
    num7.bind('<Leave>', binds.on_num7l)
    num8.bind('<Enter>', binds.on_num8) 
    num8.bind('<Leave>', binds.on_num8l)
    num9.bind('<Enter>', binds.on_num9) 
    num9.bind('<Leave>', binds.on_num9l)

    btnu1.bind('<Enter>', binds.on_btnu1) 
    btnu1.bind('<Leave>', binds.on_btnu1l)
    btnu2.bind('<Enter>', binds.on_btnu2) 
    btnu2.bind('<Leave>', binds.on_btnu2l)
    btnu3.bind('<Enter>', binds.on_btnu3) 
    btnu3.bind('<Leave>', binds.on_btnu3l)
    btnu4.bind('<Enter>', binds.on_btnu4) 
    btnu4.bind('<Leave>', binds.on_btnu4l)
    btnu5.bind('<Enter>', binds.on_btnu5) 
    btnu5.bind('<Leave>', binds.on_btnu5l)

    btn1.bind('<Enter>', binds.on_btn1)
    btn1.bind('<Leave>', binds.on_btn1l)
    btn2.bind('<Enter>', binds.on_btn2)
    btn2.bind('<Leave>', binds.on_btn2l)
    btn3.bind('<Enter>', binds.on_btn3)
    btn3.bind('<Leave>', binds.on_btn3l)

    funcall.bind('<Enter>', binds.on_entercall)
    funcall.bind('<Leave>', binds.on_leavecall)
    btn.bind('<Enter>', binds.on_enter)
    btn.bind('<Leave>', binds.on_leave)
    enter.bind('<Enter>', binds.on_enterent)
    enter.bind('<Leave>', binds.on_leaveent)
    dotb.bind('<Enter>', binds.on_dotb) 
    dotb.bind('<Leave>', binds.on_dotbl)
    plus.bind('<Enter>', binds.on_plus) 
    plus.bind('<Leave>', binds.on_plusl)
    minus.bind('<Enter>', binds.on_minus) 
    minus.bind('<Leave>', binds.on_minusl)
    umn.bind('<Enter>', binds.on_umn) 
    umn.bind('<Leave>', binds.on_umnl)
    delete.bind('<Enter>', binds.on_delete) 
    delete.bind('<Leave>', binds.on_deletel)
    clear.bind('<Enter>', binds.on_clear) 
    clear.bind('<Leave>', binds.on_clearl)
    info.bind('<Enter>', binds.on_info) 
    info.bind('<Leave>', binds.on_infol)


class packs():      #дельта x = 75, у = 64
    config.num7.place(x=225, y = 160)  #config.num7.place(x=247, y = 164)
    config.num8.place(x=300, y = 160)
    config.num9.place(x=375, y = 160)
    config.num4.place(x=225, y = 224)
    config.num5.place(x=300, y = 224)
    config.num6.place(x=375, y = 224)
    config.num1.place(x=225, y = 288)
    config.num2.place(x=300, y = 288)
    config.num3.place(x=375, y = 288)
    config.num0.place(x=300, y = 352)
    config.funcall.place(x=225, y = 352)
    config.dotb.place(x=375, y = 352)
    config.btn.place(x=0,y=0, height = 26)
    config.btn1.place(x=225,y=92, width = 75) # config.btn1.place(x=225,y=95, width = 75)
    config.btn2.place(x=300,y=92, width = 75)
    config.btn3.place(x=375,y=92, width = 76)
    config.frameleft.place(x=-476,y=0)
    config.frameleftdown.place(x=-476, y = 420) 
    config.frameright.place(x=530, y = 0)   ################
    config.delete.place(x=450,y=59, width = 50, height = 30)
    config.clear.place(x=482,y=473)  #config.clear.place(x=484,y=26)
    config.info.place(x=482,y=0, width = 42)
    config.plus.place(x=300,y=126)
    config.minus.place(x=225,y=126)   ### y на 4 
    config.umn.place(x=375,y=126, width = 76)
    config.btnu1.place(x=451,y=92,width = 49)
    config.btnu2.place(x=451,y=160)
    config.btnu3.place(x=451,y=224)
    config.btnu4.place(x=451,y=288, width = 49)
    config.btnu5.place(x=451,y=352, width = 49)
    config.framerighttext.place(x = 95,y = 0)

config.win.mainloop()

