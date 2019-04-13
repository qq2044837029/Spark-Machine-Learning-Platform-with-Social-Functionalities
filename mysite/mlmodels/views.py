from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render

from .forms import UploadMatForm
# Create your views here.
from django.views.decorators.http import require_POST

from common.decorators import ajax_required


@require_POST
@login_required
@ajax_required
def chat(request):
    from .model_chatbot import reply
    user_input = request.POST.get('input')
    if user_input:
        try:
            response=reply(user_input);
            return JsonResponse({'status': 'ok','response':response})
        except Exception:
            JsonResponse({'status': 'error','response':'sorry, something wrong on server, pls try later.'})
    return JsonResponse({'status': 'error'})



@login_required
def chatbot_page(request):
    return render(request,'mlmodels/chatbot/chatbot.html')



# responsible for prediction
@ajax_required
def shape_predict(request):
    from mlmodels.shape_predict.shape_predict_model import predict
    if request.method=='POST':
        result=predict()
        return JsonResponse({'status': 'ok','response':result})
    else:
        return JsonResponse({'status': 'error','response':"request method is not post"})

# responsible for storing file
def shape_predict_page(request):
    from mlmodels.shape_predict.shape_predict_model import store_file
    if request.method=='POST':
        form=UploadMatForm(request.POST,request.FILES)
        if form.is_valid():
            store_file(request.FILES['file'])
            messages.success(request, 'upload successfully')
            from django.http.response import HttpResponseRedirect
            from django.urls import reverse
            return HttpResponseRedirect(reverse('mlmodels:shape_predict_page'))
    else:
        form=UploadMatForm()
        return render(request,'mlmodels/shape_predict/shape_predict.html',{'form':form})