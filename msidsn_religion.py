with open("audiencefull.csv") as f:
    for line in f:
        listt = str(line).split(",")
        msidsn_religion = str(listt[2])+","+str(listt[18])
        #print msidsn_religion
        with open("./output/religion.csv", "a") as output:
            output.write(msidsn_religion+"\n")