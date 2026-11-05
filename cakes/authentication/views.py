
from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth import authenticate

from .serializers import ProfileSerializers

from rest_framework_simplejwt.tokens import RefreshToken

from decouple import config

from cakes.utils import send_mail

import threading

class LoginView(APIView):

    def post(self, request, *args, **kwargs):

        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(
            username=username,
            password=password
        )

        if user is None:
            return Response(
                {'error': 'Invalid username or password'},
                status=401
            )

        refresh_token = RefreshToken.for_user(user)

        access_token = refresh_token.access_token

        data = {
            'access token': str(access_token),
            'refresh token': str(refresh_token)
        }

        return Response(data, status=200)


class RegisterView(APIView):

    serializer_class = ProfileSerializers

    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            username = serializer.validated_data.get('username')

            password=serializer.validated_data.get('password')

            profile = serializer.save()

            profile.email = username
            
            profile.set_password(password)

            profile.save()

            recipient = profile.email

            subject = 'Welcome Abroad,Sweet moments awaits at CakeTales!'

            template = 'emails/registration.html'

            context = {'name':profile.first_name,'email':recipient,'login_url':config('LOGIN_URL')}

            #send_mail(recipient,subject,template,context)

            thread = threading.Thread(target=send_mail,args=(recipient,subject,template,context))

            thread.start()

            data = {

                'msg': 'Data created successfully'
            }

            return Response(data, status=200)

        return Response(serializer.errors, status=400)
