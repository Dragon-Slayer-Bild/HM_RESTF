from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.viewsets import ModelViewSet

from lms.models import Сourse, Lesson
from lms.serializers import LessonSerializer, СourseSerializer, СourseDetailSerializer


class СourseViewSet(ModelViewSet):
    queryset = Сourse.objects.all()
    filterset_fields = ['id', 'name']

    def get_serializer_class(self):
        if self.action == "retrieve":
            return СourseDetailSerializer
        return СourseSerializer


class LessonCreateApiView(CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonlistApiView(ListAPIView):
    queryset = Lesson.objects.all()
    filterset_fields = ['id', 'name']
    serializer_class = LessonSerializer



class LessonRetrieveApiView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonUpdateApiView(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonDestroyApiView(DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
