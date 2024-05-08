from django.shortcuts import render
from django.http import HttpResponse

# 1 : Hello World 
def hello(request):
    return HttpResponse("hello world")


# 2 : HttpResponse
def home(request):
    return HttpResponse("""<body stye='background-color:pink'>
                        <h1 style='color:red'>heading</h1>
                        </body>
                        <p>para</p>""")


# 3 : passing a variable
def menuitem(request):
    item = "pizza"
    # HttpResponse("The item name is: "+item)
    return HttpResponse(f"The item name is: {item}") # f is used for managing the variables inside the string


# 4 : passing a list through for loop
def dishes(request):
    items = {'noodles':'Costs Rs. 100',
            'pizza':'Costs Rs. 500',
            'momos':'Costs Rs. 50'}
    
    content = "<h3>The menu items are</h3>"
    for item, desp in items.items():
        content += f"<li>{item} : {desp}</li>"
    return HttpResponse(content)


# 5 : passing a parameter to a link
def greet(request, name):
    return HttpResponse(f"Hello {name}, Welcome to our website")


# 6 : passing a parameter to check for the item in the list
def menuSearch(request, item):
    items = {'noodles':'Costs Rs. 100',
            'pizza':'Costs Rs. 500',
            'momos':'Costs Rs. 50'}
    
    if(item in items):
        content = f"{item} : {items[item]}"
    else:
        content = "Not Present"
    return HttpResponse(content)


# 7 : adding two number while user input
def addPage(request, num1, num2):
    return HttpResponse(f"Addition result: {num1+num2}")


# 8 : dynamic parameter (query urls) 
def recipe(request):
    # /recipe/?food=pizza
    food = request.GET.get('food')
    return HttpResponse(f'recipe is available for {food}')


#9 : Regular Expression
def user_profile(request, username):
    return HttpResponse(f'User profile: {username}')


#10 : rendering a simple template
def restro(request):
    items = {'menu':[{'name':'Pizza', 'cost':250},
             {'name':'French Fries', 'cost':'free'},
             {'name':'Momos', 'cost':80},
             {'name':'Chutney', 'cost':'free'},
             {'name':'Pasta', 'cost':70}]}
    return render(request, 'restro.html', items)


#11 : searching for an item in a list using route parameter
def restro2(request, item):
    items2 = {'menu':[{'name':'Pizza', 'cost':250},
             {'name':'FrenchFries', 'cost':'free'},
             {'name':'Momos', 'cost':80},
             {'name':'Chutney', 'cost':'free'},
             {'name':'Pasta', 'cost':70}]}
    selectedItem = None
    for menuItem in items2['menu']:
        if(menuItem['name'] == item):
            selectedItem = menuItem
            break
    return render(request, 'restro2.html', {'item':selectedItem})


#12 : template inheritance
def home(request):
    return render(request, 'home.html')

#12 : template inheritance
def about(request):
    return render(request, 'about.html')

items = [{'name':'Naan', 'cost':78, 'details':'Details for Naan'},
        {'name':'Idli', 'cost':30, 'details':'Details for Idli'},
        {'name':'Punugulu', 'cost':35, 'details':'Details for Punugulu'},
        {'name':'Paratha', 'cost':65, 'details':'Details for Paratha'},
        {'name':'Daal Rice', 'cost':50, 'details':'Details for Daal Rice'}]

#12 : template inheritance
def food(request):
    return render(request, 'food.html', {'items':items})


#12 : template inheritance
def detail(request, item):
    singleItem = {}
    for food in items:
        if(food['name'] == item):
            singleItem = food
            break
    data = {"item":singleItem}
    return render(request, 'detail.html', data)


#13 : simple form declaration
# probably best way is to exempt the csrf, the next function below explain the other method
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def simpleform(request):
    if request.method == 'POST':
        textbox1 = request.POST.get('textbox1')
        textbox2 = request.POST.get('textbox2')
        return HttpResponse(f"The values in the textbox are {textbox1} and {textbox2}")
    else:
        form_html = f"""
<form method="POST">
<label for="textbox1">Text Box 1:</label><br>
<input type="text" id="textbox1" name="textbox1"><br>
<label for="textbox2">Text Box 2:</label><br>
<input type="text" id="textbox2" name="textbox2"><br><br>
<input type="submit" value="Submit">
</form>
"""
    return HttpResponse(form_html)


# 14 : without exempting the csrf_token
# the syntax has three stages
from django.middleware.csrf import get_token
def simpleform2(request):
    csrf_token = get_token(request)
    if request.method == 'POST':
        textbox1 = request.POST.get('textbox1')
        textbox2 = request.POST.get('textbox2')
        return HttpResponse(f"The values in the textbox are {textbox1} and {textbox2}")
    else:
        form_html = f"""
<form method="POST">
<input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
<label for="textbox1">Text Box 1:</label><br>
<input type="text" id="textbox1" name="textbox1"><br>
<label for="textbox2">Text Box 2:</label><br>
<input type="text" id="textbox2" name="textbox2"><br><br>
<input type="submit" value="Submit">
</form>
"""
    return HttpResponse(form_html)


