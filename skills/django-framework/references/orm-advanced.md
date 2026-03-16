# Django ORM Advanced Techniques

Advanced database querying, optimization, and custom managers in Django ORM.

---

## Query Optimization

### select_related (ForeignKey, OneToOne)

```python
# Bad: N+1 queries
posts = Post.objects.all()
for post in posts:
    print(post.author.name)  # Separate query for each author

# Good: Single JOIN query
posts = Post.objects.select_related('author').all()
for post in posts:
    print(post.author.name)  # No additional queries
```

### prefetch_related (ManyToMany, Reverse ForeignKey)

```python
# Bad: N+1 queries
articles = Article.objects.all()
for article in articles:
    print(article.tags.all())  # Separate query for each article

# Good: Two queries total
articles = Article.objects.prefetch_related('tags').all()
for article in articles:
    print(article.tags.all())  # Uses prefetched data
```

### only() and defer()

```python
# Fetch only specific fields
posts = Post.objects.only('title', 'created_at')

# Defer heavy fields
posts = Post.objects.defer('content')
```

---

## Complex Queries

### Q Objects

```python
from django.db.models import Q

# OR queries
Post.objects.filter(Q(title__icontains='django') | Q(content__icontains='django'))

# Complex conditions
Post.objects.filter(
    Q(published=True) & (Q(author__username='john') | Q(author__username='jane'))
)

# NOT queries
Post.objects.filter(~Q(published=True))
```

### F Expressions

```python
from django.db.models import F

# Compare fields
Post.objects.filter(views__gt=F('likes') * 2)

# Update based on current value
Post.objects.update(views=F('views') + 1)
```

### Aggregation

```python
from django.db.models import Count, Avg, Sum, Max, Min

# Aggregate across all objects
Post.objects.aggregate(
    total=Count('id'),
    avg_views=Avg('views'),
    total_likes=Sum('likes')
)

# Annotate each object
authors = Author.objects.annotate(
    post_count=Count('posts'),
    avg_views=Avg('posts__views')
)
```

---

## Custom Managers

```python
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(published=True)

class Post(models.Model):
    title = models.CharField(max_length=200)
    published = models.BooleanField(default=False)
    
    objects = models.Manager()  # Default manager
    published_objects = PublishedManager()  # Custom manager

# Usage
Post.published_objects.all()  # Only published posts
```

---

## Raw SQL

```python
# Raw queries
posts = Post.objects.raw('SELECT * FROM blog_post WHERE published = %s', [True])

# Execute custom SQL
from django.db import connection

with connection.cursor() as cursor:
    cursor.execute("UPDATE blog_post SET views = views + 1 WHERE id = %s", [post_id])
    cursor.execute("SELECT * FROM blog_post WHERE views > %s", [100])
    rows = cursor.fetchall()
```

---

## Database Functions

```python
from django.db.models.functions import Lower, Upper, Concat, Length

# String functions
Post.objects.annotate(title_lower=Lower('title'))

# Concatenation
Author.objects.annotate(
    full_name=Concat('first_name', models.Value(' '), 'last_name')
)

# Length
Post.objects.filter(title__length__gt=50)
```

---

## Transactions

```python
from django.db import transaction

# Atomic decorator
@transaction.atomic
def create_post_with_tags(title, content, tags):
    post = Post.objects.create(title=title, content=content)
    for tag_name in tags:
        tag, _ = Tag.objects.get_or_create(name=tag_name)
        post.tags.add(tag)
    return post

# Context manager
with transaction.atomic():
    post = Post.objects.create(title='Test')
    post.tags.add(tag)
```

---

## Database Indexes

```python
class Post(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(unique=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['published', '-created_at']),
            models.Index(fields=['author', 'published']),
        ]
```
