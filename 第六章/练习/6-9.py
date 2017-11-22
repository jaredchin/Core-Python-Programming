minutes = input('Input the minutes: ')
int_minutes = int(minutes)

houres = str(int(int_minutes / 60))
minute = str(int_minutes % 60)

print(houres + ':' + minute)