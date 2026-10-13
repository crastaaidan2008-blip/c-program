def get_price(item):
    if item == "idli":
        return 30
    elif item == "dosa": 
        return 50
    elif item == "coffee":
        return 20
    else:
        return 0

def item_cost(item, qty):
    # Call get_price() and return the cost
    return get_price(item) * qty

def calculate_gst(amount, rate=0.05):
    # Return the GST rounded to 2 decimals
    return round(amount * rate, 2)

def generate_bill(subtotal, discount_percent=0):
    discount = subtotal * (discount_percent / 100)
    amount_after_discount = subtotal - discount
    gst = calculate_gst(amount_after_discount)  # Call calculate_gst()
    total = amount_after_discount + gst
    return discount, gst, total  # Return discount, gst and total

def split_bill(total, people):
    each_pays = total // people
    left_over = total % people
    return each_pays, left_over

# ---------------- Main program ---------------- #
# A group of 3 friends orders 2 dosa and 3 coffee, with a 10% coupon.

# Call item_cost() for dosa and coffee and add them
subtotal = item_cost("dosa", 2) + item_cost("coffee", 3)

# Call generate_bill() using a KEYWORD argument
discount, gst, total = generate_bill(subtotal, discount_percent=10)

# Call split_bill() with the total (as a whole number) and 3 people
each, extra = split_bill(int(total), 3)

print("Subtotal :", subtotal)
print("Discount :", discount)
print("GST      :", gst)
print("Total    :", total)
print("Each pays:", each, "| Left over:", extra)
