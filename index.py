import openpyxl

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

def excelsave(data, tipo, valor):
    import openpyxl
    from datetime import datetime
    import re

    # Criar um novo arquivo XLSX
    workbook = openpyxl.Workbook()

    # Selecionar a planilha ativa (por padrão, a primeira planilha é selecionada)
    sheet = workbook.active

    # Adicionar dados ao arquivo (incluindo uma data no formato "dd/mm/aaaa")
    dados = [
        [data, tipo, valor],
    ]
    
    # Converter a data no formato "dd/mm/aaaa" para o formato de data do Python (datetime)
    for linha in dados:
        data_str = linha[0]
        data = datetime.strptime(data_str, "%d/%m/%Y")
        linha[0] = data

        # Remover o símbolo "R$" e converter o valor para float
        valor_str = linha[2].replace("R$", "").replace(",", ".")
        valor = float(valor_str)
        linha[2] = valor

        sheet.append(linha)

    print(linha)
    # Salvar o arquivo XLSX
    workbook.save("exemplo.xlsx")

    # Fechar o arquivo
    workbook.close()
    return 0

vetor = []
cont = 0

workbook = openpyxl.Workbook()
sheet = workbook.active

with open('extrato.txt', 'r') as arquivo:
    final = 0 
    for linha in arquivo:
        cont+=1
        
        if(cont != 1):
            sem_aspas = linha.strip()
            a = sem_aspas.replace('"', '')
            
            vetor_final = a.split(";")

            if(vetor_final[5] != 'C' and vetor_final[3]!= 'SALDO DIA'):  
               
              excelsave(intData(vetor_final[1]), vetor_final[3], intReais(vetor_final[4]))   
                
             


    vetor_final.clear()

workbook.save("exemplo.xlsx")