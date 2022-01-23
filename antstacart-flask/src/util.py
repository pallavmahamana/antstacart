

tax_dict = {"Medicine":5,
            "Food":5,
            "Clothes":5,
            "Music":3,
            "Imported":18,
            "Book":0}


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
    return quantity*itemprice + get_total_tax_onitems(quantity,itemCategory,itemprice)




class InvoiceGenerator():
    def __init__(self,json):
        self._json = json
        self._commodities = []
        self._total_tax = 0.0
        self._total_amount = 0.0
        self._total_amount_with_discount = 0.0


    def apply_discount(self):
        if self._total_amount > 2000:
            self._total_amount_with_discount = self._total_amount - 0.05 * self._total_amount
            return True
        else:
            self._total_amount_with_discount = self._total_amount
            return False


    def calculate_order(self):
        for item in self._json:
            self._total_amount = self._total_amount + get_total_price_ofitems(item["quantity"],
                                                                            item["itemCategory"],
                                                                            item["price"])
            self._total_tax = self._total_tax + get_total_tax_onitems(item["quantity"],
                                                                            item["itemCategory"],
                                                                            item["price"])



            self._commodities.append(
                {
                    "item":item["item"],
                    "itemCategory":item["itemCategory"],
                    "quantity":item["quantity"],
                    "itemprice":item["price"],
                    "finalprice":get_total_price_ofitems(item["quantity"],
                                                        item["itemCategory"],
                                                        item["price"]),
                    "tax_amount":get_total_tax_onitems(item["quantity"],
                                                        item["itemCategory"],
                                                        item["price"])
                }
            )
        
        





