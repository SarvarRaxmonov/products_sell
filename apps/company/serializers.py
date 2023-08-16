from rest_framework import serializers
from .models import Company, Product, Review


class CompanySerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = Company
        fields = ("image", "name", "reviews", "average_rate", "count_of_reviews")

    def get_reviews(self, obj):
        data = {
            "5 reviews count": Review.objects.filter(company=obj.id, rate=5).count(),
            "4 reviews count": Review.objects.filter(company=obj.id, rate=4).count(),
            "3 reviews count": Review.objects.filter(company=obj.id, rate=3).count(),
            "2 reviews count": Review.objects.filter(company=obj.id, rate=2).count(),
            "1 reviews count": Review.objects.filter(company=obj.id, rate=1).count(),
        }
        return data


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("name", "price", "discount")


class ReviewSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="profile.user", read_only=True)
    image = serializers.CharField(source="profile.image", read_only=True)

    class Meta:
        model = Review
        fields = ("id", "username", "profile", "image", "company", "rate", "comment")
