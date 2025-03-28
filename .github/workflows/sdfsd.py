class ConveyorBelt:  # 🏭 Конвейер на заводе
    def __init__(self):
        self.orders = []  # 📦 Заказы — это детали на конвейере

    def add_item(self, item):  # 🛠️ Добавляем деталь на конвейер
        self.orders.append(item)

    def process_items(self):  # 🔄 Обрабатываем детали
        for item in self.orders:
            print(f"🔧 Обрабатываем деталь: {item}")
