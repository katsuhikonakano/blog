from django.db import models

# Create your models here.
class Category(models.Model):

    name = models.CharField('カテゴリ名', max_length=50)
    created_at = models.DateTimeField('作成日', auto_now_add=True)

    def __str__(self):
        return self.name

class Tag(models.Model):

    name = models.CharField('タグ名', max_length=50)
    created_at = models.DateTimeField('作成日', auto_now_add=True)
 
    def __str__(self):
        return self.name

class Post(models.Model):

    title = models.CharField('タイトル', max_length=100)
    content = models.TextField('本文')
    thumnail = models.ImageField('サムネイル', upload_to='images/', null=True, blank=True)
    image = models.ImageField('画像', upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField('作成日',auto_now_add=True)
    updated_at = models.DateTimeField('更新日',auto_now=True)
    tag = models.ManyToManyField(Tag, blank=True, verbose_name="タグ")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="カテゴリ")

    class Meta:
        ordering = ['-created_at']
    

    def __str__(self):
        return self.title