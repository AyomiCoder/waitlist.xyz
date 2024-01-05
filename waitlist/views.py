
from django.shortcuts import render, redirect
from .forms import WaitlistForm

def waitlist_signup(request):
    if request.method == 'POST':
        form = WaitlistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Redirect to the success page
    else:
        form = WaitlistForm()

    return render(request, 'waitlist/signup.html', {'form': form})

# Add this line
def success_page(request):
    return render(request, 'waitlist/success.html')