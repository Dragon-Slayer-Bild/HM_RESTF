from rest_framework.serializers import ModelSerializer, SerializerMethodField

from lms.models import Lesson, Сourse


class LessonSerializer(ModelSerializer):

    class Meta:
        model = Lesson
        fields = "__all__"


class СourseSerializer(ModelSerializer):
    lessons = LessonSerializer(many=True,read_only=True)

    class Meta:
        model = Сourse
        fields = "__all__"

class СourseDetailSerializer(ModelSerializer):
    lessons_count = SerializerMethodField()
    lessons = LessonSerializer(source='lesson_set', many=True, read_only=True)


    def get_lessons_count(self,course):
        return Lesson.objects.filter(course_id=course.pk).count()

    class Meta:
        model = Сourse
        fields = ("name","description","lessons_count", "lessons")




