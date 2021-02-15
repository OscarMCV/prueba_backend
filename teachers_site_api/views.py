from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from teachers_site_api import serializers
from teachers_site_api import models
from users_manage_api.permissions import IsTeacher
from students_site_api import models as student_models

"""
this is how the request works
https://docs.djangoproject.com/en/3.1/ref/request-response/#django.http.HttpRequest
"""


class CourseView(APIView):
    """
    Retrieve all the information of every course
    """
    permission_classes = [IsAuthenticated & IsTeacher]
    serializer_class = serializers.CreateCourseSerializer

    def get(self, request, format=None):
        courses = models.Course.objects.all()
        serializer = serializers.CreateCourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.CreateCourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            related_course_id = serializer.data['id']
            related_course_name = serializer.data['name']
            related_course = student_models.Related_Course.objects.create(
                id=related_course_id,
                course_name=related_course_name
            )
            related_course.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LessonView(APIView):
    """
     Retrieve all the information of ev
     """
    permission_classes = [IsAuthenticated & IsTeacher]
    serializer_class = serializers.CreateLessonSerializer
    queryset = models.Lesson.objects.all()

    def get(self, request, format=None):
        lessons = models.Lesson.objects.all()
        serializer = serializers.CreateLessonSerializer(lessons, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = serializers.CreateLessonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #The relative lesson couldn't have been saved through the serializer
            #because the ID appears when it is .save
            related_lesson_id = serializer.data['id']
            related_lesson_name = serializer.data['name']
            related_lesson = student_models.Related_Lesson.objects.create(
                id=related_lesson_id,
                lesson_name=related_lesson_name
            )
            related_lesson.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionView(APIView):
    permission_classes = [IsAuthenticated & IsTeacher]
    serializer_class = serializers.CreateQuestionSerializer
    queryset = models.Question.objects.all()

    def get(self, request):
        questions = models.Question.objects.all()
        serializer = serializers.CreateQuestionSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.CreateQuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#The APIView for the details
class CourseDetail(APIView):
    permission_classes = [IsAuthenticated & IsTeacher]

    def get(self, request, course_id):
        try:
            course = models.Course.objects.get(pk=course_id)
            course_serialized = serializers.CreateCourseSerializer(course)
            ####NEED CONVERT INTO JSON FCKING STUPID################## don't forget
            lessons = models.Lesson.objects.filter(course=course_id)
            lessons_serialized = serializers.CreateLessonSerializer(lessons, many=True)
            data = {
                "The follow lessons came from": course_serialized.data['name'],
                "lessons of the course": lessons_serialized.data,
            }
            #It has to send the lessons ID
        except models.Course.DoesNotExist:
            raise Http404
        #serializer = serializers.CreateCourseSerializer(course)
        return Response(data)

    def delete(self, request, course_id):
        all_lessons_of_this_course = models.Lesson.objects.filter(course=course_id)
        for reference in all_lessons_of_this_course:
            related_lesson = student_models.Related_Lesson.objects.get(id=reference.id)
            related_lesson.delete()
        try:
            course = models.Course.objects.get(pk=course_id)
            related_course = student_models.Related_Course.objects.get(id=str(course_id))
        except models.Course.DoesNotExist:
            raise Http404
        course.delete()
        related_course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LessonDetail(APIView):
    permission_classes = [IsAuthenticated & IsTeacher]
    serializer_class = serializers.CreateLessonSerializer
    queryset = models.Lesson.objects.all()

    def get(self, request, lesson_id):
        try:
            course = models.Course.objects.get(lessons=lesson_id)
            course_serialized = serializers.CreateCourseSerializer(course)
            lesson = models.Lesson.objects.get(pk=lesson_id)
            #Retrieve an specific lesson
            lesson_serialized = serializers.CreateLessonSerializer(lesson)
            questions = models.Question.objects.filter(lesson=lesson_id,)
            #Questions which came from "D" lessons
            question_serialized = serializers.CreateQuestionSerializer(questions, many=True)
            data = {
                'This lesson came from': course_serialized.data['name'],
                'lesson': lesson_serialized.data['name'],
                'questions': question_serialized.data
            }
            #It has to send the question id
        except models.Course.DoesNotExist:
            raise Http404
        #serializer = serializers.CreateCourseSerializer(course)
        return Response(data)

    def delete(self, request, lesson_id):
        try:
            lesson = models.Lesson.objects.get(pk=lesson_id)
            related_lesson = student_models.Related_Lesson.objects.get(id=str(lesson_id))
        except models.Lesson.DoesNotExist:
            raise Http404
        lesson.delete()
        related_lesson.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class QuestionDetail(APIView):
    """
    Gives details of a question, name, answers and kind of answers.
    also in this view is where the answers are created.
    """
    permission_classes = [IsAuthenticated & IsTeacher]
    serializer_class = serializers.CreateAnswerSerializer

    def get(self, request, question_id):
        try:
            question = models.Question.objects.get(pk=question_id)
            #Retrieve an specific question object
            question_serialized = serializers.CreateQuestionSerializer(question)
            answers = models.Answer.objects.filter(question=question_id)
            #Retrieve all the answers of the question
            answers_serialized = serializers.ShowAnswerSerializer(answers, many=True)
            data = {
                'question': question_serialized.data['the_question_is'],
                'answers': answers_serialized.data
            }
        except models.Question.DoesNotExist:
            raise Http404
        return Response(data)

    def post(self, request, question_id):
        serializer = serializers.CreateAnswerSerializer(
            data=request.data,
            context={'question_id': question_id}
        )
        #The context should give the answer serializer, the question which they belong of the answers,
        #in order to get the data to keep safe the logic of the answers
        if serializer.is_valid():
            answer, answer_message = serializer.save()
            answer_sent = serializers.ShowAnswerSerializer(answer).data
            data = {
                "answer created": answer_sent,
                "message": answer_message
            }
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(data)

    def delete(self, request, question_id):
        try:
            question = models.Question.objects.get(pk=question_id)
        except models.Question.DoesNotExist:
            raise Http404
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
