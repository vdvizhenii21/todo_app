from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Task, TaskImage

User = get_user_model()


class TaskImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskImage
        fields = ('image',)

class TaskSerializer(serializers.ModelSerializer):
    images = TaskImageSerializer(source='taskimage_set', many=True, read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'title', 'text', 'status','author', 'pub_date', 'edit_date', 'worker', 'images')
    
    def create(self, validated_data):
        images_data = self.context.get('view').request.FILES
        workers = validated_data.pop('worker')
        task = Task.objects.create(**validated_data)
        for image_data in images_data.values():
            TaskImage.objects.create(task=task, image=image_data)
        for worker in workers:
            worker_obj = User.objects.get(id=worker.id)
            task.worker.add(worker_obj)
        return task
