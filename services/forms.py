from django import forms
from .models import CustomRequest


class CustomRequestForm(forms.ModelForm):
    class Meta:
        model = CustomRequest
        fields = ['package', 'platform_type', 'style_choice', 'prompt_details', 'extra_notes']

    def clean_prompt_details(self):
        prompt_details = self.cleaned_data['prompt_details']
        if len(prompt_details) < 20:
            raise forms.ValidationError('Prompt details must be at least 20 characters long.')
        return prompt_details