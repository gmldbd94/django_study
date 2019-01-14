#render를 통하여 사이트 페이지 띄게 하는 라이브러리
from django.shortcuts import render

#loader를 통하여 사이트 템플릿을 띄게 하는 라이브러리
from django.template import loader
#HttpResponse를 이용하는 라이브러리
from django.http import HttpResponse

#404 페이지 뜨게하는 라이브러리
from django.http import Http404

#404 페이즈 띄게해주는 라이브러리
from django.shortcuts import get_object_or_404

#뒤돌아 가기 기능을 제공하는 라이브러리
from django.http import HttpResponseRedirect

from django.urls import reverse

# 현 app의 model를 불러온다
from .models import Question, Choice

# Create your views here.

#from django.http import HttpResponse를 통하여 템플릿을 불러오는 방법
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = ', '.join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)

#from django.shortcuts import render를 이용하여 템플릿 불러오는 방법
# def index(request):
#     lastest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {'latest_question_list': lastest_question_list,}
#     # output = ', '.join([q.question_text for q in latest_question_list])
#     return HttpResponse(template.render(context,request))
#
# # django.http를 이용하여 404페이지 호출하는 방법
# # def detail(request, question_id):
# #     try:
# #         question = Question.objects.get(pk=question_id)
# #     except Question.DoesNotExist:
# #         raise Http404("Question does not exist")
# #     return render(request, 'polls/detail.html', {'question': question})
#
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
#
def vote(request, question_id):
    # get_object_or_404(Model, id값) => 모델에 있는 값을 가져오거나 404표시
    question = get_object_or_404(Question, pk=question_id)
    try:
        #selected_choice는 'choice_set'(외래키로 연결된 데이터베이스(model참조))에서 선택된 것들을 가져온다
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        # reverse는 HttpResponseRedirect 생성자에서 함수로 사용하고 있다.
        #'/polls/:question.id/results/' == reverse('results', args=(qusestion.id))
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})
#


#효율적인 코드 작성법
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


# def vote(request, question_id):
#     ... # same as above, no changes needed.
