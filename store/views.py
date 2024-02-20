# store/views.py
import io
import base64
from django.db.models import Sum, F
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Product, Customer, Order
from .serializers import ProductSerializer, CustomerSerializer, OrderSerializer
import matplotlib.pyplot as plt

class ProductList(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class CustomerList(APIView):
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

class OrderList(APIView):
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

class TotalRevenue(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Calculate total revenue
        total_revenue = Order.objects.aggregate(total=Sum(F('product__price') * F('quantity')))['total']

        # Assuming a total budget of 1000
        remaining_budget = 1000

        # Ensure non-negative values for the pie chart
        values = [max(total_revenue, 0), max(remaining_budget - total_revenue, 0)]

        # Create a pie chart
        labels = ['Total Revenue', 'Remaining']
        plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
        plt.title('Total Revenue Analysis')

        # Save the chart to a BytesIO object
        image_stream = io.BytesIO()
        plt.savefig(image_stream, format='png')
        image_stream.seek(0)
        plt.close()

        # Encode the image to base64
        image_base64 = base64.b64encode(image_stream.read()).decode('utf-8')

        # Return the total revenue and chart image data
        return Response({'total_revenue': total_revenue, 'chart_image': image_base64})

class APIRoot(APIView):
    def get(self, request):
        return Response({
            'products': '/api/products/',
            'customers': '/api/customers/',
            'orders': '/api/orders/',
            'total_revenue': '/api/total-revenue/',
            'api_root': '/api/',  # Added a default API root
        })
