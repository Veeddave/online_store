# store/queries.py

from django.db import connection

def best_selling_products():
    with connection.cursor() as cursor:
        cursor.execute("SELECT product_id, SUM(quantity) as total_sold FROM store_order GROUP BY product_id ORDER BY total_sold DESC LIMIT 5;")
        result = cursor.fetchall()
    return result
