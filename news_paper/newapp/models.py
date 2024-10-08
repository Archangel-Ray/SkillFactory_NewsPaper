from allauth.account.forms import SignupForm
from django.contrib.auth.models import User, Group
from django.core.cache import cache
from django.db import models
from django.db.models import Sum
from django.urls import reverse


# Create your models here.
class Author(models.Model):
    author_user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating_author = models.SmallIntegerField(default=0)

    def update_rating(self):
        post_rat = self.post_set.all().aggregate(post_rating=Sum('rating'))
        p_rate = 0
        p_rate += post_rat.get('post_rating')

        comment_rat = self.author_user.comment_set.all().aggregate(comment_rating=Sum('rating'))
        c_rat = 0
        c_rat += comment_rat.get('comment_rating')

        self.rating_author = p_rate * 3 + c_rat
        self.save()

    def __str__(self):
        return f'{self.author_user}'


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)
    # какие пользователи на какие категории подписаны
    subscribers = models.ManyToManyField(User, blank=True, related_name='categories')

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    NEWS = 'NW'
    ARTICLE = 'AR'
    CATEGORY_CHOICES = (
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья'),
    )
    category_type = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=ARTICLE)
    date_creation = models.DateTimeField(auto_now_add=True)
    post_category = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=128)
    text = models.TextField()
    rating = models.SmallIntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[0:124] + ' ...'

    def __str__(self):
        return f'{self.title}: {self.preview()}'

    def get_absolute_url(self):
        return reverse('вывод отдельного поста', args=[str(self.id)])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        cache.delete(f'post-{self.pk}')


class PostCategory(models.Model):
    post_through = models.ForeignKey(Post, on_delete=models.CASCADE)
    category_through = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)

    def get_author_of_post(self):
        try:
            return self.comment_post.author.author_user.username
        except:
            return self.comment_user.username

    def __str__(self):
        return f'{self.text[:20]} ...'

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()


class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        common_group = Group.objects.get(name='common')
        common_group.user_set.add(user)
        return user
