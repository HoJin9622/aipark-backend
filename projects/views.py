from gtts import gTTS
from django.core.paginator import Paginator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ParseError, NotFound
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT
from .serializers import ProjectSerializer, AudioSerializer, AudioDetailSerializer
from .models import Audio, Project


class Projects(APIView):
    def post(self, request):
        """
        프로젝트 생성
        POST api/v1/projects/
        """
        text = request.data.get("text")
        audio_index = request.data.get("audio_index")

        if not text:
            raise ParseError("text는 필수입니다.")
        if not audio_index:
            raise ParseError("audio_index는 필수입니다.")

        serializer = ProjectSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

        project = serializer.save()
        audio = Audio.objects.create(
            index=audio_index,
            text=text,
            path="files/test1.mp3",
            project=project,
        )
        tts = gTTS(" ".join(audio.processed_text))
        tts.save("files/test1.mp3")
        return Response({"ok": True})


class ProjectAudio(APIView):
    PAGE_SIZE = 10

    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        """
        텍스트 조회
        GET api/v1/projects/{id}/audios/
        """

        try:
            page = request.query_params.get("page", 1)
            page = int(page)
        except ValueError:
            page = 1

        project = self.get_object(pk)
        audios = project.audios.all()
        paginator = Paginator(audios, self.PAGE_SIZE, orphans=2)
        serializer = AudioSerializer(paginator.get_page(page), many=True)
        return Response(serializer.data)


class AudioDetail(APIView):
    def get_object(self, pk):
        try:
            return Audio.objects.get(pk=pk)
        except Audio.DoesNotExist:
            raise NotFound

    def patch(self, request, pk):
        """
        텍스트 수정
        PATCH api/v1/audios/{id}/
        """
        audio = self.get_object(pk)
        serializer = AudioDetailSerializer(
            audio,
            data=request.data,
            partial=True,
        )
        if not serializer.is_valid():
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response({"ok": True})

    def delete(self, request, pk):
        """
        텍스트 삭제
        DELETE api/v1/audios/{id}/
        """
        audio = self.get_object(pk)
        audio.delete()
        return Response({"ok": True}, status=HTTP_204_NO_CONTENT)
