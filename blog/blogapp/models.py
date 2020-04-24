from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    userid = models.CharField(max_length=32)
    username = models.CharField(max_length=32)
    pwd = models.CharField(max_length=128)
    sex = models.ImageField(choices=((0, '女'), (1, u'男'), (2, None)), verbose_name=u'性别', default=2)
    created_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='创建时间')

    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.id


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    articleTitle=models.CharField(max_length=128)
    articleContent=models.TextField()
    created_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='发布')
    User_id=models.ForeignKey(User,to_field='id',on_delete=models.CASCADE)

    class Meta:
        verbose_name=u'文章'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.articleTitle

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    userId=models.ForeignKey(User,to_field='id',on_delete=models.CASCADE)
    commentContent=models.TextField()
    created_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='发布')
    articleId=models.ForeignKey(Article,to_field='id',on_delete=models.CASCADE)

    class Meta:
        verbose_name=u'评论'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.userId