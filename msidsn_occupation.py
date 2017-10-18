with open("audiencefull.csv") as f:
    for line in f:
        listt = str(line).split(",")
        msidsn_occupation = str(listt[2])+","+ str(listt[20])
        #print msidsn_occupation
        with open("./output/occupation.csv", "a") as output:
            output.write(msidsn_occupation+"\n")