from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
import src.mysqlconn as mysqlconn
import src.Communication as cm
MonShortToNum = {
    'Jan': '01',
    'Feb': '02',
    'Mar': '03',
    'Apr': '04',
    'May': '05',
    'Jun': '06',
    'Jul': '07',
    'Aug': '08',
    'Sep': '09',
    'Oct': '10',
    'Nov': '11',
    'Dec': '12'
}


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
                self.schedule.append([{'title': n['data[' + str(i) + '][0][]']}, {'id': '_fc'+str(len(self.schedule)+1)},
                                      {'start': n['data[' + str(i) + '][2][0]']},
                                      {'end': n['data[' + str(i) + '][3][0]']},
                                      {'allday': n['data[' + str(i) + '][4][]']}])
        for i in range(len(self.schedule)):
            print(self.schedule[i])
        # {'id': n['data[' + str(i) + '][1][]']},
        # write to database.
        # sql=INSERT INTO books (name) VALUES ('MySQL Manual') ON duplicate KEY UPDATE id = id
        db, cursor = mysqlconn.mysqlConnectDefault()
        for s in self.schedule:
            name = s[0]['title']
            id = s[1]['id'][3:]

            start = s[2]['start'].split()
            if len(start) <= 1:
                start = 'null'
            else:
                start[1] = MonShortToNum[start[1]]
                start = start[3] + '-' + start[1] + '-' + start[2] + ' ' + start[4]

            end = s[3]['end'].split()
            if len(end) <= 1:
                end = 'null'
            else:
                end[1] = MonShortToNum[end[1]]
                end = end[3] + '-' + end[1] + '-' + end[2] + ' ' + end[4]
            # print(name, id, start, end, sep=' ')

            # sql = "insert into tasks values (" + id + ",'" + name + "','', 0, 0, null,'" + start + "','" + end + "',100,0,null" + ") on duplicate key update taskID = " + id
            sql = "insert into tasks values ("
            sql += str(id) + "," # id
            sql += "'" + name + "'" + "," # taskName
            sql += "''" + "," # taskDescription
            sql += "0" + "," # taskCategory
            sql += "0" + "," # taskStatus
            sql += "null" + "," # taskCreationTime
            if start == 'null': sql += "null" + "," # taskStartTime
            else: sql += "'" + start + "'" + "," # taskStartTime
            if end == 'null': sql += "null" + "," # taskEndTime
            else: sql += "'" + end + "'" + "," # taskEndTime
            sql += "100" + "," # taskPriority
            sql += "null" + ',' # taskNeedRemind
            sql += "null" + ")" # taskRemindTime
            sql += " on duplicate key update taskID = " + str(id) + ";"

            print(sql)
            c = cm.Communication()
            c.writeToDB(sql,False)
            # try:
            #     cursor.execute(sql)
            #     db.commit()
            # except pymysql.Error as e:
            #     print(e)
            #     db.rollback()
        return Response({"status": True, 'message': '发送成功'})
