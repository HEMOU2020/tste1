import xlwt
import datetime
'''workbook1=xlwt.Workbook(encoding='utf-8')
sheet1=workbook1.add_sheet('测试')
a=['日期','上班时间','下班时间','加班时长']
for i in range(len(a)):
  sheet1.write(0,i,a[i])
workbook1.save('测试.xls')'''
def work(sheetname,path,list1,list2):
  workbook1=xlwt.Workbook(encoding='utf-8')
  sheet1=workbook1.add_sheet(sheetname,cell_overwrite_ok=True)
  style=xlwt.XFStyle()
  style.num_format_str='YYYY/M/D'
  for i in range(len(list1)):
    for j in range(len(list2)):
      sheet1.write(0,i,list1[i])
      sheet1.write(1,j,list2[j],style)
    #style=xlwt.XFStyle
  workbook1.save(path)
a=['日期','上班时间','下班时间','加班时长']
localtime=datetime.date.today()
starttime=input('请输入上班时间：')
endtime=input('请输入下班时间：')
overtime=input('请输入加班时长：')
b=[localtime,starttime,endtime,overtime]
work('个人考勤记录','F:/python/python study/个人考勤记录.xls',a,b)
