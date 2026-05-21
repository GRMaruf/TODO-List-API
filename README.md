# TODO-List-API

Basic TODO API for practice.

### Implementations

* Class Based View (ListCreateAPIView, RetrieveUpdateDestroyAPIView, and ModelViewSet)
* API Versioning
* Swagger/OpenAPI/Redoc Documentation Applied using `drf_spectacular`

# What is Swagger/OpenAPI?

Swagger provides:

* Interactive API documentation
* API testing UI
* Automatic endpoint documentation

Instead of manually writing docs, Django generates them automatically.

Example:

```text
https://yourdomain.com/swagger/
```

You get:

* all endpoints
* request bodies
* response formats
* testing interface

---

# Best package for Django REST Framework

Use:

```text
drf-spectacular
```

It is modern and OpenAPI 3 compatible.

---

# 1. Install package

```bash
pip install drf-spectacular
```

---

# 2. Add to INSTALLED_APPS

In `settings.py`

```python
INSTALLED_APPS = [
    ...
    'drf_spectacular',
]
```

---

# 3. Configure DRF

Add this in `settings.py`

```python
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}
```

---

# 4. Add Swagger settings

Still in `settings.py`

```python 
SPECTACULAR_SETTINGS = {
    'TITLE': 'My API',
    'DESCRIPTION': 'Simple Django REST API',
    'VERSION': '1.0.0',
}
```

---

# 5. Configure URLs

In main `urls.py`

```python
from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('api.urls')),

    # OpenAPI schema
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),

    # Swagger UI
    path(
        'swagger/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    ),

    # ReDoc UI
    path(
        'redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc',
    ),
]
```

---

# 6. Run server

```bash
python manage.py runserver
```

---

# 7. Open Swagger

Visit:

```text
http://127.0.0.1:8000/swagger/
```

You’ll now see:

* beautiful API docs
* test buttons
* endpoint details
* request/response schemas

---

# 8. Example with your API

Your endpoint:

```text
GET /api/
```

Swagger automatically documents:

* method
* fields
* serializer structure

---

# 9. Add endpoint descriptions

You can improve documentation.

Example:

```python
from drf_spectacular.utils import extend_schema

@extend_schema(
    description="Get all products",
    summary="Product List API"
)
@api_view(['GET'])
def product_list(request):
    ...
```

You can document methods individually.

```python
from drf_spectacular.utils import extend_schema_view, extend_schema

@extend_schema_view(

    get=extend_schema(
        summary="Get Products",
        description="Returns all products"
    ),

    post=extend_schema(
        summary="Create Product",
        description="Creates a new product"
    )

)
class ProductListCreateView(ListCreateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```

---

# 10. Document POST body automatically

If using serializers properly:

```python
serializer = ProductSerializer(data=request.data)
```

Swagger auto-generates input fields.

---

# 11. Production deployment

After deployment:

```text
https://yourdomain.com/swagger/
```

works automatically.

---

# 12. Why Swagger is important

Professional backend developers use it because:

* frontend developers understand APIs quickly
* APIs become testable
* easier debugging
* looks professional
* essential for teams

---

# 13. Difference

| Tool            | Purpose                   |
| --------------- | ------------------------- |
| OpenAPI         | Standard/specification    |
| Swagger UI      | Interactive documentation |
| drf-spectacular | Django implementation     |

---

# 14. Optional: Add authentication in Swagger

Later you can add:

* JWT auth button
* Bearer tokens
* API key auth

Very useful for real projects.

---

# Bonus — Custom actions

If you use:

```python
@action(detail=True)
```

You can document those too.

Example:

```python
from rest_framework.decorators import action
from rest_framework.response import Response

class ProductViewSet(ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @extend_schema(
        summary="Mark product as featured",
        tags=["Products"]
    )
    @action(detail=True, methods=['post'])
    def feature(self, request, pk=None):

        return Response({"message": "featured"})
```

---

# One important tip

For Swagger/OpenAPI quality:

Always define:

* serializers properly
* response schemas
* validation rules

Swagger becomes much more powerful when serializers are clean.
