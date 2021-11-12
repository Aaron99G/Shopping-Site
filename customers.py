"""Customers at Ubermelon."""


class Customer(object):
    """Ubermelon customer."""

    # TODO: need to implement this
    
    def __init__(self,
                 firstName,
                 lastName,
                 email,
                 password
                 ):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password
        
    def __repr__(self):
        """ Show Information about the Customer"""
        
        return f"<Customer: {self.firstName}, {self.lastName}, {self.email}>"
    
def read_customers(filepath):
    """Read the customer data"""
        
    customers = {}
        
    with open(filepath) as file:
        for line in file:
            (firstName,
             lastName,
             email,
             password) = line.strip().split('|')
                
    customers[email] = Customer(firstName, lastName, email, password)
        
    return customers
        
def get_by_email(email):
    """Return a customer given their email"""
        
    return customers[email]
    
    
customers = read_customers("customers.txt")