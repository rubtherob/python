procent=int(input('Введите число от 1 до 100: '))
if(procent<0 or procent>100):
    print("Попробуйте снова")
elif (procent%10==1 and procent!=11):
    print(procent,"процент")
elif(procent%10>=2 and procent%10<5 and (procent < 11 or procent >20)):
    print(procent, "процента")
else:
    print(procent, "процентов")
