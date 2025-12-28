temp = float(input("enter the temperature value:"))
unit = input("enter the unit(C for Celsius, F for fahrenheirt):").strip().upper()
if unit =="C":
    converted =(temp *9/5)+32
    print(f"{temp} c is equal to {converted:.2f} F")
elif unit == "F":
    converted =(temp -32)*5/9
    print(f"{temp} f is equal to {converted:.2f} C")
else:
    print("invalid unit")