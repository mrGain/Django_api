# from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework import status, viewsets
from rest_framework.decorators import action

from .serilizer import TodoSerilizer
from .models import Todo
# Create your views here.
@api_view(['GET','POST','PATCH'])
def home(request):
    if request.method == 'GET':
        return Response({
            'status':200,
            'message':'Yes  Django Rest Freamwork is working ',
            'method_called':'GET'
        })
    if request.method == 'POST':
        return Response({
            'status':200,
            'message':'Yes  Django Rest Freamwork is working ',
            'method_called':'POST'
        })
    if request.method == 'PATCH':
        return Response({
            'status':200,
            'message':'Yes  Django Rest Freamwork is working ',
            'method_called':'PATCH'
        })

@api_view(['GET'])
def get_todo(request):
    todo_objs = Todo.objects.all()
    serilizer = TodoSerilizer(todo_objs, many=True)
    return Response({
        'status':True,
        'message':'Todo fached',
        'data':serilizer.data
    })

@api_view(['POST'])
def post_todo(request):
    try:
        data = request.data
        # print(data)
        serilizer = TodoSerilizer(data = data)

        if serilizer.is_valid():
            # print(serilizer.data)
            serilizer.save()
            return Response({
                'status':'True',
                'message':'success data',
                'data':serilizer.data
            }) 
        else:
            return Response({
                'status':'False',
                'message':'invalid data',
                'data':serilizer.errors
            })    

    except Exception as e:
        print(e)
        return Response({
            'status':'False',
            'message':'Something went wrong ',
        })


@api_view(['PATCH'])
def patch_todo(request):
    try:
        data = request.data 
        if not data.get('uid'):
            return Response({
                'status':False,
                'mesage':'uid is required',
                'data':{}
            })
        obj = Todo.objects.get(uid = data.get('uid'))
        serilizer = TodoSerilizer(obj, data = data, partial=True)
        if serilizer.is_valid():
            serilizer.save()
            return Response({
                'status':True,
                'message':'success data',
                'data':serilizer.data
            })

        return Response({
            'status':'False',
            'message':'invalid data',
            'data':serilizer.errors
        })     

    except Exception as e:
        print(e) 
        return Response({
            'status':'False',
            'message':'invalid uid',
            'data':serilizer.errors
        }) 


# Class besed view.
class TodoView(APIView):
    def get(self, request):
        todo_objs = Todo.objects.all()
        serilizer = TodoSerilizer(todo_objs, many=True)
        return Response({
            'status':True,
            'message':'Todo fached',
            'data':serilizer.data
        })     
    def post(self, request):
        try:
            data = request.data
            # print(data)
            serilizer = TodoSerilizer(data = data)

            if serilizer.is_valid():
                # print(serilizer.data)
                serilizer.save()
                return Response({
                    'status':'True',
                    'message':'success data',
                    'data':serilizer.data
                }) 
            else:
                return Response({
                    'status':'False',
                    'message':'invalid data',
                    'data':serilizer.errors
                })    

        except Exception as e:
            print(e)
            return Response({
                'status':'False',
                'message':'Something went wrong ',
            })     
    def patch(self, request):
        try:
            data = request.data 
            if not data.get('uid'):
                return Response({
                    'status':False,
                    'mesage':'uid is required',
                    'data':{}
                })
            obj = Todo.objects.get(uid = data.get('uid'))
            serilizer = TodoSerilizer(obj, data = data, partial=True)
            if serilizer.is_valid():
                serilizer.save()
                return Response({
                    'status':True,
                    'message':'success data',
                    'data':serilizer.data
                })

            return Response({
                'status':'False',
                'message':'invalid data',
                'data':serilizer.errors
            })     

        except Exception as e:
            print(e) 
            return Response({
                'status':'False',
                'message':'invalid uid',
                'data':serilizer.errors
            })        

        
# Class viewset
class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerilizer

    @action(detail=False, methods=['post'])
    def add_date_to_todo(self):
        try:

        except:    
            