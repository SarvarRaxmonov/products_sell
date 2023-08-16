from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Company, Product, Review, Profile
from .serializers import CompanySerializer, ProductSerializer, ReviewSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    lookup_field = "id"


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, company_id=None, *args, **kwargs):
        instance = self.get_queryset().filter(company=company_id)
        serializer = self.get_serializer(instance, many=True)

        return Response(serializer.data)


class ReviewListView(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def list(self, request, company_id=None, *args, **kwargs):
        instance = self.get_queryset().filter(company=company_id)
        serializer = self.get_serializer(instance, many=True)

        return Response(serializer.data)

    def update(self, request, comment_id=None, *args, **kwargs):
        profile = Profile.objects.get(user=request.user.id)
        instance_check = self.get_queryset().filter(profile=profile.id, id=comment_id)
        if instance_check:
            serializer = self.get_serializer(
                instance=instance_check, data=request.data, partial=True
            )
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        else:
            return Response("you have not access to update this comment")

    def destroy(self, request, comment_id=None, *args, **kwargs):
        profile = Profile.objects.get(user=request.user.id)
        instance_check = self.get_queryset().filter(profile=profile.id, id=comment_id)
        if instance_check:
            self.perform_destroy(instance_check)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("you have not access to delete this comment")
