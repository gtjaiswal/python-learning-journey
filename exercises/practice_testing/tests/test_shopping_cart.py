import pytest
from shopping_cart import ShoppingCart

# class TestShoppingCart:

@pytest.fixture(autouse=True)
def setup_teardown():
    shopping_cart = ShoppingCart()
    shopping_cart.add_item("item 1", 100)
    shopping_cart.add_item("item 2", 200)
    shopping_cart.add_item("item 3", 300)
    yield shopping_cart
@pytest.fixture
def empty_cart():
    return ShoppingCart()

# @pytest.fixture
# def cart_with_items():
#         shopping_cart = ShoppingCart()
#         shopping_cart.add_item("item 1", 100)
#         shopping_cart.add_item("item 2", 200)
#         shopping_cart.add_item("item 3", 300)
#         return shopping_cart

def test_empty_cart_add_item(empty_cart):
        empty_cart.add_item("empty_cart_item", 100)
        assert empty_cart.get_item_count() == 1

def test_cart_with_items_get_total(cart_with_items):
        assert cart_with_items.get_total() == 600

def test_cart_with_items_get_item_count(cart_with_items, empty_cart):
        assert cart_with_items.get_item_count() == 3
        empty_cart.add_item("empty_cart_item", 100)
        assert empty_cart.get_item_count() == 1
