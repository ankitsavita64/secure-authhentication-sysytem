from django.shortcuts import render

from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response

from google import genai

@api_view(["POST"])
def chat_ai(request):
    
    print(request.data)

    question = request.data.get("question")
    if not question:
        return Response(
            {
                "error":"Question is required."
            },
            status=400
        )

    client = genai.Client(
        api_key=settings.GEMINI_API_KEY
    )

    prompt = f"""
    
You are SecureAuth AI Assistant.

Only answer questions related to:

- Login
- Signup
- JWT
- Authentication
- Django
- REST API
- Docker
- AWS
- HTTPS
- Nginx

User Question:

{question}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return Response({
        "question": question,
        "answer": response.text
    })