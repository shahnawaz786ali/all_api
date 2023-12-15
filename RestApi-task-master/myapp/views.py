from django.shortcuts import render,HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializer import UserSerializer,CategorySerializer, ProductSerializer
from django.core.mail import send_mail
from .models import Category, Product, User
from django.core.mail import EmailMessage
from django.conf import settings
import openpyxl
from .tasks import test_func    
from django.core.cache import cache
# Create your views here.

def index(request):
    return render(request,'index.html')


@api_view(['POST'])
def AddCategory(request):
    try: 
        if request.method == 'POST':
                serializer = CategorySerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                else:
                    return Response(serializer.errors)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def GetProductData(request):
    mydata = Product.objects.all()
    serializer = ProductSerializer(mydata,many = True)
    return Response(serializer.data)

@api_view(['POST'])
def CreateProductData(request):
    try:
        if request.method == 'POST':
                serializer = ProductSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                else:
                    return Response(serializer.errors)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            
@api_view(['PUT'])
def EditProductData(request,id):
    try : 
        mydata = Product.objects.get(pk=id)
        if request.method == 'PUT':
            serializer = ProductSerializer(mydata,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def DeleteProductData(request,id):
    try:
        if request.method == 'DELETE':
            mydata = Product.objects.get(pk=id)
            mydata.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def SendEmail(request):
    try:
        users = User.objects.all()
        filename = 'myfile.xlsx'
        workbook = openpyxl.Workbook()
        worksheet = workbook.active
        worksheet.title = 'UserData'
        header = ['ID', 'Name', 'Is Active']
        worksheet.append(header)

        for user in users:
            row = [user.id, user.name, user.is_active]
            worksheet.append(row)
        workbook.save(filename)
        if request.method == 'POST':
            data = request.data.get('email')
            test_func.delay(email=data,filename=filename)
        return Response({'success': True})
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def ProductList(request):
    key = "all_products"
    products = cache.get(key)
    if not products:
        products = Product.objects.all()
        cache.set(key, products)
    serializer = ProductSerializer(products,many = True)
    return Response(serializer.data)

@api_view(['POST'])
def ScheduleEmail(request):
    try:
        users = User.objects.all()
        filename = 'myfile.xlsx'
        workbook = openpyxl.Workbook()
        worksheet = workbook.active
        worksheet.title = 'UserData'
        header = ['ID', 'Name', 'Is Active']
        worksheet.append(header)

        for user in users:
            row = [user.id, user.name, user.is_active]
            worksheet.append(row)
        workbook.save(filename)
        if request.method == 'POST':
            data = request.data.get('email')
            test_func.apply_async(args = [data,filename], countdown=120)
        return Response({'success': True})
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)