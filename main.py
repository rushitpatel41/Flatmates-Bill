from flat import Bill, Flatmate
from report import PdfReport

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive number")
                continue
            return value
        except ValueError:
            print("Please enter a valid number")

def get_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a non-negative number")
                continue
            return value
        except ValueError:
            print("Please enter a valid integer")

try:
    amount = get_float_input("Hey user, Enter the bill amount: ")
    period = input("What is the bill period? E.g. December 2024: ")

    name1 = input("What is your name? ")
    days_in_house1 = get_int_input(f"How many days does {name1} stay in the house during the bill period? ")

    name2 = input("What is the name of the other flatmate? ")
    days_in_house2 = get_int_input(f"How many days does {name2} stay in the house during the bill period? ")

    the_bill = Bill(amount=amount, period=period.title())
    flatmate1 = Flatmate(name=name1, days_in_house=days_in_house1)
    flatmate2 = Flatmate(name=name2, days_in_house=days_in_house2)

    print(f"\nBill Summary for {period}:")
    print(f"Total Amount: ${amount:.2f}")
    print(f"{flatmate1.name} pays: ${flatmate1.pays(the_bill, flatmate2):.2f}")
    print(f"{flatmate2.name} pays: ${flatmate2.pays(the_bill, flatmate1):.2f}")

    pdf_report = PdfReport(f"{the_bill.period}.pdf")
    pdf_report.generate(flatmate1, flatmate2, the_bill)
    print("\nPDF report has been generated and should open in your browser.")

except Exception as e:
    print(f"\nAn error occurred: {str(e)}")
    print("Please try again with valid inputs.")
