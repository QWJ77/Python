# coding=gbk
'''
time模块
'''
import time
'''
获取当前时间戳
'''
# result=time.time()
# years=result/(24*60*60*365)+1970
# print(years)
# print(result)
'''
获取时间元组
'''
# result=time.localtime()
# print(result)
# time.struct_time(tm_year=2019, tm_mon=8, tm_mday=31, tm_hour=21, tm_min=15, tm_sec=13, tm_wday=5, tm_yday=243, tm_isdst=0)
'''
获取格式化时间
time.ctime([seconds])
'''
t=time.time()
result=time.ctime(t)
print(result)

# 时间元组->可读时间
timetuple=time.localtime()
result=time.asctime(timetuple)
print(result)

'''
格式化日期字符串
time.strftime(格式字符串,时间元组)
time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())

'''

