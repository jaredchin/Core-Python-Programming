def atoc(astring):
    for i in range(len(astring)-1, -1, -1):
        if astring[i] == '-' or astring[i] == '+':
            real = float(astring[:i])
            image = float(astring[i:len(astring)-1])
            return complex(real, image)
        else:
            exit('error')

print(atoc('-1.23e+4-5.67j'))