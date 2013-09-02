from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from EMDSapp.models import Specialty, SpecialtyForm, Group, GroupForm


def main_page(request):
    return redirect('/specialty')


def specialty_list(request):
    specialties = Specialty.objects.all()
    return render_to_response('specialty/list.html', locals())


def specialty_add(request):
    if request.POST:
        form = SpecialtyForm(request.POST)
        if form.is_valid():
            Specialty(title=request.POST['title']).save()
            return redirect('/specialty')
    form = SpecialtyForm()
    return render_to_response('specialty/add.html', locals())


def specialty_edit(request, id):
    if request.POST:
        form = SpecialtyForm(request.POST)
        if form.is_valid():
            specialty = Specialty(pk=id)
            specialty.title = request.POST['title']
            specialty.save()
            return redirect('/specialty')
    fid = id
    form = SpecialtyForm(instance=Specialty.objects.get(pk=id))
    return render_to_response('specialty/edit.html', locals())


def specialty_remove(request, id):
    Specialty.objects.get(pk=id).delete()
    return redirect('/specialty')


def group_list(request):
    groups = Group.objects.all()
    return render_to_response('group/list.html', locals())


def group_add(request):
    if request.POST:
        form = GroupForm(request.POST)
        if form.is_valid():
            spec = Specialty.objects.get(pk=request.POST['specialty'])
            Group(title=request.POST['title'], specialty=spec).save()
            return redirect('/group')
    form = GroupForm()
    return render_to_response('group/add.html', locals())


def group_edit(request, id):
    if request.POST:
        form = GroupForm(request.POST)
        if form.is_valid():
            group = Group(pk=id)
            group.title = request.POST['title']
            group.specialty = Specialty.objects.get(pk=request.POST['specialty'])
            group.save()
            return redirect('/group')
    fid = id
    form = GroupForm(instance=Group.objects.get(pk=id))
    return render_to_response('group/edit.html', locals())


def group_remove(request, id):
    Group.objects.get(pk=id).delete()
    return redirect('/group')
