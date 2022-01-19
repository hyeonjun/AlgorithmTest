lyrics = ['baby', 'sukhwan', 'tururu', 'turu',
          'very', 'cute', 'tururu', 'turu',
          'in', 'bed', 'tururu', 'turu',
          'baby', 'sukhwan']
n = int(input())
repeat = n // len(lyrics)
idx = n % 14
l = lyrics[idx-1]
if l == 'tururu' or l == 'turu':
    if l == 'tururu' and repeat >= 3:
        l = f'tu+ru*{repeat+2}'
    elif l == 'turu' and repeat >= 4:
        l = f'tu+ru*{repeat+1}'
    else:
        l = l + 'ru' * repeat
print(l)
