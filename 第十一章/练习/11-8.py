def isrunnian(year):
    try:
        year = int(year)
        if year % 4 == 0 and year % 100 !=0 or year % 400 == 0:
            return True
        else:
            return False
    except Exception as e:
        return False


years = [1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004]
print(list(filter(isrunnian, years)))
