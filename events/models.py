from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='uploads/', blank=True)

    def __str__(self):
        return self.title


class Review(models.Model):

    class Rating(models.IntegerChoices):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5

    rating = models.IntegerField(choices=Rating.choices)
    text = models.TextField()

    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, blank=True, null=True, related_name="reviews")
    profile = models.ForeignKey(
        "accounts.UserProfile", on_delete=models.CASCADE, blank=True, related_name="reviews")

    def __str__(self):
        return self.text
