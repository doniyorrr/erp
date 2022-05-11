from django.contrib import admin
from django.urls import path, include
from core.views import front

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt import views as jwt_views




schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
   ),
   public=True,
)

urlpatterns = [
   path('admin/', admin.site.urls),
   path('api/market/', include('market.urls')),
   path('api/product/', include('product.urls')),
   path('api/sale/', include('sale.urls')),
   path('api/users/', include('users.urls')),

   path('api/', include('rest_framework.urls')),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path("", front, name="front"),
   path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

   

]