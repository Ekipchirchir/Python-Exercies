def convert (fraction):
    try:
        x,y = fraction.split
        x,y = int(x),int(y)
        if not isinstance(x,int) and isinstance(y,int):
            raise ValueError
        if x>y:
            raise ValueError
        if y == 0:
            raise ZeroDivisionError
        return round (x/y * 100)
    except (ValueError, ZeroDivisionError):
        raise ValueError ('Invalid fraction: {}'. format(fraction))
    
    
def gauge(percentage):
    if percentage <=1:
        return "E"
    elif percentage>=99:
        return "F"
    else:
        return "{}%".format(percentage)
    
def main():
    fraction =input("Enter the remainin amount of fuel in X/Y format:")
    try:
        percentage =convert(fraction)
        print('The fuel gauge reads: {}'.format(percentage))
    except ValueError as e:
        print ('Error :{}'.format(str(e))) 
        
if __name__  =="__main__":
    main()
    