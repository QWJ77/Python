# coding=gbk
'''
timeģ��
'''
import time
'''
��ȡ��ǰʱ���
'''
# result=time.time()
# years=result/(24*60*60*365)+1970
# print(years)
# print(result)
'''
��ȡʱ��Ԫ��
'''
# result=time.localtime()
# print(result)
# time.struct_time(tm_year=2019, tm_mon=8, tm_mday=31, tm_hour=21, tm_min=15, tm_sec=13, tm_wday=5, tm_yday=243, tm_isdst=0)
'''
��ȡ��ʽ��ʱ��
time.ctime([seconds])
'''
t=time.time()
result=time.ctime(t)
print(result)

# ʱ��Ԫ��->�ɶ�ʱ��
timetuple=time.localtime()
result=time.asctime(timetuple)
print(result)

'''
��ʽ�������ַ���
time.strftime(��ʽ�ַ���,ʱ��Ԫ��)
time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())

'''

