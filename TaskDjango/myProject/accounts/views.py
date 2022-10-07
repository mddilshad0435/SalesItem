from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.views import View
from .forms import CustomerRegistrationForm, LoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import Item,Employee
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

class Signup(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/signup.html', {'form':form})
    
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = User(username=name)
            user.set_password(password)
            user.save()
            
            return redirect('home')
            
        return render(request, 'app/signup.html', {'form':form})
    
def Home(request):
    user = request.user
    if user.is_authenticated:
        employee = Employee.objects.get(user=user.id)
        print("employee",employee)
        item = Item.objects.filter(Requisition_By=employee.id)

        page = request.GET.get('page')
        print(item,"sdjfbsdjfbsdf")
        paginator = Paginator(item, 2)
        
        page_obj = paginator.get_page(page)


        # try:
        #     items = paginator.page(page)
        # except PageNotAnInteger:
        #     items = paginator.page(1)
        # except EmptyPage:
        #     items = paginator.page(paginator.num_pages)
        # print(items)
        return render(request,'app/index.html',{'page': page_obj})
    return render(request,'app/index.html')

class LoginView(View):
    def get(self,request):
        form = LoginForm()
        return render(request,'app/login.html',{'form':form})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)

            return redirect('home')
        
        return redirect('login')
@method_decorator(csrf_exempt,name='dispatch')
class AddItems(View):
    def post(self,request):
        data={}
        print("wuidu3eh",request.POST)
        Item_Code = request.POST['Item_Code']
        Item_name = request.POST['Item_name']
        Item_Measurement = request.POST['Item_Measurement']
        Item_stock = request.POST['Item_stock']
        Item_Image = request.FILES['Item_Image']
        Supplier_name = request.POST['Supplier_name']
        employeeName = request.POST['employee_name']
        print("emmppp9========+++",employeeName)
        employee = Employee.objects.filter(id=employeeName).first()
        print("emmppp9+++",employee)
        
        employee = Item.objects.create(Item_Code=Item_Code,Item_name=Item_name,Item_Measurement=Item_Measurement,Item_stock=Item_stock,Item_Image=Item_Image,Supplier_name=Supplier_name,Requisition_By=employee)
        return redirect('home')
    def get(self, request):
        employee = Employee.objects.filter(user=request.user)
        print("employee",employee)
        return render(request, 'app/additems.html',{'employee':employee})

class EditItems(View):
    def post(self,request,id):
        item = Item.objects.get(id=id)
        item.Item_Code = request.POST['Item_Code']
        item.Item_name = request.POST['Item_name']
        item.Item_Measurement = request.POST['Item_Measurement']
        item.Item_stock = request.POST['Item_stock']
        item.Item_Image = request.FILES['Item_Image']
        item.Supplier_name = request.POST['Supplier_name']
        item.Requisition_By = Employee.objects.filter(id=request.POST['employee_name']).first()
        item.save()
        print("+++++++++++++",item)
        # employee = Employee.objects.filter(id=employeeName).first()
        # print("emmppp9+++",employee)
        
        
        print("updated")
        return redirect('home')
    def get(self, request,id):
        print(id)
        item = Item.objects.get(id=id)
        print("item",item)
        employee = Employee.objects.filter(user=request.user)
        return render(request, 'app/edititems.html',{'item':item,'employee':employee})