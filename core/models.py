from django.db import models
from django.contrib.auth.models import User


class Tweet(models.Model):
    note = models.CharField(max_length=280)
    created_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.note

    def set_note(self, str):
        self.note = str

    def split_post(self):
        splitted = {}
        x = 0
        while x < len(self.note):
            substr, end, hashtag = self.get_substring(self.note[x:])
            splitted.update({substr: hashtag})
            x += end
        return splitted

    def get_substring(self, str):
        if str[0] != '#':
            end = str.find('#')
            if end == -1:
                end = len(str)
            return str[0:end], end, False
        else:
            for x in range(1, len(str)):
                if str[x] == '#' or str[x] == ' ' or x == len(str)-1:
                    if x == len(str)-1:
                        return str[0:x+1], x+1, True
                    return str[0:x], x, True

    def view_count(self):
        return Like.objects.filter(post=self).count()


class Hashtag(models.Model):
    tag = models.CharField(max_length=18)
    posts = models.ManyToManyField(Tweet)


class Like(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING)
    post = models.ForeignKey(Tweet, null=True, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)