# 15 : performing simple addition in form
from django.middleware.csrf import get_token
def simpleform3(request):
    csrf_token = get_token(request)
    if request.method == 'POST':
        textbox1 = request.POST.get('textbox1')
        textbox2 = request.POST.get('textbox2')
        return HttpResponse(f"The added value is: {int(textbox1) + int(textbox2)}")
    else:
        form_html = f"""
<form method="POST">
<input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
<label for="textbox1">Text Box 1:</label><br>
<input type="text" id="textbox1" name="textbox1"><br>
<label for="textbox2">Text Box 2:</label><br>
<input type="text" id="textbox2" name="textbox2"><br><br>
<input type="submit" value="Submit">
</form>
"""
    return HttpResponse(form_html)


# 16 : defining a form using template
from django.views import View
class MyView(View):
    def get(self, request):
        return render(request, 'form.html')
    
    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if name and email and password:
            return HttpResponse("Form submitted successfully!")
        return render(request, 'form.html')

# 16 : defining a form using template        
def testcss(request):
    return render(request, 'testcss.html')


# 17 : validating a form
def validation(request):
    name_error = ''
    email_error = ''
    password_error = ''
    if(request.method == 'POST'):
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if not name:
            name_error = "Name is Mandatory"
        if not email:
            email_error = "Email is Mandatory"
        if not password:
            password_error = "Password is Mandatory"
            
        if name_error or email_error or password_error:
            # so that the data remains even after page reloading
            return render(request, 'validation.html',{
                'name':name,
                'email': email,
                'password':password,
                'name_error':name_error,
                'email_error':email_error,
                'password_error':password_error,
            })   
    return render(request, 'validation.html')



# 18 : creating a form using forms.py
from .forms import InputForm1
def val_django_form(request):
    submitted_details = None
    if(request.method == 'POST'):
        form = InputForm1(request.POST)
        if form.is_valid():
            submitted_details = form.cleaned_data
        else:
            return render(request, 'val_django_form.html', {'form':form, 'submitted_details':submitted_details})
    else:
        form = InputForm1()
    return render(request, 'val_django_form.html', {'form':form, 'submitted_details':submitted_details})


# 19 : models in django(creation of a record)
from .models import Customers
def signup(request):
    if(request.method == 'POST'):
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        c = Customers.objects.create(name=name, email=email, password=password)
        c.save()
        return HttpResponse("Customer account created successfully!!!")
    s = Customers.objects.all()[1]
    e = s.email
    print(s, e)
    return render(request, 'signup.html')


# 20 : using models and forms together(creation of a record) with a confirmation
from .forms import SignupForm
from .models import Signup
def Sign(request):
    account_created = False
    if(request.method == 'POST'):
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            s = Signup.objects.create(username=username, email=email, password=password)
            s.save()
            account_created = True
    else:
        form = SignupForm()
    return render(request, 'signup2.html', {'form':form, 'account_created':account_created})


# 21 : Get Cookie
def get_cookie(request):
    cookie_value = request.COOKIES.get('subjectName')
    if(cookie_value):
        return HttpResponse(f"Cookie value: {cookie_value}")
    else:
        return HttpResponse(f"Cookie not found!")
    
# 21 : Set Cookie
def set_cookie(request):
    response = HttpResponse("Cookie set!")
    response.set_cookie('subjectName', 'django', max_age=30, secure=True) # in seconds
    return response

# 21 : Delete Cookie
def delete_cookie(request):
    response = HttpResponse("Cookie deleted!")
    response.delete_cookie('subjectName')
    return response


# 22 : blogpost
from .models import Blogpost
def blogpost(request):
    post = Blogpost.objects.all()
    return render(request, 'blogpost.html', {'post':post})

#22 : blogpost
from .models import Blogpost
def blogpost2(request, id):
    post = Blogpost.objects.filter(post_id = id)[0]
    return render(request, 'blogpost.html', {'post':post})


# 23 : Setting Cookie 2
from .models import CookieDetails
def set_cookie2(request):
    if(request.method == 'POST'):
        response = HttpResponse("Cookie set!")
        textbox1 = request.POST.get('textbox1')
        # print(textbox1)
        textbox2 = request.POST.get('textbox2')
        # print(textbox2)
        response.set_cookie(textbox1, textbox2, max_age=30)
        s = CookieDetails.objects.create(cookie_name = textbox1, cookie_value = textbox2)
        s.save()
        return response
    return render(request, 'setting_cookie.html')

# 23 : Getting Cookie 2
def get_cookie2(request):
    if(request.method == 'POST'):
        textbox3 = request.POST.get('textbox3')
        cookie_value = request.COOKIES.get(textbox3)
        if(cookie_value):
            return HttpResponse(f"Cookie value: {cookie_value}")
        else:
            return HttpResponse(f"Cookie not found!") 
    return render(request, 'getting_cookie.html')


# 24 : set session
def set_session(request):
    request.session['username'] = 'pratik_kumar'
    request.session['email'] = 'kumar.pratik2402@gmail.com'
    return render(request, 'set_session.html')

# 24 : get session
def get_session(request):
    username = request.session.get('username', 'Guest')
    email = request.session.get('email', 'guest@gmail.com')
    return render(request, 'get_session.html', {'username': username, 'email': email})

# 24 : delete session
def delete_session(request):
    request.session.flush()
    return HttpResponse("Session deleted!!!")

# 25 : session part 2
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('homee')  
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

from django.contrib.auth.decorators import login_required
@login_required(login_url='/login/')
def homee(request):
    return render(request, 'homee.html', {'user': request.user})

def user_logout(request):
    logout(request)
    return redirect('login') 
