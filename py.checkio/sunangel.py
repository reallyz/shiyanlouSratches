def sun_angle(time):
    #replace this for solution
    c=time.split(sep=':')
    a=int(c[0])
    b=int(c[1])
    if 6<=a<=18:
        return (180/(12*60))*((a-6)*60+b)
    else:
        return "I don't see the sun!"

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")