with open("audiencefull.csv") as f:
    for line in f:
        listt = str(line).split(",")
        msidsn_softwareversion = str(listt[2])+","+str(listt[30])
        #print msidsn_softwareversion
        with open("output/softwareversion.csv", "a")as output:
            output.write(msidsn_softwareversion+"\n")