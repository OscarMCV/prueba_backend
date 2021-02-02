Prueba Backend
Backend developer position challenge
We require to develop an API for e-learning courses to integrate in our system. The purpose of this tool is for us, as professors to manage courses configuration and performance reviews and, for our students, to take courses when using our frontend. Our PM is a very busy person, so we don’t have detailed tasks but only the business rules to work with. Here they are:
    1. We have courses that contain lessons and lessons that contain questions
    2. The courses are correlative with previous ones
    3. The lessons are correlative with previous ones
    4. The questions for each lesson have no correlation
    5. All questions for a lesson are mandatory
    6. Each question has a score
    7. Each lesson has an approval score that has to be met by the sum of correctly answered questions to approve it
    8. A course is approved when all lessons are passed.
    9. There’s no restriction on accessing approved courses
    10. Only professors can create and manage courses, lessons and questions
    11. Any student can take a course
    12. Initially, we’ll need to support these types of questions:
        ◦ Boolean
        ◦ Multiple choice where only one answer is correct
        ◦ Multiple choice where more than one answer is correct
        ◦ Multiple choice where more than one answer is correct and all of them must be answered correctly
    13. Frontend guys specifically asked for these endpoints for the students to use:
        ◦ Get a list of all courses, telling which ones the student can access
        ◦ Get lessons for a course, telling which ones the student can access
        ◦ Get lesson details for answering its questions
        ◦ Take a lesson (to avoid several requests, they asked to send all answers in one go)
        ◦ Basic CRUD for courses, lessons and questions
Codebase rules:
    1. The API must be developed using Python
    2. There must be a readme file documenting installation and usage.
    3. You can use any frameworks and libraries you want, but they must be included in the readme file documenting its purpose and a brief explanation with the reasoning for your choice.
