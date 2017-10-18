with open("audiencefull.csv") as f:
    for line in f:
        listt = str(line).split(",")
        msidsn_state = str(listt[2])+","+str(listt[22])
        #print msidsn_state
        with open("output/state.csv", "a") as output:
            output.write(msidsn_state+"\n")