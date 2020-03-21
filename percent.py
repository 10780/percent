#percentage calculator
in1 = float(input("First number: "))
in2 = float(input("Second number: "))

def main():
    percent = ((in1/in2) * 100)
    print("{} is {}% of {}".format(in1,percent,in2))

main()
