from django import forms
from .models import CustomRequest


class CustomRequestForm(forms.ModelForm):
    class Meta:
        model = CustomRequest
        fields = ['package', 'platform_type', 'style_choice', 'prompt_details', 'extra_notes']
        labels = {
            'package': 'Choose a package',
            'platform_type': 'Platform',
            'style_choice': 'Style',
            'prompt_details': 'What do you need?',
            'extra_notes': 'Extra notes (optional)',
        }
        help_texts = {
            'prompt_details': 'Describe the vibe, setting, colours, outfits, camera angle… the more detail the better.',
            'extra_notes': 'Links to inspiration, deadlines, file size needs, or anything special.',
        }
        widgets = {
            'prompt_details': forms.Textarea(attrs={'rows': 5, 'placeholder': 'e.g. Cinematic headshot, golden hour lighting, shallow depth of field, soft pastel palette…'}),
            'extra_notes': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Optional extras like reference links or timing requests'}),
        }

    def clean_prompt_details(self):
        prompt_details = self.cleaned_data['prompt_details']
        if len(prompt_details) < 20:
            raise forms.ValidationError('Prompt details must be at least 20 characters long.')
        return prompt_details

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.setdefault('class', 'form-control')
        self.fields['platform_type'].empty_label = None
