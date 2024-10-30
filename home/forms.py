from django import forms
from .models import Comments , Messsages

attrs = { 'class': 'form-control'}

class Add_Comment_Form(forms.ModelForm):
    # text = forms.CharField(widget=forms.Textarea(attrs=attrs))
    text = forms.CharField( label="Comment" ,widget=forms.Textarea(attrs=attrs))

    class Meta:
        model = Comments
        fields = ['text' ]



class Contact_Us_form(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs=attrs))
    email = forms.EmailField(widget=forms.TextInput(attrs=attrs))
    numper = forms.IntegerField(widget=forms.TextInput(attrs=attrs))
    message = forms.CharField(widget=forms.Textarea(attrs=attrs))

    class Meta:
        model = Messsages
        fields = ['name','email','numper','message' ]
