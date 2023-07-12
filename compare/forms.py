from django import forms


class ProductForm(forms.Form):
    title = forms.CharField(label="Title", max_length=100)
    name = forms.CharField(label="Name", max_length=255)
    price = forms.FloatField(label="Price", max_length=10)
    description = forms.CharField(label="Description", max_length=1000, required=False, widget=forms.Textarea)
    image_url = forms.URLField(required=False)
