from django.core.management.base import BaseCommand
from store.models import Product, Customer, Order
from faker import Faker
import random

fake = Faker()


class Command(BaseCommand):
    help = 'Create test data for the store app'

    def handle(self, *args, **options):
        # Create 10 products
        for _ in range(10):
            Product.objects.create(
                name=fake.word(),
                price=random.uniform(1, 100)
            )

        # Create 5 customers
        for _ in range(5):
            Customer.objects.create(
                name=fake.name(),
                email=fake.email()
            )

        # Create 20 random orders
        for _ in range(20):
            product = random.choice(Product.objects.all())
            customer = random.choice(Customer.objects.all())
            quantity = random.randint(1, 10)

            Order.objects.create(
                product=product,
                customer=customer,
                quantity=quantity
            )

        self.stdout.write(self.style.SUCCESS('Test data created successfully!'))
