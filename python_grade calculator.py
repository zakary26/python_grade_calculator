n = 0
i = 0
lis_not = []
som = 0.0
klasifikasyon = ''

note=0
print("Byen vini; pwogram sa pral pèmèt ou kalkile mwayèn  n_nòt")
n=input("Konbyen nòt wap rantre : ")

while (not n or n.isnumeric()== False): # asirans ke itilizatè a fè yon sezi epi ke se yon nonb li sezi 
        n = input("Tanpri, tape yon nonb : ")
n=int(n)
while(i < n): # kalkil mwayèn lan 
    print("Rantre " + str(i+1) + "e nòt la ")
    note=(input(": "))
    while (not note or note.isnumeric()== False):
            note= input("asire w ke "+ str(i+1) +"e nòt la pa vid e li se yon nonb : " )
            
    note=int(note)
    lis_not.insert(i, note)
   
    som = som + lis_not[i]
    i+= 1

mwayen = som/n
#jesyon klasifikasyon depandan de mwayen lan
if(mwayen >= 90):
        print(": A")
        klasifikasyon = 'A'
elif(mwayen >= 80 and mwayen < 90):
        print(": B")
        klasifikasyon = 'B'
elif(mwayen >= 70 and mwayen < 80):
        print(": C")
        klasifikasyon = 'C'
elif(mwayen >= 60 and mwayen < 70):
        print(": D")
        klasifikasyon = 'D'
elif(mwayen < 60):
        print(": F")
        klasifikasyon = 'F'
        
print("mwayen lan se: " + str(mwayen) + " : " + klasifikasyon )
print("mesi paske te itilize pwogram sa pou w kalkile mwayen")
input("peze antre(Enter) pou soti: ")
