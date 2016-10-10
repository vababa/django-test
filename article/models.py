from django.db import models
from django.utils.html import format_html

# Create your models here.
class Article(models.Model):
    class Meta:
        db_table = 'article'
    article_title = models.CharField(max_length = 200)
    article_text = models.TextField()
    article_date = models.DateTimeField()
    article_likes = models.IntegerField(default = 0)

    def colored_title(self):
        return format_html(
            '<span style="color: #11ff12;">{}</span>',
            self.article_title,
        )
    colored_title.short_description = 'Article Title'


class Comments(models.Model):
    class Meta():
        db_table = 'comments'
    comments_text = models.TextField(verbose_name='Текст комментария')
    comments_article = models.ForeignKey(Article)