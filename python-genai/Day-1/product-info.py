
# creating product catalogue display info

def product_catalogue():
    Product_name="Wireless Mouse"
    Product_price = 29.99
    Product_quantity = 5
    Product_discount = 0.1
    after_discount_price = (Product_quantity) * (Product_price) * (Product_discount)

    product_info=f'''
    =================== PRODUCT RECEIPT ====================
    #  1. PRODUCT NAME :- {Product_name}                
    #  2. PRODUCT QUANTITY :- {Product_quantity}        
    #  3. PRODUCT PRICE :- {Product_price}              
    #  4. DISCOUNT PRICE :- {after_discount_price}      
    ====================== END =============================
    '''
    print(product_info)
    print(f'Prodcut price for single {Product_name} item before discount: {Product_price}$')
    print()
    print(f'Prodcut price for single {Product_name} item after discount: {after_discount_price}$')

 
product_catalogue()
