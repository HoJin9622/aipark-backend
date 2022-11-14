from gtts import gTTS
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from rest_framework.status import HTTP_400_BAD_REQUEST
from .serializers import ProjectSerializer
from .models import Audio


class Projects(APIView):
    """
    프로젝트 생성
    POST api/v1/projects/
    """

    def post(self, request):
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
