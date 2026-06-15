def main():
    dollars = dollars_to_float(input("How much was the meal? ").replace("$"," "))
    percent = percent_to_float(input("What percentage would you like to tip? ").replace("%"," "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):

    Float=float(d)
    return Float

def percent_to_float(p):
    
    Float=float(p)/100
    return Float


main()