# https://teamsparta.notion.site/ada2aa44da1f490ea9dacb67f1ee7e4c
# 카페에서 손님이 바리스타에게 메뉴를 주문하는 과정을 객체지향 코드로 만들어보기
""" 
다음 코드를 읽어보고 Customer, Barista 클래스의 action 메소드를 요구사항에 맞게 오버라이딩하여 기능을 구현해보세요.
요구사항은 Customer, Barista 클래스의 action 메소드에 독스트링으로 기재되어 있습니다.
"""


class MenuItem:
    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients

    def __str__(self):
        return f"{self.name}: {self.price}원"


class Menu:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, item):
        """메뉴에 메뉴 아이템 객체 추가"""
        self.items[item_name] = item

    def show_menu(self):
        """메뉴에 저장된 모든 아이템을 출력"""
        for key in self.items:
            print(self.items[key])

    def get_items(self):
        """메뉴에 저장된 모든 아이템을 딕셔너리 형태로 리턴"""
        return self.items

    def get_item(self, item_name):
        """{item_name}의 value, 메뉴 아이템 객체를 리턴"""
        return self.items[item_name]


class InventoryItem:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}: {self.quantity}"

    def add_quantity(self, quantity):
        """아이템의 수량 증가"""
        self.quantity += quantity

    def remove_quantity(self, quantity):
        """아이템의 수량 감소. 결과가 0개 미만일 경우 에러"""
        if self.quantity - quantity < 0:
            raise ValueError(f"{self.name}이 충분하지 않습니다. [{self.quantity}]")
        self.quantity -= quantity


class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, item):
        """인벤토리에 인벤토리 아이템 객체 추가"""
        self.items[item_name] = item

    def get_items(self):
        """인벤토리에 저장된 모든 아이템을 딕셔너리 형태로 리턴"""
        return self.items

    def get_item(self, item_name):
        """{item_name}의 value, 인벤토리 아이템 객체를 리턴"""
        return self.items[item_name]

    def add_item_quantity(self, item_name, quantity):
        """인벤토리에 {item_name}를 key로 등록된 인벤토리 아이템 객체의 수량 증가"""
        self.items[item_name].add_quantity(quantity)

    def remove_item_quantity(self, item_name, quantity):
        """인벤토리에 {item_name}를 key로 등록된 인벤토리 아이템 객체의 수량 감소"""
        self.items[item_name].remove_quantity(quantity)


class Person:
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory

    def action(self, param):
        pass

    def info(self):
        """Person 객체의 이름, 인벤토리 정보를 출력"""
        print(f"이름 : {self.name}")
        print("소지품")
        items = self.inventory.get_items()
        for key in items:
            print(items[key])


class Customer(Person):
    def __init__(self, name, inventory):
        super().__init__(name, inventory)
        self.order = None

    # 주문
    def action(self, order_item):
        money = self.inventory.get_item("money")
        if money.quantity < order_item.price:
            raise ValueError("현금이 부족해..")
        else:
            self.order = order_item

class Barista(Person):
    def __init__(self, name, inventory):
        super().__init__(name, inventory)

    # 커피 제조
    def action(self, customer):
        order_item = customer.order
        print(f"{order_item.name} 주문 확인했습니다")
        for item_name, quantity in order_item.ingredients.items():
            # 재료가 충분하지 않다면 InventoryItem property에서 에러 발생하므로 바리스타 인벤토리에서 재료 빼기
            self.inventory.remove_item_quantity(item_name, quantity)
            
        self.inventory.add_item_quantity("money", order_item.price)
        customer.inventory.remove_item_quantity("money", order_item.price)
        print(f"주문하신 {order_item.name} 나왔습니다.")
        # customer.order = None 나중에 주문번호? 개념 접목시 사용
        
    def get_income(self):
        """Barista 객체가 보유한 money를 리턴"""
        return self.inventory.get_item("money")


# 카페 메뉴 생성
menu = Menu()
menu.add_item("americano", MenuItem(
    "Americano", 3000, {"bean": 2, "water": 2}))
menu.add_item("latte", MenuItem("Latte", 3000, {"bean": 2, "milk": 2}))
print("--메뉴 정보--")
menu.show_menu()

# 고객 생성
customer_inventory = Inventory()
customer_inventory.add_item("money", InventoryItem("Money", 10000))
customer = Customer("철수", customer_inventory)
print("--고객 정보--")
customer.info()

# 바리스타 생성
barista_inventory = Inventory()
barista_inventory.add_item("water", InventoryItem("Water", 20))
barista_inventory.add_item("bean", InventoryItem("Bean", 20))
barista_inventory.add_item("milk", InventoryItem("Milk", 10))
barista_inventory.add_item("money", InventoryItem("Money", 0))
barista = Barista("민수", barista_inventory)
print("--바리스타 정보--")
barista.info()

# 주문
customer.action(menu.get_item("americano"))

# 커피 제조
barista.action(customer)

# 정보 확인
print("--고객 정보--")
customer.info()
print("--바리스타 정보--")
barista.info()
print("")
print(f"바리스타 수입 : {barista.get_income()}")
