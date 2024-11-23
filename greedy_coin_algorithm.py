
def get_exact_change(amount):
    denominations = {
        "$100 bill": 10000,
        "$50 bill": 5000,
        "$20 bill": 2000,
        "$10 bill": 1000,
        "$5 bill": 500,
        "$1 bill": 100,
        "quarter": 25,
        "dime": 10,
        "nickel": 5,
        "penny": 1
    }
    
    change = {}
    
    remaining_amount = round(amount * 100)
    
    for denomination, value in denominations.items():
        if remaining_amount >= value:
            count = remaining_amount // value
            remaining_amount -= count * value
            change[denomination] = count
    
    return change