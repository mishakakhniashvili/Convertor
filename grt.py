a=input("ricxvi dawere: ").replace(" ","")
erteuli={"ერთი":1,"ორი":2,"სამი":3,"ოთხი":4,"ხუთი":5,"ექვსი":6,"შვიდი":7,"რვა":8,"ცხრა":9}
ateuli={"ათი":10,"თერთმეტი":11,"თორმეტი":12,"ცამეტი":13,"თოთხმეტი":14,"თხუთმეტი":15,"თექვსმეტი":16,"ჩვიდმეტი":17,"თვრამეტი":18,"ცხრამეტი":19,"ოცი":20}
oceuli={"ორმოცი":40,"სამოცი":60,"ოთხმოცი":80,"ორმოც":40,"სამოც":60,"ოთხმოც":80,"ოც":20}
asi={"ასი":100,"ას":100}
atasi={"ათასი":1000,"ათას":1000}
gansak ={"მილიარდი":1000000000,"მილიარდ":1000000000,"მილიონი":1000000,"მილიონ":1000000, "ათასი":1000,"ათას":1000}
yvela={}
yvela.update(erteuli)
yvela.update(ateuli)
yvela.update(oceuli)
yvela.update(asi)
yvela.update(gansak)
def fudze(a):
    b=0
    if a in yvela:
        return yvela[a]
    if "და" in a:
        a=a.split("და")
        b+=yvela[a[1]]
        a=a[0]
    for i in erteuli:
        if i in a[3:]:
            b+=erteuli[i]
            a=a.replace(i,"")
    for i in oceuli:
        if i in a:
            b+=oceuli[i]
            a=a.replace(i,"")
    for i in asi:
        if i in a:
            b+=asi[i]
            a=a.replace(i,"")
    if a in ("ცხრა","რვა"):
        b+=yvela[a]*100-100
    else:
        b+=yvela[a+"ი"]*100-100
    return b

def didi_ricxvi(a):
    if a in yvela:
        return yvela[a]
    b=0
    for i in gansak:
        a=a.split(i)
        if len(a)>1:
            if a[0]=="":
                b+= gansak[i]
            else:
                b+=fudze(a[0])*gansak[i]
            a=a[1]
        else:
            a=a[0]
    b+=fudze(a)
    return b
print(didi_ricxvi(a))
