with open("audiencefull.csv") as f:
    for line in f:
        #print(line) 
        listt = str(line).split(",")
        #print (listt)
        msidsn_imei = str(listt[2])+","+ str(listt[24])
        #print msidsn_imei 
        with open("./output/imei.csv", "a") as output:
            output.write(msidsn_imei+"\n")