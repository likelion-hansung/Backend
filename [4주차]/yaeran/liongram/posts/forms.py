from django.core.exceptions import ValidationError
from django import forms
from .models import Post

# class PostBaseForm(forms.Form):
#     image = forms.ImageField()
#     content = forms.CharField(widget=forms.Textarea)

class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

class PostCreateForm(PostBaseForm):
    class Meta(PostBaseForm.Meta):
        fields = ['image', 'content']

        def clean_content(self):
            data = self.cleaned_data['content']
            if "비속어" == data:
                raise ValidationError("'비속어'는 사용하실 수 없습니다.")

class PostUpdateForm(PostBaseForm):
    class Meta(PostBaseForm.Meta):
        fields = ['image', 'content']

class PostDetailForm(PostBaseForm):
    def __init__(self, *args, **kwargs):
        super(PostDetailForm, self).__init__(*args, **kwargs)
        for key in self.fields:
            self.fields[key].widget.attrs['disabled'] = True