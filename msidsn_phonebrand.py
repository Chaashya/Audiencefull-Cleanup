with open("audiencefull.csv") as f:
    for line in f:
        #print(line) 
        listt = str(line).split(",")
        #print (listt)
        msidsn_phonebrand = str(listt[2])+","+str(listt[26])
        #print msidsn_phonebrand
        with open("./output/phonebrand.csv", "a") as output:
            output.write(msidsn_phonebrand+"\n")