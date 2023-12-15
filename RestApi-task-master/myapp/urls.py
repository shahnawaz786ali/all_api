from django.urls import path
from myapp import views

urlpatterns = [
    path("",views.index,name="index"),
    path("add-category",views.AddCategory,name="AddCategory"),
    path("get-product-data",views.GetProductData,name="Getproductdata"),
    path("create-product-data",views.CreateProductData,name="CreateProductData"),
    path("edit-product-data/<int:id>",views.EditProductData,name="EditProductdata"),
    path("del-product-data/<int:id>",views.DeleteProductData,name="DeleteProductdata"),
    path('send-excel-file', views.SendEmail, name='SendEmail'),
    path('list-of-product', views.ProductList, name='ProductList'),
    path('schedule-email', views.ScheduleEmail, name='ScheduleEmail'),
    
]
    
    