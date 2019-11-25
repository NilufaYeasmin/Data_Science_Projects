s_time=0
p_time=0
spd=0
kf=0

result=dict()

for i in range(1,3):
    fname=str(i)+".out"
    #print(fname)

    with open(fname,"r") as f:
        f.readline()

        for line in f:
            l=line.split()

            key=l[0]

            if key not in result:
                #s_time = float(l[1])
                #p_time = float(l[2])
                #spd = float(l[3])
                #kf = float(l[4])

                result[key]=[float(l[i]) for i in range(1,5)]
                #print("first:"+key+str(result[key]))
            else:
                r=result[key]
                #print("Before: "+key+"\t"+str(r))
                s_time = float(r[0]) + float(l[1])
                p_time = float(r[1]) + float(l[2])
                spd = float(r[2]) + float(l[3])
                kf = float(r[3]) + float(l[4])
                result[key] = [s_time,p_time,spd,kf]
                #print("After: "+key+"\t"+str(result[key]))

with open('avg.out', 'w') as f:
    run2=2
    f.write("Points\tSeq Time\tPar Time\tSpeed Up\tKrap-Flatt\n")

    for k in result:
        v=result[k]

        st=round((v[0]/run2),2)
        pt=round((v[1]/run2),2)
        su = round((v[2] / run2), 2)
        kft = round((v[3] / run2), 2)

        val=str(st).rjust(8)+"\t"+str(pt).rjust(8)+"\t"+str(round(su,3)).rjust(6)+"\t\t"+str(round(kft,2))



        f.write(k.rjust(7)+"\t"+val+"\n")