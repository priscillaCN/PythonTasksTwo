def apply_discount(item, price, promo_code)
    
    discount_price = 0
    
    if(promo_code == "SAVE10"):
        discount_price = price - (price * 0.1)
        
    elif(promo_code == "HALFOFF"):
        discount_price = price - (price * 0.5) 
       
    else:
        discount_price = price
    
    return price
