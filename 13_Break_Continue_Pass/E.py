# que 35
# for i in range(1,6):
#     if i==2:
#         continue
#     if i==4:
#         break
#     print(i)
# else:
#     print("Finished")
#else does not run because the loop is forced to break

#que 36
# listt = [7,67,-9,5,53,2,-8]
# for x in listt:
#     if x<0:
#         continue
#     if x==5:
#         break
#     print(x)
# else:
#     print("Target not found")

#que 37
# listt = [7,0,8,17,-1]
# for x in listt:
#     if x==0:
#         continue
#     if x==-1:
#         break
#     print(x)
# else:
#     print("All values processed")

#que 38
# for row in range(1,4):
#     for col in range(1,4):
#         if col==2:
#             continue
#         if row==3:
#             break
#         print(row,col)
#     else:
#         print("Inner loop completed")

#pairs printed are 1 1, 1 3, 2 1, 2 3
#inner loop one and two finishes without break
#no, not for the last row because it was force break-ed

#que 39
# nums = [2,5,-8,24,48,88]
# for i in nums:
#     if i<0:
#         continue
#     if i%4==0 and i%6==0 and i%3==0:
#         print("Found", i)
#         break
# else:
#     print("No match found")

#que 40
# 1 break
# 2 continue
# 3 for-else
# 4 pass
# 5 continue
# 6 break
# 7 if-else, break
# 8 pass