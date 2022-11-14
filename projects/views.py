import re
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from rest_framework.status import HTTP_400_BAD_REQUEST
from .serializers import ProjectSerializer


def text_preprocessor(text):
    separated_text = re.split("[.!?]", text)
    no_gap_text = []
    for text in separated_text:
        if text.isspace():
            continue
        no_gap_text.append(text.strip())
    return no_gap_text


class Projects(APIView):
    """
    프로젝트 생성
    POST api/v1/projects/
    """

    def post(self, request):
        text = request.data.get("text")
        if not text:
            raise ParseError("text는 필수입니다.")
        new_text = text_preprocessor(text)
        print(new_text)
        serializer = ProjectSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response({"ok": True})
