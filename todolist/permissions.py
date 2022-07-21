from rest_framework.permissions import IsAuthenticated


class IsAuthor(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user

class IsWorker(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return request.user in obj.worker.all()

class IsWorkerStatus(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return request.data['status'] == "INPROGRESS"

