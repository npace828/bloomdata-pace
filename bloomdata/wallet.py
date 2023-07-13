# class Wallet:

#     # first thing to run when we make a new class
#     # outline required user-provided input values here

#     def __init__(self, inital_amount):
#         # save user provided initial_amount as an attribute
#         self.balance = inital_amount

#     def spend_cash(self, amount):
#         if self.balance < amount:
#             return "not enough money"
#         else:
#             self.balance = self.balance - amount
#             return f"remaining balance: {self.balance}"
        
#     def add_cash(self, amount):
#         self.balance = self.balance + amount
#         return f"new balance of: {self.balance}"
#     # __repr__ method
#     # changes how the "object" looks when its printed out
#     def __repr__(self):
#         return f"wallet with balance of: {self.balance}"

# if __name__ == '__main__':
#     wallet1 = Wallet(100)
#     print(wallet1.add_cash(100))
#     print(wallet1.add_cash(60))



