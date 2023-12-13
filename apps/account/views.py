from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from django.http import Http404

from .serializers import (
    RegistrationSerializer,
    ChangePasswordSerializer,
    RestorePasswordSerializer,
    SetRestoredPasswordSerializer,
    UserRetrieveSerializer
    )


User = get_user_model()

class RegistrationView(APIView):
    def post(self, request: Request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                'Thank you for registration! Activate your account.', 
                status=status.HTTP_201_CREATED
            )
        

class UserRetrieveView(APIView):
    def get(self, request: Request, username):
        user = User.objects.get(username=username)
        serializer = UserRetrieveSerializer(user).data
        try:
            return Response(serializer)
        except User.DoesNotExist:
            raise Http404
        

class EmailActivationView(APIView):   
    def get(self, request, activation_code):
        user = User.objects.filter(activation_code=activation_code).first()
        if not user:
            return Response(
                'Page not found.' ,
                status=status.HTTP_404_NOT_FOUND
                )
        user.is_active = True       
        user.activation_code = ''
        user.save()
        return Response(
            'Account activated. You can login now.',
            status=status.HTTP_200_OK
            )


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request: Request):
        serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.set_new_password()
            return Response(
                'Password was changed successfully.',  
                status=status.HTTP_200_OK
            )


class RestorePasswordView(APIView): 
    def post(self, request):  
        serializer = RestorePasswordSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.send_code()
            return Response(
                'The code has been sent to your email.',   
                status=status.HTTP_200_OK
            )


class SetRestoredPasswordView(APIView):  
    def post(self, request: Request): 
        serializer = SetRestoredPasswordSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.set_new_password()
            return Response(
                'Password was restored successfully.',  
                status=status.HTTP_200_OK
            )


class DeleteAccountView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request: Request):
        username = request.user.username
        User.objects.get(username=username).delete()
        return Response(
            'Your account is deleted.',                 
            status=status.HTTP_204_NO_CONTENT
        )