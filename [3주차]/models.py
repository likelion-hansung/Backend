from django.db import models

# N 테이블에 field 정의
class Post(models.Model):
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True,null=True)
    tags = models.ManyToManyField('Tag', blank=True)
    title = models.CharField('TITLE',max_length=50)
    description = models.CharField('DESCRIPTION', max_length=100,blank=True, help_text='simple one-line text.')
    image = models.ImageField('IMAGE',upload_to='blog/%Y/%m/',blank=True,null=True)
    content = models.TextField('CONTENT')
    create_dt = models.DateTimeField('CREATE DT',auto_now_add=True)
    update_dt = models.DateTimeField('UPDATE DT', auto_now=True)
    like = models.PositiveSmallIntegerField('LIKE',default=0)

    def __str__(self):
        return self.title

class Category(models.Model): # P:C = N : 1
    name = models.CharField(max_length=50,unique=True)
    description = models.CharField('DESCRIPTION',max_length=100,blank=True,help_text='simple one-line text.')

    def __str__(self):
        return self.name

class Tag(models.Model): # P:T = N : N
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Comment(models.Model): # P:C = 1 : N
    post = models.ForeignKey(Post,on_delete=models.CASCADE,blank=True,null=True)
    content = models.TextField('CONTENT')
    create_dt = models.DateTimeField('CREATE DT',auto_now_add=True)
    update_dt = models.DateTimeField('UPDATE DT',auto_now=True)

    @property
    def short_content(self):
        return self.content[:10]
    def __str__(self):
        return self.short_content
