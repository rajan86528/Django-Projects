from django import forms
from blog. models import BlogPost

class CreateBlogPostForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ('title','summery', 'body','category', 'status','image')
        exclude = []
