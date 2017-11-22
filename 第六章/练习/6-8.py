units = ['zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','forteen','fifteen','sixteen','seventeen','eighteen','nineteen']
tens = ['twenty','thirty','forty','fifth','sixty','seventy','eighty','ninety']
hundreds = ['hundreds']

myInput = input('Enter an integer: ')

myInput_num = int(myInput)

if myInput_num <= 19:
    print(units[myInput_num])
elif myInput_num <= 100:
    tens_unit = int(myInput[0])-2
    unit_unit = int(myInput[1])
    if unit_unit == 0:
        print(tens[tens_unit])
    else:
        print(tens[tens_unit] + '-' + units[unit_unit])
elif myInput_num < 1000:
    if myInput_num <= 119:
        hundred_unit = int(myInput[0])
        unit_unit = int(myInput[1:])
        print(units[hundred_unit] + ' hundreds and ' + units[unit_unit])
    else:
        hundred_unit = int(myInput[0])
        tens_unit = int(myInput[1]) - 2
        unit_unit = int(myInput[2])
        if unit_unit == 0:
            print(units[hundred_unit] + ' hundreds and ' + tens[tens_unit])
        else:
            print(units[hundred_unit] + ' hundreds and ' + tens[tens_unit] + '-' + units[unit_unit])