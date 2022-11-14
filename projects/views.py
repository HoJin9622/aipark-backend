import re
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ParseError


def text_preprocessor(text):
    separated_text = re.split("[.!?]", text)
    no_gap_text = []
    for text in separated_text:
        if text.isspace():
            continue
        no_gap_text.append(text.strip())
    return no_gap_text


class Projects(APIView):
    def post(self, request):
        text = request.data.get("text")
        if not text:
            raise ParseError("text는 필수입니다.")
        new_text = text_preprocessor(text)
        print(new_text)
        return Response()
