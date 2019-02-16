#cal.py
heigh, weight=eval(input("please put into the value of heigh and weight[use comma to separate]:"))
BMI=weight/pow(heigh,2)
print("The BMI is :{:.2f}".format(BMI))
who,nat="",""
if BMI<18.5:
    who,nat="thinish","thinish"
elif 18.5<=BMI<24:
    who,nat="normal","normal"
elif 24<=BMI<25:
    who,nat="normal","chubby"
elif 25<=BMI<28:
    who,nat="chubby","chubby"
elif 28<=BMI<30:
    who,nat="chubby","fat"
else:
    who,nat="fat","fat"
print("THE BIM stands that:(who)'{0}',(nat)'{1}'".format(who,nat))
        
