from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

# Create your views here.
def contact(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

         #  Check if user has made inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(name=name, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made your order, for change order please contact the chefs phone number!')
                return redirect('contact')
           
        
        contact = Contact(user_id=user_id, name=name, email=email, phone=phone, message=message)

        contact.save()

        # Send email
        # send_mail(
        #     'Food menu order',
        #     'You have recieve message to your email for food order ' + contact.message + '. Sign into the admin panel for more info',
        #     '1234567890.gtest@gmail.com',
        #     ['sentmessage@gmail.com'],
        #     fail_silently=False
           
        # )

        messages.success(request, 'Your order has been submitted, we will contact you to confirm and for additional order!')
        return redirect('contact')
    return render(request, 'contacts.html')
