from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

test = []
class HelloView(APIView):
    def get(self, request, *args, **kwargs):
        # title=request.query_params.dict()['title'].replace('\n','')
        # start=request.query_params.dict()['start'].replace('\n','')
        # end=request.query_params.dict()['end'].replace('\n','')
        # allday=request.query_params.dict()['allday'].replace('\n','')
        n=request.query_params

        if n['title'] not in test :
            test.append(n['title'])

        print(test)
        # print(title,'\n',start,'\n',end,'\n',allday)
        return Response({"status": True, 'message': '发送成功'})

