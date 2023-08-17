def discount(price, is_member):
    if is_member == True:
        discount = 0.10 * price
        discounted_amount = price - discount
        return discounted_amount
    else:
        return 0

#-------------------------------------------------------


def difference(numbers):
    if not numbers:
        return None
    max_num = max(numbers)
    min_num = min(numbers)
    dif = max_num - min_num
    return dif


