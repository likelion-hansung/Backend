from django import forms
from .models import Post

# class PostBaseForm(forms.Form):
#     CATEGORY_CHOICES = [
#         ('1', '일반'),
#         ('2', '계정'),
#     ]
#     image = forms.ImageField()
#     content = forms.CharField(widget=forms.Textarea)
#     category = forms.ChoiceField(choices = CATEGORY_CHOICES)
     
class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        
class PostCreateForm(PostBaseForm):
    class Meta(PostBaseForm.Meta):
        fields = ['image', 'content']
        

class PostUpdateForm(PostBaseForm):
    class Meta(PostBaseForm.Meta):
        fields = ['image', 'content']        

class PostDetailForm(PostBaseForm):
    pass