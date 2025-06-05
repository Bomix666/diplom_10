from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Непроверенное'),
        ('approved', 'Проверенное'),
    ]
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField()
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)
    categories = models.ManyToManyField(Category, related_name='events')
    tags = models.ManyToManyField(Tag, related_name='events', blank=True)
    region = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Source(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='sources')
    url = models.URLField()
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.url

class Comment(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Комментарий от {self.author} к событию {self.event.title}"
