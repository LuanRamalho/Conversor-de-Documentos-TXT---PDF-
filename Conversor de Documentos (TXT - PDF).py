import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PyPDF2 import PdfReader, PdfWriter
import os


def convert_file():
    input_format = input_format_var.get()
    output_format = output_format_var.get()
    file_path = file_path_var.get()
    
    if not file_path:
        messagebox.showerror("Erro", "Por favor, escolha um arquivo!")
        return

    if input_format == output_format:
        messagebox.showerror("Erro", "Os formatos de entrada e saída não podem ser iguais!")
        return
    
    try:
        if input_format == "TXT" and output_format == "PDF":
            with open(file_path, "r", encoding="utf-8") as txt_file:
                content = txt_file.read()
            pdf_writer = PdfWriter()
            pdf_writer.add_blank_page(width=72*8.5, height=72*11)
            pdf_file = os.path.splitext(file_path)[0] + ".pdf"
            with open(pdf_file, "wb") as pdf_output:
                pdf_writer.write(pdf_output)
            messagebox.showinfo("Sucesso", f"Arquivo convertido para PDF: {pdf_file}")
        
        elif input_format == "PDF" and output_format == "TXT":
            reader = PdfReader(file_path)
            text_content = ""
            for page in reader.pages:
                text_content += page.extract_text()
            txt_file = os.path.splitext(file_path)[0] + ".txt"
            with open(txt_file, "w", encoding="utf-8") as txt_output:
                txt_output.write(text_content)
            messagebox.showinfo("Sucesso", f"Arquivo convertido para TXT: {txt_file}")
        
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")


def choose_file():
    input_format = input_format_var.get()
    filetypes = [("Arquivos de Texto", "*.txt")] if input_format == "TXT" else [("Arquivos PDF", "*.pdf")]
    file_path = filedialog.askopenfilename(filetypes=filetypes)
    file_path_var.set(file_path)


# Configuração da janela principal
root = tk.Tk()
root.title("Conversor de Arquivos")
root.geometry("400x300")
root.configure(bg="#d94fd3")

# Estilo
style = ttk.Style(root)
style.configure("TCombobox", font=("Arial", 12))

# Variáveis
input_format_var = tk.StringVar(value="TXT")
output_format_var = tk.StringVar(value="PDF")
file_path_var = tk.StringVar()

# Widgets
tk.Label(root, text="Formato de Entrada:", font=("Arial",12), bg="#d94fd3").pack(pady=5)
input_format_menu = ttk.Combobox(root, textvariable=input_format_var, values=["TXT", "PDF"], state="readonly", font=("Arial",12))
input_format_menu.pack(pady=5)

tk.Label(root, text="Formato de Saída:", font=("Arial",12), bg="#d94fd3").pack(pady=5)
output_format_menu = ttk.Combobox(root, textvariable=output_format_var, values=["TXT", "PDF"], state="readonly", font=("Arial",12))
output_format_menu.pack(pady=5)

choose_file_button = tk.Button(root, text="Escolher Arquivo", command=choose_file, font=("Arial",12), bg="indigo", fg="white")
choose_file_button.pack(pady=10)

file_path_label = tk.Label(root, textvariable=file_path_var, wraplength=350, font=("Arial",12), bg="#d94fd3")
file_path_label.pack(pady=5)

convert_button = tk.Button(root, text="Converter", command=convert_file, font=("Arial",12), bg="darkgreen", fg="white")
convert_button.pack(pady=20)

# Rodar o aplicativo
root.mainloop()
