#from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
import openai, os
from dotenv import load_dotenv
load_dotenv()

api_key=os.getenv("OPENAI_KEY",None)

def chatbot(request):
    chatbot_response = None
    if api_key is not None and  request.method == 'POST':
        openai.api_key = api_key
        user_input= request.POST.get('user_input')
        #prompt = f"if the question is related to weather - answer it: {user_input},else say: can't answer this"
        prompt = user_input
        question = user_input

        response = openai.Completion.create(
            engine = "text-davinci-002",
            prompt= prompt,
            max_tokens=100,
            temperature=1
        )
        print(response)
    

        chatbot_response = response["choices"][0]["text"]
    return render(request,"main.html",{"response":chatbot_response,})
    
    