from django import forms
from django_recaptcha.fields import ReCaptchaField


class InquiryForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    email = forms.EmailField(label="Email")
    inquiry_type = forms.ChoiceField(
        label="Type of Inquiry",
        choices=[
            ("General", "General Inquiry"),
            ("Training", "Training Opportunities"),
            ("Feedback", "Feedback"),
            ("Partnership", "Brand Partnerships"),
        ],
    )
    captcha = ReCaptchaField()
    message = forms.CharField(label="Message", widget=forms.Textarea)
