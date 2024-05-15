def calculate_total(items_purchased, grocery_list):
    item_prices = {
        "milk": 2.50,
        "eggs": 3.25,
        "bread": 1.21,
        "cheese": 3.50,
        "apples": 7.44,
        "bananas": 3.88,
        "carrots": 3.89,
        "lettuce": 1.12,
        "potatoes": 32.21,
        "cereal": 5.99,
    }

    # Don't touch above this line

    sum = 0
    unpurchased_items = []
    purchased_item = {}

    for i in range(0, len(grocery_list)):
        if grocery_list[i] not in items_purchased:
            unpurchased_items.append(grocery_list[i])
    
    for i in range(0, len(items_purchased)):
        if items_purchased[i] in item_prices:
            purchased_item[items_purchased[i]] = item_prices[items_purchased[i]]
            sum += item_prices[items_purchased[i]]
    
    return unpurchased_items, purchased_item, sum
    
