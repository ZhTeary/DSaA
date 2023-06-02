class CreditCard:
    """A consumer credit card."""

    def __init__(self, customer, bank, acnt, limit, balance=0):
        """Create a new credit card instance.

        The initial balance is zero.

        customer    the name of the customer(e.g. 'John Bowman')
        bank        the name of the bank(e.g. 'California Savings')
        acnt        the account identifier(e.g. '5391 0375 9387 5309')
        limit       credit limit(measured in dollars)
        """
        self._customer = customer
        self._bank = bank
        self._acnt = acnt
        self._limit = limit
        self._balance = balance

    def get_customer(self):
        """Return name of the customer."""
        return self._customer

    def get_bank(self):
        """Return name of the bank"""
        return self._bank

    def get_account(self):
        """Return the card identifying number (typically stored as a string)"""
        return self._acnt

    def get_limit(self):
        """Return current credit limit"""
        return self._limit

    def get_balance(self):
        """Return current balance"""
        return self._balance

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.

        Return True if charge was processed; False if charge was denied.
        """
        try:
            if price + self._balance > self._limit:
                print(self._bank,self._balance)
                return False
            else:
                self._balance += price
                return True
        except TypeError:
            print('TypeError： 参数类型不对')

    def make_payment(self, amount):
        """Process custom payment that reduces balance"""
        # try:
        if amount > 0:
            self._balance -= amount
        else:
            raise ValueError("amount should bigger than 0 ")
        # except TypeError:
        #     print('TypeError： 参数类型不对')
        raise TypeError("miss arguement")



class PredatoryCreditCard(CreditCard):
    """An extension to CreditCard that compounds interst and fees."""

    def __init__(self, customer, bank, acnt, limit, apr):
        """Create a nre predatory credit card instance

        The initial balance is zero.

        customer    the name of the customer(e.g. 'John Bowman')
        bank        the name of the bank(e.g. 'California Savings')
        acnt        the account identifier(e.g. '5391 0375 9387 5309')
        limit       credit limit(measured in dollars)
        apr         annual percentage rate(e.g. 0.0825 for 8.25% APR)
        """
        super().__init__(customer, bank, acnt, limit)  # call super constructor
        self._apr = apr

    def charge(self, price):
        """ Charge given price to the card, assuming sufficient credit limit.

        Return True if charge was processed.
        Return False and assess $5 fee if charge is denied.
        """
        success = super().charge(price)
        if not success:
            self._balance -= 5
        return success

    def process_month(self):
        """Access monthly interest on outstanding balance."""
        if self._balance > 0:
            # if positive balance, convert APR to monthly multiplicative factor
            monthly_factor = pow(1 + self._apr, 1 / 12)
            self._balance *= monthly_factor
#

"""Test"""
if __name__ == '__main__':
    # wallet = [CreditCard("John Doe", "1st bank", "0000 1111 2222 3333", 1000),
    #           CreditCard("John Doe", "2st bank", "1111 2222 3333 4444", 2000),
    #           CreditCard("John Doe", "3st bank", "2222 3333 4444 5555", 3000)]
    # for val in range(1, 46):
    #     wallet[0].charge(val)
    #     wallet[1].charge(2 * val)
    #     wallet[2].charge(3 * val)
    c =  CreditCard("John Doe", "3st bank", "2222 3333 4444 5555", 3000)
    try:
        c.charge("ff")
    except TypeError:
        print("miss arg")
    # for c in range(3):
    #     print('Customer =', wallet[c].get_customer())
    #     print('Bank =', wallet[c].get_bank())
    #     print('Account =', wallet[c].get_account())
    #     print('Limit =', wallet[c].get_limit())
    #     print('Balance =', wallet[c].get_balance())
    #     while wallet[c].get_balance() > 100:
    #         wallet[c].make_payment(100)
    #         print('New balance =', wallet[c].get_balance())
