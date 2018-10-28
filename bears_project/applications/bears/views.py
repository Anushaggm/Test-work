import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView

from applications.bears.models import Bear


class ListBearsView(ListView):
    """
    list all bears
    """
    model = Bear
    template_name = 'bears/list_bears.html'
    context_object_name = 'bears'

    def get_queryset(self, **kwargs):
        bears = super(ListBearsView, self).get_queryset(**kwargs)
        bears = bears.order_by('bear_type')
        return bears


class AddBearsView(CreateView):
    """
     Create new Bear
    """

    template_name = 'bears/add_bear.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request):
        ctx = {}
        name = request.POST.get('name')
        bear_type = request.POST.get('bear_type')

        if Bear.objects.filter(name=name, bear_type=bear_type).exists():
            #Prevent from creating duplicate entries
            ctx['status'] = False
            ctx['exist'] = True
        else:
            if name and bear_type:
                bear = Bear()
                bear.name = name
                bear.bear_type = bear_type
                bear.save()
                ctx['status'] = True
            else:
                ctx['status'] = False
        if ctx['status'] == True:
            #set cookie if an entry has been created
                response = HttpResponse(json.dumps(ctx), content_type="application/json")
                response.set_cookie('i_love_cookies', 'I love cookies')
                return response
        return HttpResponse(json.dumps(ctx), content_type="application/json")



