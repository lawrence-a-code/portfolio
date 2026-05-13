from django.shortcuts import render



def home(request):

    context = {
        'name': 'Lawrence A.', 
        'title': 'Python Developer',
        'about': 'B.Sc Computer Science Student | Django Specialist',
        'Dob':'04 - 02 - 2006',
    }
    return render(request, 'index.html', context)
