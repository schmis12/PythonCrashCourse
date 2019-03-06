# Stefan J. Schmidt, 06.03.2019

print('peak list:')
peaks = ['schauinsland', 'belchen', 'feldberg']
print(f'{peaks}'.title())

print('append a peak:')
peaks.append('grand ballon')
print(f'{peaks}'.title())

print('insert peak at 1st position:')
peaks.insert(0, 'rosskopf')
print(f'{peaks}')

print('pop off last entry:')
popped = peaks.pop()
print(f'popped {popped.upper()}')
print(f'{peaks}'.title())

print('insert at 2nd position:')
peaks.insert(1, 'everest')
print(f'{peaks}'.title())

print('pop of 2nd position:')
peaks.pop(1)
print(f'{peaks}'.title())

print('insert at 3rd position:')
peaks.insert(2, 'kandel')
print(f'{peaks}'.title())

print('delete 1st position:')
del peaks[0]
print(f'{peaks}'.title())

print('remove by value \'kandel\':')
peaks.remove('kandel')
print(f'{peaks}'.title())

print('temporary sorted list:')
print(f'{sorted(peaks)}'.title())
print('original:')
print(f'{peaks}'.title())

print('temporary reverse sorted list:')
print(f'{sorted(peaks, reverse=True)}'.title())
print('original:')
print(f'{peaks}'.title())

print('permanently reversed:')
peaks.reverse()
print(f'{peaks}'.title())

print('permanently sorted:')
peaks.sort()
print(f'{peaks}'.title())

print('permanently reverse sorted:')
peaks.sort(reverse=True)
print(f'{peaks}'.title())