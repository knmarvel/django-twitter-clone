from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.views import View
from authentication.forms import LoginForm


class Login_View(View):
    html = "login_form.html"
    form_class = LoginForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.html, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request,
                username=data['username'],
                password=data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage'))
                )


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))
