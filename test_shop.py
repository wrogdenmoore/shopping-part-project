from shopping_cart_project import to_usd

def test_to_usd():
    result = to_usd(10)
    assert result ==10.60

from shopping_cart_project import human_friendly_timestamp 

def test_human_friendly_timestamp():
    result = human_friendly_timestamp()
    assert result == '19-05-09'
# from shop_cart_final import find_product

# def test_find_product():
#     result = find_product(1)
#     assert result == "Chocolate Sandwich Cookies"
