vetor = []
cont = 0

with open('extrato.txt', 'r') as arquivo:
    final = 0 
    for linha in arquivo:
        cont+=1
        
        if(cont != 1):
            sem_aspas = linha.strip()
            a = sem_aspas.replace('"', '')
            
            vetor_final = a.split(";")

            if(vetor_final[5] != 'C' and vetor_final[3]!= 'SALDO DIA'):    
                print(vetor_final[1],vetor_final[3],vetor_final[4])   


    vetor_final.clear()
