def intData(inteiro_data):
    from datetime import datetime

    # Convertendo o inteiro em uma string no formato "AAAA-MM-DD"
    data_string = str(inteiro_data)

    # Criando um objeto datetime a partir da string formatada
    data_formatada = datetime.strptime(data_string, '%Y%m%d')

    data_formatada_saida = data_formatada.strftime('%d/%m/%Y')

    return(data_formatada_saida)

def intReais(inteiro):
    import locale

    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    numero_inteiro = float(inteiro)
    valor_formatado = locale.currency(numero_inteiro / 100.0, grouping=True, symbol=True)

    return(valor_formatado)

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
                 
                print(intData(vetor_final[1]),vetor_final[3],intReais(vetor_final[4]))   


    vetor_final.clear()
