

# Create your views here.

# appname/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateContactForm, UpdateContactForm, DeleteContactForm, ReadContactForm
from .models import Contact
from django.http import HttpResponse

def create_contact(request):
    if request.method == 'POST':
        form = CreateContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_info')
    else:
        form = CreateContactForm()
    return render(request, 'myapp3/create_contact.html', {'form': form})

def failure(request):
    return render(request, 'myapp3/failure.html')

def menu(request):
    return render(request, 'myapp3/menu.html')

def display_info(request):
    # Query the database to retrieve all contacts
    contacts = Contact.objects.all()
    
    # Pass the contacts to the template as part of the context
    context = {
        'title': 'Display Info Page',
        'contacts': contacts,  # Add contacts to the context
    }
    
    return render(request, 'myapp3/display_info.html', context)


def update_contact(request):
    contact = None
    update_form = None

    contact_id = request.POST.get('contact_id')  # Get contact_id from POST
    if contact_id:
        try:
            contact = Contact.objects.get(pk=contact_id)
            update_form = UpdateContactForm(request.POST, instance=contact)
            if request.method == 'POST' and update_form.is_valid():
                # Check if the form is valid
                print("Form is valid")
                update_form.save()  # Commit changes to the database
                return redirect('display_info')
            else:
                # Print form errors for debugging
                print("Form errors:", update_form.errors)
        except Contact.DoesNotExist:
            # Contact with the provided ID does not exist, redirect to failure view
            return redirect('failure')
    else:
        print("No contact ID provided")

    return render(request, 'myapp3/update_contact.html', {'update_form': update_form, 'contact': contact})




def delete_contact(request):
    if request.method == 'POST':
        form = DeleteContactForm(request.POST)
        if form.is_valid():
            contact_id = form.cleaned_data['contact_id']
            try:
                contact = Contact.objects.get(pk=contact_id)
                # Contact with the provided ID exists, continue normally
                contact.delete()
                return redirect('display_info')
            except Contact.DoesNotExist:
                # Contact with the provided ID does not exist, redirect to failure view
                return redirect('failure')
    else:
        form = DeleteContactForm()

    return render(request, 'myapp3/delete_contact.html', {'form': form})

def read_contact(request):
    if request.method == 'POST':
        form = ReadContactForm(request.POST)
        if form.is_valid():
            contact_id = form.cleaned_data['contact_id']
            try:
                contact = Contact.objects.get(pk=contact_id)
                # Contact with the provided ID exists, continue normally
                return render(request, 'myapp3/read_contact.html', {'contact': contact})
            except Contact.DoesNotExist:
                # Contact with the provided ID does not exist, redirect to failure view
                return redirect('failure')
    else:
        form = ReadContactForm()

    return render(request, 'myapp3/read_contact.html', {'form': form})




