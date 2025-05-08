import re
import tkinter as tk
from tkinter import scrolledtext

# Palabras clave de Python
palabras_clave = {
    "if", "else", "while", "for", "def", "return", "class", "import",
    "in", "not", "and", "or", "break", "continue", "True", "False", "int",
    "print", "float", "str"
}

# Expresiones regulares
regex_tab = r"\t+"
regex_espacio = r"[ ]+"
regex_operadores = r"(<=|>=|<>|><|=|<|>)"
regex_numero = r"\d+(\.\d+)?([eE][+-]?\d+)?"
regex_identificador = r"[a-zA-Z_][a-zA-Z0-9_]*"

def analizar_linea(linea, numero_linea):
    tokens = []
    i = 0
    while i < len(linea):
        sub = linea[i:]

        if match := re.match(regex_tab, sub):
            tokens.append(("TABULACION", repr(match.group())))
        elif match := re.match(regex_espacio, sub):
            tokens.append(("ESPACIO", repr(match.group())))
        elif match := re.match(regex_operadores, sub):
            tokens.append(("OPERADOR_RELACIONAL", match.group()))
        elif match := re.match(regex_numero, sub):
            tokens.append(("NUMERO", match.group()))
        elif match := re.match(regex_identificador, sub):
            valor = match.group()
            tipo = "PALABRA_CLAVE" if valor in palabras_clave else "IDENTIFICADOR"
            tokens.append((tipo, valor))
        else:
            tokens.append(("CARÁCTER_ESPECIAL", sub[0]))
            match = None

        i += len(match.group()) if match else 1

    resultado = f"Línea {numero_linea}: {linea.strip()}\n"
    for tipo, valor in tokens:
        resultado += f"  {tipo:20}: {valor}\n"
    return resultado

def analizar_texto():
    texto = entrada.get("1.0", tk.END).splitlines()
    salida.delete("1.0", tk.END)
    for idx, linea in enumerate(texto, 1):
        resultado = analizar_linea(linea, idx)
        salida.insert(tk.END, resultado + "\n")

# Crear ventana
ventana = tk.Tk()
ventana.title("Analizador Léxico")
ventana.geometry("700x600")
ventana.configure(bg="#f4f4f4")

titulo = tk.Label(ventana, text="Analizador Léxico Simple", font=("Arial", 16, "bold"), bg="#f4f4f4")
titulo.pack(pady=10)

entrada = scrolledtext.ScrolledText(ventana, width=80, height=15, font=("Consolas", 12))
entrada.pack(padx=10, pady=10)

boton = tk.Button(ventana, text="Analizar", command=analizar_texto, font=("Arial", 12), bg="#4CAF50", fg="white", padx=10, pady=5)
boton.pack(pady=5)

salida = scrolledtext.ScrolledText(ventana, width=80, height=15, font=("Consolas", 11), bg="#eef0f2")
salida.pack(padx=10, pady=10)

ventana.mainloop()
