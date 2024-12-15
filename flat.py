class Bill:
    """
    Object that cotains data about a bill, such as
    total amount and period of the bill
    """
    def __init__(self,amount,period):
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Bill amount must be a positive number")
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Create a flatmate person who lives in the flat
    and pays a share of the bill.
    """
    def __init__(self,name,days_in_house):
        if not isinstance(days_in_house, int) or days_in_house < 0:
            raise ValueError("Days in house must be a non-negative integer")
        self.name = name
        self.days_in_house = days_in_house


    def pays(self, bill, flatmate2):
        total_days = self.days_in_house + flatmate2.days_in_house
        if total_days == 0:
            # If both flatmates were absent, split equally
            return bill.amount / 2
        weight = self.days_in_house/total_days
        to_pay = bill.amount * weight
        return to_pay
