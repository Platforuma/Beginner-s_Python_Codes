'''
Write a Python program to convert temperatures to and from celsius, fahrenheit 
[ Formula : c/5 = (f-32)/9 [ where c = temperature in celsius and f = temperature in fahrenheit ] 
Expected Output : 
60°C is 140 in Fahrenheit
45°F is 7 in Celsius 
'''
temp = input('Enter the Unit of Temperature (C/F): ')

if temp=='C' or temp=='c':
    cel = float(input('Enter the temp in *C: '))
    fah = ((9*cel)/5)+32
    print(str(cel) + '*C is ' + str(fah) + ' in Fahrenheit')

elif temp=='F' or temp=='f':
    fah = float(input('Enter the temp in *F: '))
    cel = 5 * ((fah - 32)/9)
    print(str(fah) + '*F is ' + str(cel) + ' in Celsius')

else:
    print('Enter valid Unit')
