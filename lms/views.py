from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.viewsets import ModelViewSet

from lms.models import Сourse
from lms.serializers import LessonSerializer, СourseSerializer


class СourseViewSet(ModelViewSet):
    queryset = Сourse.objects.all()
    serializer_class = СourseSerializer


class LessonCreateApiView(CreateAPIView):
    queryset = Сourse.objects.all()
    serializer_class = LessonSerializer


class LessonlistApiView(ListAPIView):
    queryset = Сourse.objects.all()
    serializer_class = LessonSerializer


class LessonRetrieveApiView(RetrieveAPIView):
    queryset = Сourse.objects.all()
    serializer_class = LessonSerializer


class LessonUpdateApiView(UpdateAPIView):
    queryset = Сourse.objects.all()
    serializer_class = LessonSerializer


class LessonDestroyApiView(DestroyAPIView):
    queryset = Сourse.objects.all()
    serializer_class = LessonSerializer
