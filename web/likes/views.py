import json
from django.http import HttpResponse
from django.views import View
from rest_framework.views import APIView
from django.contrib.contenttypes.models import ContentType
from .models import LikeDislike
from rest_framework.response import Response
from rest_framework import authentication, permissions


class VotesView(APIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    model = None  # Модель данных - Статьи или Комментарии
    vote_type = None  # Тип комментария Like/Dislike

    def post(self, request, section, slug):
        obj = self.model.objects.get(slug=slug)
        # GenericForeignKey не поддерживает метод get_or_create
        try:
            likedislike = LikeDislike.objects.get(content_type=ContentType.objects.get_for_model(obj), object_id=obj.id,
                                                  user=request.user)
            if likedislike.vote is not self.vote_type:
                likedislike.vote = self.vote_type
                likedislike.save(update_fields=['vote'])
                result = True
            else:
                likedislike.delete()
                result = False

        except LikeDislike.DoesNotExist:
            obj.votes.create(user=request.user, vote=self.vote_type)
            result = True

        data = {
            "is_liked": True if request.user in obj.votes.is_liked() else False,
            "is_disliked": True if request.user in obj.votes.is_disliked() else False,
            "result": result,
            "like_count": obj.votes.likes().count(),
            "dislike_count": obj.votes.dislikes().count(),
            "sum_rating": obj.votes.sum_rating()
        }
        # return HttpResponse(json.dumps(data), content_type="application/json")
        return Response(data, content_type="application/json")
