john = float(input('enter john age'))
smith = float(input('enter smith age'))
ajay = float(input('enter ajay age'))

if john>smith or john>ajay:
    print('john is eldest')
elif smith>ajay:
    print('smith is eldest')
else:
    print('ajay is eldest')

    