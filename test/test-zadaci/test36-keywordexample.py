# ##and ....  logical operators
#
# def myFunction(a,b) :
#     if a<b:
#         return True
#     else:
#         False
#
# print(myFunction(10,20))
#
#
#
# ## with -as je  file handling
#
# # 1) without using with statement
# file = open('file_path', 'w')
# file.write('hello world !')
# file.close()
#
# # 2) without using with statement
# file = open('file_path', 'w')
# try:
#     file.write('hello world')
# finally:
#     file.close()
#
# # 3) using with statement
# with open('file_path', 'w') as file:
#     file.write('hello world !')
# 4) USING AS
# import calendar as c
# print(c.month_name[10])


#assert
# ensure that something is tru or something False that have a error message
#assert False, "Error"
