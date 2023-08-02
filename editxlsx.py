import tkinter as tk
from tkinter import filedialog
import openpyxl

def abrir_arquivo():
    arquivo = filedialog.askopenfilename(filetypes=[("Arquivos XLSX", "*.xlsx")])
    if arquivo:
        global workbook
        workbook = openpyxl.load_workbook(arquivo)
        update_caixa_texto()

def salvar_arquivo():
    if workbook:
        arquivo = filedialog.asksaveasfilename(filetypes=[("Arquivos XLSX", "*.xlsx")])
        if arquivo:
            workbook.save(arquivo)

def update_caixa_texto():
    if workbook:
        sheet = workbook.active
        conteudo = ""
        for row in sheet.iter_rows():
            for cell in row:
                conteudo += str(cell.value) + "\t"
            conteudo += "\n"
        texto_box.delete('1.0', tk.END)
        texto_box.insert(tk.END, conteudo)

def fechar_janela():
    if workbook:
        workbook.close()
    janela.quit()

# Configuração da janela principal
janela = tk.Tk()
janela.title("Editor de Arquivo XLSX")

workbook = None

# Botão para abrir o arquivo
btn_abrir = tk.Button(janela, text="Abrir arquivo", command=abrir_arquivo)
btn_abrir.pack(pady=10)

# Botão para salvar o arquivo
btn_salvar = tk.Button(janela, text="Salvar arquivo", command=salvar_arquivo)
btn_salvar.pack(pady=5)

# Caixa de texto para exibir e editar o conteúdo do arquivo
texto_box = tk.Text(janela, wrap="word", width=80, height=20)
texto_box.pack(padx=10, pady=5)

janela.protocol("WM_DELETE_WINDOW", fechar_janela)
janela.mainloop()