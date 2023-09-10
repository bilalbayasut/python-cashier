import pytest

from Transaction import Transaction


@pytest.fixture
def transaction():
    return Transaction()


def test_add_item(transaction):
    transaction.add_item("Ayam Goreng", 2, 20000)
    transaction.add_item("Pasta Gigi", 3, 15000)
    assert transaction.items == [
        {"item_name": "Ayam Goreng", "item_qty": 2, "item_price": 20000},
        {"item_name": "Pasta Gigi", "item_qty": 3, "item_price": 15000},
    ]
    assert transaction.total_price == 85000


def test_update_item_name(transaction):
    transaction.add_item("Ayam Goreng", 2, 20000)
    transaction.update_item_name("Ayam Goreng", "Ayam Bakar")
    assert transaction.items == [
        {"item_name": "Ayam Bakar", "item_qty": 2, "item_price": 20000}
    ]


def test_update_item_qty(transaction):
    transaction.add_item("Ayam Goreng", 2, 20000)
    transaction.update_item_qty("Ayam Goreng", 3)
    assert transaction.items == [
        {"item_name": "Ayam Goreng", "item_qty": 3, "item_price": 20000}
    ]
    assert transaction.total_price == 60000


def test_update_item_price(transaction):
    transaction.add_item("Ayam Goreng", 2, 20000)
    transaction.update_item_price("Ayam Goreng", 25000)
    assert transaction.items == [
        {"item_name": "Ayam Goreng", "item_qty": 2, "item_price": 25000}
    ]
    assert transaction.total_price == 50000


def test_delete_item(transaction):
    transaction.add_item("Ayam Goreng", 2, 20000)
    transaction.add_item("Pasta Gigi", 3, 15000)
    transaction.delete_item("Ayam Goreng")
    assert transaction.items == [
        {"item_name": "Pasta Gigi", "item_qty": 3, "item_price": 15000}
    ]
    assert transaction.total_price == 45000


def test_reset_transaction(transaction):
    transaction.add_item("Ayam Goreng", 2, 20000)
    transaction.add_item("Pasta Gigi", 3, 15000)
    transaction.reset_transaction()
    assert transaction.items == []
    assert transaction.total_price == 0


def test_check_order_valid(transaction):
    transaction.add_item("Ayam Goreng", 2, 20000)
    transaction.add_item("Pasta Gigi", 3, 15000)
    result = transaction.check_order()
    assert result == "Pemesanan sudah benar"


def test_check_order_invalid(transaction):
    with pytest.raises(ValueError):
        transaction.add_item("Ayam Goreng", None, 20000)
        transaction.check_order()


def test_total_price_before_discount(transaction):
    transaction.add_item("Ayam Goreng", 2, 20000)
    transaction.add_item("Pasta Gigi", 3, 15000)
    total_price = transaction.total_price_before_discount()
    assert total_price == 85000


def test_total_price_after_discount(transaction):
    transaction.add_item("Ayam Goreng", 2, 200)
