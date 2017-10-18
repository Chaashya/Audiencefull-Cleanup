with open("audiencefull.csv") as f:
    for line in f:
        #print(line) 
        listt = str(line).split(",")
        #print (listt)
        msidsn_localgovt = str(listt[2])+","+(listt[21])
        #print msidsn_localgovt
        with open("./output/localgovt.csv", "a") as output:
            output.write(msidsn_localgovt+"\n")