with open("audiencefull.csv") as f:
    for line in f:
        #print(line) 
        listt = str(line).split(",")
        #print (listt)
        msidsn_gender = str(listt[2]) + "," + str(listt[16])
        #print msidsn_gender
        with open("./output/gender.csv", "a") as output:
            output.write(msidsn_gender+"\n")

      
        