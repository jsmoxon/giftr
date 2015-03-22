from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from feedback.models import Question, Choice

#def index(request): 
 #   return render(request, 'feedbacked.html')

# first hack at feedbacked view, before understanding it:
#def index(request):
 #   latest_question_list = Question.objects.order_by('-pub_date')[:5]
  #  template = loader.get_template('feedbacked.html')
   # context = RequestContext(request, {
    #    'latest_question_list': latest_question_list,
    #})
    #return HttpResponse(template.render(context))


#Jack what's the difference between render and HttpResponse? WHy don't we need  loader, RequestContext and HttpResponse ?
# The render() function takes the request object as its first argument, 
# a template name as its second argument and a dictionary as its optional third argument. 
# It returns an HttpResponse object of the given template rendered with the given context.    

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'feedback/index.html', context)

#def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    template = loader.get_template('feedback/index.html')
#    context = RequestContext(request, {
#    	'latest_question_list': latest_question_list,
#    	})
#    return HttpResponse(template.render(context))


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'feedback/detail.html', {'question': question})

#def detail(request, question_id):
#    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'feedback/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('feedback:results', args=(p.id,)))    

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'feedback/results.html', {'question': question})        
