from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.db import models
from django.db.models import Avg


class Company(models.Model):
    image = models.ImageField(upload_to="images/")
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name

    def average_rate(self):
        return self.review_company.aggregate(avg_rate=Avg("rate"))["avg_rate"]

    def count_of_reviews(self):
        return self.review_company.filter(company=self.id).count()


class Product(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    price = models.BigIntegerField(default=0)
    discount = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to="profile_images/")

    def __str__(self):
        return f"{self.user.username}"


class Review(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="review_company"
    )
    rate = models.IntegerField(default=0, validators=[MaxValueValidator(5)])
    comment = models.TextField()

    def __str__(self):
        return self.comment
