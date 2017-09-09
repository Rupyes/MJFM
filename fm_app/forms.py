from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Name' , required=True,
                        widget=forms.TextInput(attrs={'placeholder': "Your Name", 'class':'form-control'}))
    address = forms.CharField(max_length=256, label='Address', required=True,
                            widget=forms.TextInput(attrs={'placeholder':"Your Address", 'class':'form-control'}))
    email = forms.EmailField(label="Email", required=True,
                            widget=forms.TextInput(attrs={'placeholder':"Email Address", 'class':'form-control'}))
    text = forms.CharField(label="Message", required=True,
                            widget=forms.Textarea(attrs={'placeholder': "Messages", 'class':'form-control'}))
