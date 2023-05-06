from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

class ScheduleView(APIView):
    schedule = []
    # 日程信息，每个元素为[{'title':},{'id':},{'start':},{'end':},{'allday':}]，value均为string
    # 如果allday='true',则end='null'
    # [{'title': 'All Day Event'}, {'id': '_fc1'}, {'start': 'Mon May 01 2023 00:00:00 GMT+0800 (中国标准时间)'}, {'end': 'null'}, {'allday': 'true'}]
    def get(self, request, *args, **kwargs):
        n=request.query_params.dict()
        for i in range(int(len(n)/5)):
            if [{'title':n['data['+str(i)+'][0][]']},{'id':n['data['+str(i)+'][1][]']},
                                {'start':n['data['+str(i)+'][2][0]']},{'end':n['data['+str(i)+'][3][0]']},
                                {'allday':n['data['+str(i)+'][4][]']}] not in self.schedule:# 判断重复
                self.schedule.append([{'title':n['data['+str(i)+'][0][]']},{'id':n['data['+str(i)+'][1][]']},
                                    {'start':n['data['+str(i)+'][2][0]']},{'end':n['data['+str(i)+'][3][0]']},
                                    {'allday':n['data['+str(i)+'][4][]']}])
        for i in range(len(self.schedule)):
            print(self.schedule[i])

        print(self.schedule[3][0]['title'])

        return Response({"status": True, 'message': '发送成功'})

