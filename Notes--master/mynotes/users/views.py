from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib import messages



class RegisterView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')  # Redirect to login page after registration

    def form_valid(self, form):
        # Optionally, add a success message
        messages.success(self.request, "Your account has been successfully created.")
        return super().form_valid(form)

    def form_invalid(self, form):
        # Optionally, add an error message
        messages.error(self.request, "There was an error with your registration. Please try again.")
        return super().form_invalid(form)