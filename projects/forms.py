from django import forms
from catalog.models import Product
from .models import ProjectPost


class ProjectPostCreateForm(forms.ModelForm):
    related_products = forms.ModelMultipleChoiceField(
        queryset=Product.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        required=True,
        label='Related Products'
    )

    class Meta:
        model = ProjectPost
        exclude = ('slug', 'created_at')
        labels = {
            'title': 'Title',
            'section': 'Section',
            'excerpt': 'Short description',
            'content': 'Content',
            'cover_image': 'Cover Image',
            'related_products': 'Related Products',
        }
        help_texts = {
            'excerpt': '',
            'cover_image': '',
            'related_products': 'Select the products related to this project.',
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Modern Interior Designs'}),
            'excerpt': forms.Textarea(attrs={'placeholder': 'Short summery for the project. Maximum 255 characters.'}),
            'content': forms.Textarea(attrs={'placeholder': 'Write your project article here'}),
            'cover_image': forms.ClearableFileInput(attrs={'multiple': False}),
        }
        error_messages = {
            'title': {
                'required': 'Please enter a title for your project.',
            },
            'excerpt': {
                'required': 'Please enter a short description for your project.',
                'max_length': 'Short description must be less than 255 characters.',
            },
            'content': {
                'required': 'Please enter the content for your project.',
            },
            'cover_image': {
                'required': 'Please upload a cover image for your project.',
            },
            'related_products': {
                'required': 'Please select at least one product.',
            },
        }

    def clean_title(self):
        title = self.cleaned_data['title'].strip()
        if len(title) < 5:
            raise forms.ValidationError('Title must be at least 5 characters.')
        return title


class ProjectPostUpdateForm(ProjectPostCreateForm):
    slug = forms.CharField(disabled=True, required=False, label='read-only')

    class Meta(ProjectPostCreateForm.Meta):
        exclude = ('created_at',)