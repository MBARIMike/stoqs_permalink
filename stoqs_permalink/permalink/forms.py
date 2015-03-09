from django import forms

class PermalinkForm(forms.Form):
    parameters = forms.CharField()

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass
