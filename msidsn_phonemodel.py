with open("audiencefull.csv") as f:
    for line in f:
        #print(line) 
        listt = str(line).split(",")
        #print (listt)
        msidsn_phonemodel = str(listt[2])+","+str(listt[27])
        #print msidsn_phonemodel
        with open("./output/phonemodel.csv", "a") as output:
            output.write(msidsn_phonemodel+"\n")