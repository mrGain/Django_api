
from rest_framework import serializers
import re
from .models import TimingTodo, Todo
from django.template.defaultfilters import slugify

class TodoSerilizer(serializers.ModelSerializer):
     
    slug = serializers.SerializerMethodField()

    class Meta:
        model = Todo
        # fields = '__all__' # This field is used when all fields are serilized.
        fields = ['uid','slug','todo_title','todo_description','is_done']
        # exclude = ['created_date','updated_at']  # This field is used when we want to exclude some field

    def get_slug(self, obj):
        return slugify(obj.todo_title)    

    # Validating a specific key
    def validate_todo_title(self, data):

       
        if data:
            todo_title = data
            regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
            
            if len(todo_title) < 3:
                raise serializers.ValidationError('Todo tiele must be more than 3 chars..')

            if not regex.search(todo_title) == None:
                raise serializers.ValidationError('Todo tiele cannot contains special character..')
        
        return  data    

    # # Validating any key from the data set.
    # def validate(self, validated_data):
    #     if validated_data.get('todo_title'):
    #         todo_title = validated_data['todo_title']
    #         regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
            
    #         if len(todo_title) < 3:
    #             raise serializers.ValidationError('Todo tiele must be more than 3 chars..')

    #         if not regex.search(todo_title) == None:
    #             raise serializers.ValidationError('Todo tiele cannot contains special character..')

                

    #     return validated_data        

class TimingTodoSerilizer(serializers.ModelSerializer):
    class Meta:
        model = TimingTodo
        exclude = ['created_at','updated_at']
        