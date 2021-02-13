from rest_framework import serializers

from teachers_site_api import models


class HelloSerializer(serializers.Serializer):
    """Create a serializer for a request in my HelloApiView"""
    name = serializers.CharField(max_length=10)
    """
    the last serializer is used for test purposes
    """


class CreateCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ['name', 'id']


class CreateLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lesson
        fields = ['course', 'name', 'description', 'order', 'id']


class CreateQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Question
        fields = [
            'lesson',
            'order',
            'type_question',
            'GoodAnswers',
            'BadAnswers',
            'score',
            'the_question_is',
            'id'
        ]

    def validate(self, data):
        """
        validates the cohesion between the amount of answers
        and the type of question, before of create a question
        """
        NumberGoodAnswers = data['GoodAnswers']
        NumberBadAnswers = data['BadAnswers']
        if NumberBadAnswers == 0:
            raise serializers.ValidationError('The 0 value is not allowed for BadAnswers')
        if NumberGoodAnswers == 0:
            raise serializers.ValidationError('The 0 value is not allowed for GoodAnswers')
        if NumberGoodAnswers > 1 and data['type_question'] == 'BOOLEAN':
            raise serializers.ValidationError('Boolean answers only can have one correct answer')
        if NumberBadAnswers > 1 and data['type_question'] == 'BOOLEAN':
            raise serializers.ValidationError('Boolean answers only can have one bad answer')
        if NumberGoodAnswers > 1 and data['type_question'] == 'MULTIPLECHOICE1':
            raise serializers.ValidationError('Multiple Choice 1 only can have a single good answer')
        return data

    def create(self, validated_data):
        """Generate a question object"""
        return models.Question.objects.create(**validated_data)


class CreateAnswerSerializer(serializers.ModelSerializer):
    """
        Asumsions: the models requires to storage any value in NumberGoodAnswers so
            -NumberGoodAnswers cannot be empty
            -NumberBadAnswers cannot be empty
            **The CreateQuestions of the Questions serialzer make sure:
                -Boolean only can have 1 GoodAnswer and 1 BadAnswer
                -MultimpleChoice1 only Can have 1 Good answe
        The AnswerSerializer has to:
        1-Verify the actual amount of good answers
        2.-Verify the actual amount of bad answes
    """
    class Meta:
        model = models.Answer
        fields = ['id', 'question', 'answer', 'kind_answer']

    def validate(self, data):
        query = models.Question.objects.get(pk=self.context['question_id'])
        #The question object is storaged in self.context
        answers = models.Answer.objects.filter(question=data["question"])
        #Retrieve all the objectis which match with the question UUID value
        #answers is a list which contains objects type models.Answer
        actual_GoodAnswers = 0
        actual_BadAnswers = 0
        for answer_object in answers:
            if answer_object.kind_answer is True:
                actual_GoodAnswers = actual_GoodAnswers + 1
            actual_BadAnswers = actual_BadAnswers + 1
        if actual_GoodAnswers == query.GoodAnswers:
            raise serializers.ValidationError('The amount of Good Answers has been reached')
        if actual_BadAnswers == query.BadAnswers:
            raise serializers.ValidationError('The amount of Bad Answers has been reached')
        return data

    def create(self, validated_data):
        return models.Answer.objects.create(**validated_data)
        #####IF U DON'T WRITE FCKN REEEETUUUURNNNNN THE OBJECT DON'T WILL BE SAVED
