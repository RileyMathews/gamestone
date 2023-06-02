from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.views.generic import View
from .models import User
import uuid

class TemporaryLoginView(View):
    def get(self, request):
        return render(request, "identity/temporary_login.html")

    def post(self, request):
        user = User.objects.create_user(uuid.uuid4(), is_demo_user=True)
        login(request, user, backend="django.contrib.auth.backends.ModelBackend")
        next_url = request.GET.get("next")
        return redirect(next_url)
