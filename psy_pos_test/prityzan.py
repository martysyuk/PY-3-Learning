while True:
    up_c = input('Результаты через запятую (без пробелов):\n').rstrip().split(',')
    if up_c == ['']:
        exit(0)
    up_ball = ((int(up_c[2]) - int(up_c[1])) + (int(up_c[4]) - int(up_c[3])) + (int(up_c[6])) - int(up_c[5])) / 3
    up_ball = round(up_ball, 2)

    print(up_ball)
