from django.urls import path,include
#from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, TestViewSet, LabHeadLoginView, PatientLoginView,LabHeadSignUpView,PatientSignUpView,LabTestCreateView,PrintBillView



""" router = DefaultRouter()
router.register(r'patients', PatientViewSet, basename='patient')
router.register(r'tests', TestViewSet, basename='test') """



urlpatterns = [
    #path('', include(router.urls)),
    path('patients/', PatientViewSet.as_view({'get': 'list','post': 'create'}), name='patient-create'),
    path('tests/', TestViewSet.as_view({'get': 'list'}), name='test-list'),
    path('labhead/login/', LabHeadLoginView.as_view(), name='labhead-login'),
    path('patient/login/', PatientLoginView.as_view(), name='patient-login'),
    path('signup/lab-head', LabHeadSignUpView.as_view(), name='lab_head_signup'),
    path('signup/patient', PatientSignUpView.as_view(), name='patient_signup'),
    path('labtests/create/', LabTestCreateView.as_view(), name='labtest-create'),
    path('print-bill/', PrintBillView.as_view(), name='print-bill'),
]








