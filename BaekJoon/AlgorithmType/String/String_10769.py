string = input()
happy, sad = string.count(':-)'), string.count(':-(')
if happy < sad:
    print('sad')
elif happy > sad:
    print('happy')
elif happy == sad == 0:
    print('none')
elif happy == sad:
    print('unsure')