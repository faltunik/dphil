from rest_framework import viewsets, status
from rest_framework.response import Response


from .serializer import CourseSerializer

# Create your views here.




# API to create course
# API to list all course
# API to retrieve a course
class CourseAPI(viewsets.ModelViewSet):
    def create(self, request):
        if request.user.teacher:
            serializer = CourseSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(teacher= request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "You Dont Have Permission"}, status=status.HTTP_400_BAD_REQUEST)



# API to update a course (Enroll on Course)





# API to get students list  of course(same as ppl who like the post)




