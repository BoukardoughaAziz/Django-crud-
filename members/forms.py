from django import forms
from .models import Member

class MembersForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'

        # label = {
        # "title" : "Title",
        # "description" : "Description",
        # }

        # widgets ={
        # "title" : forms.TextInput(attrs={"placeholder":"Buy Groceries"}),
        # "description" : forms.TextInput(attrs={"placeholder":"Visit super market and buy some groceries"}), 
        # }