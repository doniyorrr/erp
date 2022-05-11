from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from rest_framework import views
from rest_framework.response import Response
from .serializers import MyTokenObtainPairSerializer


class LoginView(views.APIView):
    # This view should be accessible also for unauthenticated users.
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = serializers.LoginSerializer(data=self.request.data,
            context={ 'request': self.request })
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(None, status=status.HTTP_202_ACCEPTED)


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (IsAuthenticated,)
    serializer_class = MyTokenObtainPairSerializer


