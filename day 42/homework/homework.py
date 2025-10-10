# def search(budget, prices):
#    for 


def search(budget, prices):
    # Filter prices within budget
    affordable = [price for price in prices if price <= budget]
    
    # Sort the filtered prices
    affordable.sort()
    
    # Convert to string format
    return ' '.join(str(price) for price in affordable)


print(search(10, [12, 5, 8, 20, 3]))