from django.shortcuts import render

from projects.models import ProjectPost


def projects_list(request):
    project = ProjectPost.objects.all()

    sections = request.GET.get('section')
    if sections in (ProjectPost.BATH, ProjectPost.KITCHEN):
        project = project.filter(section=sections)

    context = {
        'projects': project,
        'section': sections,
    }

    return render(request, 'projects/projects_list.html', context)

def project_detail(request, slug):

    context = {
        "slug": slug
    }

    return render(request, "projects/project_detail.html", context)
