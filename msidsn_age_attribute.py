def attributee(x):
    if(len(x) > 0):
        try: 
            x = int(x)
            if x==17 or x<17:
                return "Teenage";
            elif x>=18 and x<=24:
                return "Young"
            elif x>=25 and x<=34:
                return "Young adult"
            elif x>=35 and x<=59:
                return "Adult"
            else:
                return "Elder"
        except ValueError:
            return ""
    else:
        return ""


with open("audiencefull.csv") as f:
    msidsn_age_attribute = ""
    for line in f:
        listt = str(line).split(",")
        _age = str((listt[17]))
        #print(_age)
        _attribute = attributee(_age)
        msidsn_age_attribute = msidsn_age_attribute + str(listt[2]) + "," + str(_age) + "," + str(_attribute) + "\n"

        print(msidsn_age_attribute)

        with open("./output/age_attribute.csv","a") as output:
            output.write(msidsn_age_attribute+"\n")
