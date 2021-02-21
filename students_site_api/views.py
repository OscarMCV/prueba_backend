from django.db.models.query import QuerySet
from django.http import Http404
#Core Django imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
#Rest_framework imports
from users_manage_api import models as user_models
from teachers_site_api import serializers
from teachers_site_api import models
from students_site_api import serializers as student_serializers
from students_site_api import models as student_models
from users_manage_api.permissions import IsStudent
#Imports from internal apps


class CourseView(APIView):
    """
    Retrieve all the information of every course
    """
    permission_classes = [IsAuthenticated & IsStudent]
    serializer_class = serializers.CreateCourseSerializer

    def get(self, request, format=None):
        courses = models.Course.objects.all()
        serializer = serializers.CreateCourseSerializer(courses, many=True)
        return Response(serializer.data)


class LessonView(APIView):
    """
     Retrieve all the lessons in the system
     """
    permission_classes = [IsAuthenticated & IsStudent]
    serializer_class = serializers.CreateLessonSerializer
    queryset = models.Lesson.objects.all()

    def get(self, request, format=None):
        lessons = models.Lesson.objects.all()
        serializer = serializers.CreateLessonSerializer(lessons, many=True)
        return Response(serializer.data)


class QuestionView(APIView):
    """
    Retrieve all the questions in the
    system
    """
    permission_classes = [IsAuthenticated & IsStudent]
    serializer_class = serializers.CreateQuestionSerializer
    queryset = models.Question.objects.all()

    def get(self, request):
        questions = models.Question.objects.all()
        serializer = serializers.CreateQuestionSerializer(questions, many=True)
        return Response(serializer.data)


#The APIView's for the details
class CourseDetail(APIView):
    """
    Retrieve all the lessons (and their id's) of a given ID course
    Don't support post method for students
    """
    permission_classes = [IsAuthenticated & IsStudent]

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


class SolveQuestion(APIView):
    """Retrieve a question whit their answers and allows
    send the student answers"""
    permission_classes = [IsAuthenticated & IsStudent]

    def get(self, request, question_id):
        question = models.Question.objects.get(pk=question_id)
        question_serialized = student_serializers.ShowQuestionForStudentsSerializer(question)
        return Response(question_serialized.data)

    def post(self, request, question_id):
        try:
            question = models.Question.objects.get(pk=question_id)
            student_answers = request.data['answers']
            correct_answers_objects = models.Answer.objects.filter(question=question_id)
            correct_answers_boolean_list = []
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        for answers in correct_answers_objects:
            if answers.kind_answer is True:
                correct_answers_boolean_list.append(1)
            if answers.kind_answer is False:
                correct_answers_boolean_list.append(0)
        #Checking student answers
        bad_ans = 0
        answer_status = []
        grade = question.score
        for x in range(len(student_answers)):
            if student_answers[x] == correct_answers_boolean_list[x]:
                pass
            else:
                answer_status.append("fallo aqui {}, {}".format(student_answers[x], correct_answers_boolean_list[x]))
                grade = 0
                if question.type_question == 'MULTIPLECHOICE2':
                    grade = question.score
                    bad_ans = bad_ans + 1
        if bad_ans == len(correct_answers_boolean_list):
            grade = 0
        #making a related answer with all gotten data
        student_progress = student_models.StudentProgress.objects.get(name=request.user)
        RelateAnswer = student_models.RelateAnswers.objects.create(
            student=student_progress,
            question=str(question_id),
            question_grade=grade
        )
        serializer = student_serializers.RelateAnswerSerializer(RelateAnswer)
        RelateAnswer.save()
        enviar = {
            "data": serializer.data,
            "question": question.score,
            "student_answers": student_answers,
            "correct_answers": correct_answers_boolean_list,
            "status": answer_status
        }
        return Response(enviar)


class SolveLesson(APIView):
    """Retrieve the status of the lesson and
    the get method allows save the lesson, this get
    erease all the related asnwers of that lesson in the
    student object and create an lesson achivment whit
    any grade"""

    def get(self, request, lesson_id):
        return Response()


class LessonDetail(APIView):
    """
    Retrieve all the questions of a lesson and their possible
    answers
    """
    permission_classes = [IsAuthenticated & IsStudent]
    serializer_class = student_serializers.ShowQuestionForStudentsSerializer

    def get(self, request, lesson_id):
        try:
            questions = models.Question.objects.filter(lesson=lesson_id)
            serialized_questions = student_serializers.ShowQuestionForStudentsSerializer(questions, many=True)
        except models.Question.DoesNotExist:
            raise Http404
        return Response(serialized_questions.data)

