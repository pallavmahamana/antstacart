

tax_dict = {"Medicine":5,
            "Food":5,
            "Clothes":5,
            "Music":3,
            "Imported":18,
            "Books":0}


#get tax on item category
def get_item_tax(itemCategory) -> int:
    return tax_dict[itemCategory]

#get tax on a single item
def get_tax_amount(itemCategory,itemprice) -> int:
    return itemprice*get_item_tax(itemCategory)/100

#get tax on items of quantity
def get_total_tax_onitems(quantity,itemCategory,itemprice) -> int:
    return quantity*get_tax_amount(itemCategory,itemprice)

#get total price of items deducting tax
def get_total_price_ofitems(quantity,itemCategory,itemprice) -> int:
    return quantity*itemprice - get_total_tax_onitems(quantity,itemCategory,itemprice)






