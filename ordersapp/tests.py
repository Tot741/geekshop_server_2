from django.test import TestCase
from ordersapp.models import Order, OrderItem
from mainapp.models import Product, ProductCategory
from authapp.models import User
from datetime import datetime


class ProductsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='Vasya')
        self.order = Order.objects.create(user=self.user, created=datetime, updated=datetime, status='FM')
        self.category = ProductCategory.objects.create(name="стулья")
        self.product_1 = Product.objects.create(name="стул 1",
                                                category=self.category,
                                                price=1999.5,
                                                quantity=150)

        self.product_2 = Product.objects.create(name="стул 2",
                                                category=self.category,
                                                price=2998.1,
                                                quantity=125)

        self.product_3 = Product.objects.create(name="стул 3",
                                                category=self.category,
                                                price=998.1,
                                                quantity=115)
        self.orderitem_1 = OrderItem.objects.create(order=self.order,
                                                    product=self.product_1,
                                                    quantity=1)
        self.orderitem_2 = OrderItem.objects.create(order=self.order,
                                                    product=self.product_2,
                                                    quantity=1)
        self.orderitem_3 = OrderItem.objects.create(order=self.order,
                                                    product=self.product_3,
                                                    quantity=1)

    def test_get_total_quantity(self):
        self.assertEqual(self.order.get_total_quantity(), 3)

    def test_get_product_type_quantity(self):
        self.assertEqual(self.order.get_product_type_quantity(), 3)

    def test_get_total_cost(self):
        self.assertEqual(self.order.get_total_cost(), 5995.7)

