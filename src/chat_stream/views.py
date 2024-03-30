from django.http import StreamingHttpResponse
from rest_framework.views import APIView


class ChatStreamView(APIView):
    def get(self, request):
        return StreamingHttpResponse("Hello, world!", content_type="text/plain")



