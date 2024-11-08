from django.shortcuts import render

def profile_view(request):
    profile = {
        'name': 'Sasi Vaibhav',
        'bio': 'Data Science enthusiast with a background in AI & DS.',
        # Other profile fields...
    }
    skills = [
        {'name': 'Python', 'level': 'Advanced'},
        {'name': 'Java', 'level': 'Intermediate'},
        {'name': 'C', 'level': 'Intermediate'},
        {'name': 'ML', 'level': 'Advanced'},
    ]
    achievements = ['Top of the class in AI & DS', 'Certified Python Developer']
    education = ['B_Tech(AI&DS) - KLH University']
    experiences = [
        {
            'job_title': 'Data Science Intern',
            'company': 'Tech Solutions',
            'start_date': 'June 2023',
            'end_date': 'Aug 2023',
            'description': 'Worked on machine learning models for data analysis.',
        },
    ]
    projects = [
        {
            'title': 'Disease Prediction Model',
            'description': 'A machine learning project to predict diseases based on symptoms.',
            'link': 'http://example.com',
            'image': None,  # or set an image URL if you have one
        },
    ]
    return render(request, 'profile.html', {
        'profile': profile,
        'skills': skills,
        'achievements': achievements,
        'education': education,
        'experiences': experiences,
        'projects': projects
    })


def home(request):
    return render(request, 'home.html')

