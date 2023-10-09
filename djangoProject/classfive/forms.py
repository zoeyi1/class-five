from django import forms

class InquiryForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email')
    inquiry_type = forms.ChoiceField(
        label='Type of Inquiry',
        choices=[
            ('general', 'General Inquiry'),
            ('support', 'Technical Support'),
            ('feedback', 'Feedback'),
        ]
    )
    message = forms.CharField(label='Message', widget=forms.Textarea)