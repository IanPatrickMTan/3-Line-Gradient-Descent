x,y,t=float(input('x = ')),input('y = '),int(input('Iterations: '));exec("for iter in range(t):x-=(eval(y.replace('x', '(x + 0.001)'))-eval(y))/0.001*0.1;print('\\nx =',x,'\\ny =',eval(y))")
