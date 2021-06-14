print("Welcome to the tip calculator")
bill = input("What was the total bill?")

tip = input("What percentage tip would you like to give?")
#12% 12*total_bill/100
total_bill =  int(tip)* int (bill) /100 + int(bill)
people = input("How many people have to split the bill?")
each = float(total_bill)/int(people)
x= round(each,2)
print(x)