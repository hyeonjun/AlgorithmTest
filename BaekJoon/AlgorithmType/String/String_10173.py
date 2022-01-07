while True:
    string = input()
    if string == 'EOI':
        break
    if 'nemo' in string.lower():
        print('Found')
    else:
        print('Missing')