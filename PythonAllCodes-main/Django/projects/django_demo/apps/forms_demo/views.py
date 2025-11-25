from django.shortcuts import render
from .forms import ContactForm


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return render(request, 'forms_demo/success.html', {'name': form.cleaned_data['name']})
    else:
        form = ContactForm()

    return render(request, 'forms_demo/form.html', {'form': form})
