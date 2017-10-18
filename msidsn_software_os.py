with open("audiencefull.csv") as f:
    for line in f:
        listt = str(line).split(",")
        msidsn_software_os = str(listt[2])+","+str(listt[29])
        #print msidsn_software_os
        with open("./output/softwareos.csv", "a") as output:
            output.write(msidsn_software_os+"\n")