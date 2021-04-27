from django.shortcuts import render,redirect
from users.forms import RegisterForm


# def login(request):
#     return render(request, "login.html")
# aici am incercat sa definesc view-ul
# Create your views here.
def register_view(request):
    if request.method == 'GET':
        form=RegisterForm()
    else:
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'users/register.html', {'form': form})
