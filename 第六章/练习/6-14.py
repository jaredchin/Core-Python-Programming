import random
uchoose = input('Input your choice(shitou, jiandao, or bu): ')
compchoose = random.choice(['shitou', 'jiandao', 'bu'])
print('电脑选择出了:%s' % compchoose)

if uchoose == 'shitou':
    if compchoose == 'shitou':
        exit('平手!')
    elif compchoose == 'jiandao':
        exit('恭喜你，你赢了!')
    else:
        exit('你输了!')
elif uchoose == 'jiandao':
    if compchoose == 'shitou':
        exit('你输了!')
    elif compchoose == 'jiandao':
        exit('平手!')
    else:
        exit('恭喜你，你赢了!')
elif uchoose == 'bu':
    if compchoose == 'shitou':
        exit('恭喜你，你赢了!')
    elif compchoose == 'jiandao':
        exit('你输了!')
    else:
        exit('平手!')
else:
    exit('能不能好好玩了?')