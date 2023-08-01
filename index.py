vetor = []
cont = 0

with open('extrato.txt', 'r') as arquivo:
    final = 0 
    for linha in arquivo:
        cont+=1
        
        if(cont != 1):
            vetor.insert(final,linha.strip())
            final+=1

        print(vetor)     
        vetor.clear()
