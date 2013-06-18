from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

from . import forms
from . import models


def project_list(request):
    projects = models.Project.objects.all()
    context = {'projects': projects}
    return render(request, "codereader/project_list.html", context)


def project_details(request, slug):
    project = models.Project.objects.get(slug=slug)
    context = {'project': project}
    return render(request, "codereader/project_details.html", context)


def project_add(request):
    form = forms.ProjectForm(request.POST or None)
    if form.is_valid():
        project = form.save()
        return redirect(reverse("project_details", args=(project.slug, )))
    context = {'form': form}
    return render(request, "codereader/project_form.html", context)


def repository_show(request, slug, repo_id):
    repository = models.Repository.objects.get(pk=repo_id)
    context = {'repository': repository}
    return render(request, "codereader/repository_details.html", context)


def repository_add(request, slug):
    project = models.Project.objects.get(slug=slug)
    form = forms.RepositoryForm(request.POST or None, project=project)
    if form.is_valid():
        form.save()
        return redirect(reverse("project_details", args=(slug, )))
    context = {'form': form}
    return render(request, "codereader/repository_form.html", context)
