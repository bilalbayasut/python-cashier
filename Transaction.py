class Transaction:
    def __init__(self):
        self.transaction_id = None
        self.items = []
        self.total_price = 0

    def add_item(self, item_name, item_qty, item_price):
        self.items.append({
            'item_name': item_name,
            'item_qty': item_qty,
            'item_price': item_price
        })
        self.update_total_price()

    def update_item_name(self, old_item_name, new_item_name):
        for item in self.items:
            if item['item_name'] == old_item_name:
                item['item_name'] = new_item_name

    def update_item_qty(self, item_name, new_item_qty):
        for item in self.items:
            if item['item_name'] == item_name:
                item['item_qty'] = new_item_qty
                self.update_total_price()

    def update_item_price(self, item_name, new_item_price):
        for item in self.items:
            if item['item_name'] == item_name:
                item['item_price'] = new_item_price
                self.update_total_price()

    def delete_item(self, item_name):
        self.items = [item for item in self.items if item['item_name'] != item_name]
        self.update_total_price()

    def reset_transaction(self):
        self.items = []
        self.total_price = 0

    def check_order(self):
        for item in self.items:
            if not item['item_name'] or not item['item_qty'] or not item['item_price']:
                return "Terdapat kesalahan input data"
        return "Pemesanan sudah benar"

    def update_total_price(self):
        self.total_price = sum(item['item_qty'] * item['item_price'] for item in self.items)

    def total_price_before_discount(self):
        return self.total_price

    def total_price_after_discount(self):
        if self.total_price >= 500000:
            return self.total_price * 0.9
        elif self.total_price >= 300000:
            return self.total_price * 0.92
        elif self.total_price >= 200000:
            return self.total_price * 0.95
        else:
            return self.total_price

    def print_transaction(self):
        table_header = "| No | Nama Item | Jumlah Item | Harga/Item | Total Harga |\n"
        table_divider = "|----|-----------|-------------|------------|-------------|\n"
        table_rows = ""
        for i, item in enumerate(self.items, start=1):
            row = f"| {i}  | {item['item_name']}     | {item['item_qty']:^11} | {item['item_price']:^10} | {item['item_qty'] * item['item_price']:^11} |\n"
            table_rows += row
        return table_header + table_divider + table_rows
