import tkinter as tk
from tkinter import messagebox


def adicionar(valor):
    visor.insert(tk.END, valor)


def inserir_decimal():
    texto = visor.get()

    if janela.operacao:
        numero_atual = texto.split(janela.operacao)[-1]
    else:
        numero_atual = texto

    if "." not in numero_atual:
        visor.insert(tk.END, ".")


def escolher_operacao(op):
    texto = visor.get()

    if texto == "":
        return

    janela.primeiro_numero = float(texto)
    janela.operacao = op
    visor.insert(tk.END, op)


def calcular():
    texto = visor.get()

    if janela.primeiro_numero is None or janela.operacao is None:
        return

    try:
        partes = texto.split(janela.operacao)

        if len(partes) != 2 or partes[1] == "":
            return

        segundo_numero = float(partes[1])

        if janela.operacao == "+":
            resultado = janela.primeiro_numero + segundo_numero

        elif janela.operacao == "-":
            resultado = janela.primeiro_numero - segundo_numero

        elif janela.operacao == "*":
            resultado = janela.primeiro_numero * segundo_numero

        else:
            if segundo_numero == 0:
                messagebox.showerror("Erro", "Não é possível dividir por zero.")
                return

            resultado = janela.primeiro_numero / segundo_numero

        expressao = f"{janela.primeiro_numero} {janela.operacao} {segundo_numero}"
        salvar_historico(expressao, resultado)

        visor.delete(0, tk.END)
        visor.insert(0, resultado)

        janela.primeiro_numero = None
        janela.operacao = None

    except:
        messagebox.showerror("Erro", "Operação inválida.")


def limpar():
    visor.delete(0, tk.END)
    janela.primeiro_numero = None
    janela.operacao = None


def apagar():
    texto = visor.get()

    if len(texto) > 0:
        visor.delete(len(texto) - 1, tk.END)


def salvar_historico(expressao, resultado):
    with open("historico.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{expressao} = {resultado}\n")


def mostrar_historico():
    historico = tk.Toplevel(janela)
    historico.title("Histórico")
    historico.geometry("400x350")
    historico.configure(bg="#1e1e1e")

    texto = tk.Text(historico, bg="#2d2d2d", fg="white", font=("Arial", 12))
    texto.pack(fill="both", expand=True, padx=10, pady=10)

    try:
        with open("historico.txt", "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()

            if conteudo.strip():
                texto.insert(tk.END, conteudo)
            else:
                texto.insert(tk.END, "Nenhuma operação registrada.")

    except FileNotFoundError:
        texto.insert(tk.END, "Nenhuma operação registrada.")

    texto.config(state="disabled")

    tk.Button(historico, text="Fechar", bg="#1565c0", fg="white", font=("Arial", 11, "bold"), command=historico.destroy).pack(pady=5)


janela = tk.Tk()
janela.title("Calculadora DS")
janela.geometry("350x550")
janela.resizable(False, False)
janela.configure(bg="#1e1e1e")

janela.primeiro_numero = None
janela.operacao = None


visor = tk.Entry(
    janela,
    font=("Arial", 22, "bold"),
    justify="right",
    bg="#2d2d2d",
    fg="white",
    insertbackground="white"
)

visor.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")


cor_numero = "#3b3b3b"
cor_operacao = "#ff9800"
cor_limpar = "#c62828"
cor_igual = "#2e7d32"
cor_historico = "#1565c0"


tk.Button(janela, text="Histórico", bg=cor_historico, fg="white", font=("Arial", 12, "bold"), command=mostrar_historico).grid(row=1, column=0, columnspan=4, sticky="nsew", padx=2, pady=2)

tk.Button(janela, text="C", bg=cor_limpar, fg="white", font=("Arial", 14, "bold"), command=limpar).grid(row=2, column=0, sticky="nsew")
tk.Button(janela, text="⌫", bg=cor_limpar, fg="white", font=("Arial", 14, "bold"), command=apagar).grid(row=2, column=1, sticky="nsew")
tk.Button(janela, text="/", bg=cor_operacao, fg="white", font=("Arial", 14, "bold"), command=lambda: escolher_operacao("/")).grid(row=2, column=2, sticky="nsew")
tk.Button(janela, text="*", bg=cor_operacao, fg="white", font=("Arial", 14, "bold"), command=lambda: escolher_operacao("*")).grid(row=2, column=3, sticky="nsew")

tk.Button(janela, text="7", bg=cor_numero, fg="white", font=("Arial", 14), command=lambda: adicionar("7")).grid(row=3, column=0, sticky="nsew")
tk.Button(janela, text="8", bg=cor_numero, fg="white", font=("Arial", 14), command=lambda: adicionar("8")).grid(row=3, column=1, sticky="nsew")
tk.Button(janela, text="9", bg=cor_numero, fg="white", font=("Arial", 14), command=lambda: adicionar("9")).grid(row=3, column=2, sticky="nsew")
tk.Button(janela, text="-", bg=cor_operacao, fg="white", font=("Arial", 14, "bold"), command=lambda: escolher_operacao("-")).grid(row=3, column=3, sticky="nsew")

tk.Button(janela, text="4", bg=cor_numero, fg="white", font=("Arial", 14), command=lambda: adicionar("4")).grid(row=4, column=0, sticky="nsew")
tk.Button(janela, text="5", bg=cor_numero, fg="white", font=("Arial", 14), command=lambda: adicionar("5")).grid(row=4, column=1, sticky="nsew")
tk.Button(janela, text="6", bg=cor_numero, fg="white", font=("Arial", 14), command=lambda: adicionar("6")).grid(row=4, column=2, sticky="nsew")
tk.Button(janela, text="+", bg=cor_operacao, fg="white", font=("Arial", 14, "bold"), command=lambda: escolher_operacao("+")).grid(row=4, column=3, sticky="nsew")

tk.Button(janela, text="1", bg=cor_numero, fg="white", font=("Arial", 14), command=lambda: adicionar("1")).grid(row=5, column=0, sticky="nsew")
tk.Button(janela, text="2", bg=cor_numero, fg="white", font=("Arial", 14), command=lambda: adicionar("2")).grid(row=5, column=1, sticky="nsew")
tk.Button(janela, text="3", bg=cor_numero, fg="white", font=("Arial", 14), command=lambda: adicionar("3")).grid(row=5, column=2, sticky="nsew")

tk.Button(janela, text="=", bg=cor_igual, fg="white", font=("Arial", 14, "bold"), command=calcular).grid(row=5, column=3, rowspan=2, sticky="nsew")

tk.Button(janela, text="0", bg=cor_numero, fg="white", font=("Arial", 14), command=lambda: adicionar("0")).grid(row=6, column=0, columnspan=2, sticky="nsew")
tk.Button(janela, text=".", bg=cor_numero, fg="white", font=("Arial", 14), command=inserir_decimal).grid(row=6, column=2, sticky="nsew")


for linha in range(7):
    janela.grid_rowconfigure(linha, weight=1)

for coluna in range(4):
    janela.grid_columnconfigure(coluna, weight=1)


janela.mainloop()