from django import forms
from posts.models import Comment, Post, Category, Tag

class PostForm(forms.Form):
    image = forms.ImageField(required=False)
    title = forms.CharField(max_length=100)
    content = forms.CharField(max_length=100)

    def clean_title(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        if title.lower() == "javascript":
            raise forms.ValidationError("Javascrip is not allowed")
        return title
    
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        content = cleaned_data.get("content")
        if title and content and (title.lower() == content.lower()):
            raise forms.ValidationError("Title and content should be different")
        return cleaned_data
    
class SearchForm(forms.Form):
    q = forms.CharField(max_length=100, required=False, label="Search")
    category_id = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
    tag_ids = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False)
    orderings = (
        ("created", "По дате"),
        ("-created", "По дате (по убыванию)"),
        ("updated", "По обновления"),
        ("-updated", "По обновления (по убыванию)"),
        ("title", "По названию"),
        ("-title", "По названию (по убыванию)"),
        ("rate", "По рейтенгу"),
        ("-rate", "По рейтингу (по убыванию)"),
        (None, None)
    )

    ordering = forms.ChoiceField(choices=orderings, required=False)

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ( "image", "title", "content","category")


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']