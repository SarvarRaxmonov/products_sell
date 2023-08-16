from django.urls import path
from .views import CompanyViewSet, ProductsViewSet, ReviewListView

urlpatterns = [
    path(
        "company/<int:id>/",
        CompanyViewSet.as_view({"get": "retrieve"}),
        name="company",
    ),
    path(
        "company/<int:company_id>/products",
        ProductsViewSet.as_view({"get": "list"}),
        name="product-list",
    ),
    path(
        "company/<int:company_id>/reviews",
        ReviewListView.as_view({"get": "list"}),
        name="review-list",
    ),
    path(
        "company/<int:company_id>/review-create",
        ReviewListView.as_view({"post": "create"}),
        name="review-create",
    ),
    path(
        "company/<int:comment_id>/review-update",
        ReviewListView.as_view({"put": "update", "delete": "destroy"}),
        name="review-update",
    ),
]

