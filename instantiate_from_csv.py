import csv
import gc
class Customers:
    obj_lst = []
    def __init__(self,cus_id,f_name,l_name,email,phone):
        self.cus_id = cus_id
        self.f_name = f_name
        self.l_name = l_name
        self.email = email
        self.phone = phone
        Customers.obj_lst.append(self)

    @classmethod
    def csv_instantiate(cls,filename):
        with open(filename) as f:
            reader = csv.DictReader(f)
            list_of_data = list(reader)

        for data in list_of_data:
            Customers(
                cus_id=data.get("User Id"),
                f_name=data.get("First Name"),
                l_name=data.get("Last Name"),
                email= data.get("Email"),
                phone=data.get("Phone")
            )
    def __repr__(self) -> str:
        return f"Customers({self.f_name}, {self.l_name}, {self.email}, {self.phone})"

class Products:
    obj_lst = []
    def __init__(self,prod_id,prod_name,prod_supplier,price,quantity,category):
        self.prod_id = prod_id
        self.prod_name = prod_name
        self.prod_supplier = prod_supplier
        self.price = price
        self.quantity = quantity
        self.category = category
        Products.obj_lst.append(self)

    @classmethod
    def csv_instantiate(cls,filename):
        with open(filename) as f:
            reader = csv.DictReader(f)
            list_of_data = list(reader)

        for data in list_of_data:
            Products(
                prod_id=data.get("productid"),
                prod_name=data.get("product name"),
                prod_supplier=data.get("product supplier"),
                price= data.get("price"),
                quantity=data.get("quantity"),
                category =data.get("category")
            )
    def __repr__(self) -> str:
        return f"Products({self.prod_id}, {self.prod_name}, {self.prod_supplier}, {self.price},{self.quantity},{self.category})"
class Orders:
    obj_lst = []
    def __init__(self,order_id,date_of_order,cus_id,productid):
        self.order_id = order_id
        self.date_of_order = date_of_order
        self.cus_id = cus_id
        self.productid = productid
        Orders.obj_lst.append(self)

    @classmethod
    def csv_instantiate(cls,filename):
        with open(filename) as f:
            reader = csv.DictReader(f)
            list_of_data = list(reader)

        for data in list_of_data:
            Orders(
                order_id=data.get("order-id"),
                date_of_order=data.get("date-of-order"),
                cus_id=data.get("cus_id"),
                productid= data.get("productid"),
            )
    def __repr__(self) -> str:
        return f"Products({self.order_id}, {self.date_of_order}, {self.cus_id}, {self.productid})"


