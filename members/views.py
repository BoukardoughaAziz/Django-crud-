from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render,redirect
from .forms import MembersForm
from .models import Member

def members(request):
  # template = loader.get_template('FirstView.html')
  # return HttpResponse(template.render())²
  return render (request, 'FirstView.html',{'name':'John'})



def test (request) :
  return HttpResponse('Hello World')


def AddMember(request):
  form = MembersForm
  if request.method == 'POST':
    form = MembersForm(request.POST)
    if form.is_valid():
         form.save()
         return redirect("/members/test")
  else:
    form = MembersForm()

  return render(request, 'AddMember.html', {'form': form})


def DisplayMemebrs(request):
   members = Member.objects.all()
   return render(request, 'DisplayMembers.html', {'members': members})


def UpdateMemebers(request,id):
  member = Member.objects.get(id=id)
  form = MembersForm(instance=member)
  if request.method == 'POST':
    form = MembersForm(request.POST, instance=member)
    if form.is_valid():
      form.save()
      return redirect("/members/display")
  return render(request, 'UpdateMember.html', {'form': form})


def DeleteMember(request,id):
  member = Member.objects.get(id=id)
  member.delete()   
  return redirect("/members/display")
  

