from rest_framework import serializers

from teachers_site_api import models


class CreateCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ['name', 'id']


class CreateLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lesson
        fields = ['course', 'name', 'the_lesson_is', 'order', 'id']


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
        question = models.Question.objects.get(pk=self.context['question_id'])
        lol1 = data['question']
        lol2 = question.the_question_is

        if str(lol1) != str(lol2):
            send = "This doesn't works=>{uno}context=>{dos}".format(
                uno=lol1,
                dos=lol2
            )
            raise serializers.ValidationError(send)
        #The question object is storaged in self.context
        answers = models.Answer.objects.filter(question=data["question"])
        #Retrieve all the objectis which match with the question UUID value
        #answers is a list which contains objects type models.Answer
        actual_GoodAnswers = 0
        actual_BadAnswers = 0
        try:
            if len(answers) != 0:
                #Meas there is one or more answer objects
                for answer_object in answers:
                    if answer_object.kind_answer is True:
                        actual_GoodAnswers = actual_GoodAnswers + 1
                    else:
                        actual_BadAnswers = actual_BadAnswers + 1
                if actual_GoodAnswers == question.GoodAnswers and data['kind_answer'] is True:
                    raise serializers.ValidationError('The amount of Good Answers has been reached')
                if actual_BadAnswers == question.BadAnswers and data['kind_answer'] is False:
                    raise serializers.ValidationError('The amount of Bad Answers has been reached')
                if data['kind_answer'] is True:
                    self.context['GoodAnswers'] = question.GoodAnswers - actual_GoodAnswers - 1
                    self.context['BadAnswers'] = question.BadAnswers - actual_BadAnswers
                else:
                    self.context['GoodAnswers'] = question.GoodAnswers - actual_GoodAnswers
                    self.context['BadAnswers'] = question.BadAnswers - actual_BadAnswers - 1
                self.context['init'] = 'mmm'
                return data
            if len(answers) == 0:
                #Means there is not answer objects for the given question
                if data['kind_answer'] is False:
                    self.context['GoodAnswers'] = question.GoodAnswers
                    self.context['BadAnswers'] = question.BadAnswers - 1
                else:
                    self.context['GoodAnswers'] = question.GoodAnswers - 1
                    self.context['BadAnswers'] = question.BadAnswers
                self.context['init'] = "this is the first answer "
                return data
        except models.Question.DoesNotExist:
            raise serializers.ValidationError('no entró en ninguno')

    def create(self, validated_data):
        answer_message = "{init} left {GA} good answers and {BA} bad answers".format(
            init=self.context['init'],
            GA=self.context['GoodAnswers'],
            BA=self.context['BadAnswers'],
        )
        answer = models.Answer.objects.create(**validated_data)
        answer.save()
        #Intance answer object and save it
        self.context['answer'] = answer
        self.context['message'] = answer_message
        #set up the output
        return self.context['answer'], self.context['message']
        #####IF U DON'T WRITE FCKN REEEETUUUURNNNNN THE OBJECT DON'T WILL BE SAVED


class ShowAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Answer
        fields = '__all__'
