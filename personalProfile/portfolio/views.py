from django.shortcuts import render
from django.http import Http404
from .models import Experience, Cert, Project, Education, Skill, Award, Image

# Defining Dictionaries
home_models = {
    'Experiences': Experience.objects.all(),
    "Educations": Education.objects.all(),
    "Projects": Project.objects.all(),
    "Skills": Skill.objects.all(),
    "Images": Image.objects.all(),
    "Certs": Cert.objects.all()
}

project_models = {
    'Images': Image.objects.all(),
    'Project': Project.objects.all(),
}

work_models = {
    'Experiences': Experience.objects.all(),
    'Images': Image.objects.all()
}

certifications_models = {
    'Awards': Award.objects.all(),
    'Certifications': Cert.objects.all(),
    'Skills': Skill.objects.all(),

}


# These are the 2 main pages, a home page with most info, and an awards/certifications page
def home(request):
    return render(request, 'portfolio/home.html', home_models)


def certs(request):
    return render(request, 'portfolio/certifications.html', certifications_models)


# These are the sub-pages, each page representing more information for either a 'work' or a project
def work_info(request, id):
    try:
        work = Experience.objects.get(id=id)
    except Experience.DoesNotExist:
        raise Http404('Experience not found')
    return render(request, 'portfolio/work_info.html', {'Experience': work, 'Images': Image.objects.all()})


def project_info(request, id):
    try:
        project = Project.objects.get(id=id)
    except Project.DoesNotExist:
        raise Http404('Project not found')
    return render(request, 'portfolio/project_info.html', {'Project': project, 'Images': Image.objects.all()})


