with open("audiencefull.csv") as f:
    for line in f:
        listt = str(line).split(",")
        msidsn_softwarevendor = str(listt[2])+","+str(listt[28])
        #print msidsn_softwarevendor
        with open("./output/softwarevendor.csv","a")as output:
            output.write(msidsn_softwarevendor+"\n")