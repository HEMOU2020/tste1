import xlwt
import xlrd
from xlutils.copy import copy
import datetime
import time
def work(path,list1):
    workbook=xlrd.open_workbook(path,formatting_info=True)
    sheet_name=workbook.sheet_names()
    sheet=workbook.sheet_by_index(0)
    row1=sheet.nrows
    #col1=sheet.ncols
    #row1_date=sheet.row_values(0) #读取第一行数据
    #row2_date=sheet.row_values(1) #读取第二行数据
    #cell_value=sheet.cell_value(1,1) #读取特定单元格数据
    #print(cell_value)
    sheet.put_cell(row1,0,1,list1[0],3)
    sheet.put_cell(row1,1,1,list1[1],1)
    sheet.put_cell(row1,2,1,list1[2],1)
    sheet.put_cell(row1,3,1,list1[3],1)
    #cell_value2 = sheet.cell(1,1)
    #print(cell_value2)
    wb=copy(workbook)
    wb.save('test1.xls')
date1=input('请输入日期：')
starttime=input('请输入上班时间：')
endtime=input('请输入下班时间：')
#endtime1=starttime+datetime.timedelta(hours=8)
overtime=input('请输入加班时长：')
list1=[date1,starttime,endtime,overtime]
work('F:/python/python study/个人考勤记录.xls',list1)