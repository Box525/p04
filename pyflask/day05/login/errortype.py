import sys,traceback


try:
    list_data = [0,1,2,3,4,5]
    list_data[7] = 1
except Exception as e:
    print('error:',traceback.format_exc())
    print(sys.exc_info()[0])
    print(sys.exc_info()[1])
    print(e)