def steps(number):
    step = 0
    if (number < 1):
        raise ValueError("Sorry, no numbers below 1")
    elif (number == 1):
        return (step)
    else:
        while (number > 1):
            if number % 2 == 0:
                number = number/2
            else:
                number = number*3 + 1
            
            step = step + 1
        return (step)
