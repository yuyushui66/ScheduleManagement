from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
import src.mysqlconn as mysqlconn


class ScheduleView(APIView):
    schedule = []

    # 日程信息，每个元素为[{'title':},{'id':},{'start':},{'end':},{'allday':}]，value均为string
    # 如果allday='true',则end='null'
    # [{'title': 'All Day Event'}, {'id': '_fc1'}, {'start': 'Mon May 01 2023 00:00:00 GMT+0800 (中国标准时间)'}, {'end': 'null'}, {'allday': 'true'}]
    def get(self, request, *args, **kwargs):
        n = request.query_params.dict()
        for i in range(int(len(n) / 5)):
            if [{'title': n['data[' + str(i) + '][0][]']}, {'id': n['data[' + str(i) + '][1][]']},
                {'start': n['data[' + str(i) + '][2][0]']}, {'end': n['data[' + str(i) + '][3][0]']},
                {'allday': n['data[' + str(i) + '][4][]']}] not in self.schedule:  # 判断重复
                self.schedule.append([{'title': n['data[' + str(i) + '][0][]']}, {'id': n['data[' + str(i) + '][1][]']},
                                      {'start': n['data[' + str(i) + '][2][0]']},
                                      {'end': n['data[' + str(i) + '][3][0]']},
                                      {'allday': n['data[' + str(i) + '][4][]']}])
        for i in range(len(self.schedule)):
            print(self.schedule[i])

        print(self.schedule[3][0]['title'])

        # write to database.
        # sql=INSERT INTO books (name) VALUES ('MySQL Manual') ON duplicate KEY UPDATE id = id
        db, cursor = mysqlconn.mysqlConnectDefault()
        for s in self.schedule:
            name = s[0]['title']
            id = s[1]['id'][2:]
            start = s[2]['start'].split()
            start = start[3] + '-' + start[1] + '-' + start[2] + ' ' + start[4]
            end = s[3]['end'].split()
            end = end[3] + '-' + end[1] + '-' + end[2] + ' ' + end[4]
            print(name,id,start,end,sep=' ')
            #sql = "insert into tasks values (" + id + "," + name + ",'', 0, 0, null," + start + "," + end + ",100,0,null" + ") on duplicate key update taskID = " + id
            # try:
            #     cursor.execute(sql)
            #     db.commit()
            # except pymysql.Error as e:
            #     print(e)
            #     db.rollback()
        return Response({"status": True, 'message': '发送成功'})
