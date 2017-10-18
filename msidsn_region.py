with open("audiencefull.csv") as f:
    for line in f:
        listt = str(line).split(",")
        msidsn_region = str(listt[2])+","+str(listt[23])
        #print msidsn_region
        with open("./output/region.csv", "a") as output:
            output.write(msidsn_region+"\n")