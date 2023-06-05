from django.shortcuts import render
from rest_framework import viewsets,generics
from rest_framework.response import Response
from .models import Patient, Test , LabTest
from .serializers import PatientSerializer, TestSerializer ,LabTestSerializer
from rest_framework.views import APIView
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from rest_framework import status

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

""" class LabTestCreateView(generics.CreateAPIView):
    queryset = LabTest.objects.all()
    serializer_class = LabTestSerializer """
 
""" class LabTestCreateView(generics.CreateAPIView):
    queryset = LabTest.objects.all()
    serializer_class = LabTestSerializer

    def get(self, request, *args, **kwargs):
        patient_id = request.query_params.get('patient')
        try:
            lab_test = self.queryset.get(patient_id=patient_id)
            serializer = self.get_serializer(lab_test)
            return Response(serializer.data)
        except LabTest.DoesNotExist:
            return Response({'detail': 'Lab test not found for the given patient.'}, status=status.HTTP_404_NOT_FOUND) """

class LabTestCreateView(generics.ListCreateAPIView):
    queryset = LabTest.objects.all()
    serializer_class = LabTestSerializer

    """ def get(self, request, *args, **kwargs):
        patient_id = request.query_params.get('patient')
        lab_test = self.queryset.filter(patient_id=patient_id).first()

        if lab_test:
            serializer = self.get_serializer(lab_test)
            return Response(serializer.data)
        else:
            return Response({'detail': 'Lab test not found for the given patient.'}, status=status.HTTP_404_NOT_FOUND)
     """
    
class PrintBillView(APIView):
    def get(self, request):
        patient_id = request.query_params.get('patient')
        lab_tests = LabTest.objects.filter(patient__id=patient_id)  # Use double underscore "__" for field lookups
        serializer = LabTestSerializer(lab_tests, many=True)
        return Response(serializer.data)



""" In the PatientViewSet, override the create method to handle the POST request. 
It validates the incoming data using the serializer, performs the creation of the patient record, 
and returns the serialized data in the response with a status of 201 (Created).

In the TestViewSet,  override the list method to handle the GET request. It retrieves the 
queryset of all test records, serializes the data, and returns it in the response."""

""" Now, when I make a POST request to the /patients/ endpoint, it will create a new patient
record in the database. And when you make a GET request to the /tests/ endpoint, it will retrieve
all the test records from the database. """

class LabHeadLoginView(APIView):
    def post(self, request):
        
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active and user.is_staff:
            login(request, user)
            return Response({'message': 'Lab head logged in successfully.'})
        return Response({'message': 'Invalid credentials or lab head account not found.'}, status=401)

""" class PatientLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return Response({'message': 'Patient logged in successfully.'})
        return Response({'message': 'Invalid credentials or patient account not found.'}, status=401) """

""" LabHeadLoginView and PatientLoginView are implemented as APIView subclasses. The post method 
handles the login functionality for the lab head and patient. It retrieves the username and password 
from the request data, authenticates the user, and logs them in if the authentication is successful.
"""


class LabHeadSignUpView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if username and password:
            user = User.objects.create_user(username=username, password=password)
            user.is_staff = True
            user.save()
            return Response({'message': 'Lab head created successfully.'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Invalid data provided.'}, status=status.HTTP_400_BAD_REQUEST)


class PatientLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active and not user.is_staff:
            login(request, user)
            return Response({'message': 'Patient logged in successfully.'})
        return Response({'message': 'Invalid credentials or patient account not found.'}, status=401) 



class PatientSignUpView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if username and password:
            user = User.objects.create_user(username=username, password=password)
            user.is_patient = True
            user.save()
            return Response({'message': 'Patient created successfully.'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Invalid data provided.'}, status=status.HTTP_400_BAD_REQUEST)






