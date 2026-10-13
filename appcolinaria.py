import requests
import tkinter as tk
from tkinter import messagebox

API_KEY = "06ed0007e4msh8306d02ab6badbbp1d25e0jsnf2bdf46b3d22"
API_HOST = "poonacular-recipe-food-nutrition-v1.p.rapidapi.com"

# Variável global para guardar as receitas pesquisadas
receitas_atuais = []

# Função para pesquisar receitas
def obter_receitas(dieta, ingredientes):
    url = f"https://{API_HOST}/recipes/complexSearch"
    params = {
        "diet": dieta,
        "includeIngredients": ingredientes,
        "number": "5",
        "addRecipeInformation": "true",
        "fillIngredients": "true"
    }
    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": API_HOST
    }

    try:
        resposta = requests.get(url, headers=headers, params=params)
        if resposta.status_code == 200:
            return resposta.json().get("results", [])
        else:
            messagebox.showerror("Erro", f"Erro ao obter receitas: {resposta.status_code}")
            return []
    except Exception as e:
        messagebox.showerror("Erro de Conexão", f"Não foi possível ligar à API: {e}")
        return []

# Função para mostrar receitas na janela
def mostrar_receitas(receitas):
    resultado_text.delete("1.0", tk.END)
    if not receitas:
        resultado_text.insert(tk.END, "Nenhuma receita encontrada.")
        return

    for receita in receitas:
        resultado_text.insert(tk.END, f"\n🍽 {receita['title']}\n")
        resultado_text.insert(tk.END, "Ingredientes:\n")
        for ing in receita.get("extendedIngredients", []):
            resultado_text.insert(tk.END, f"- {ing.get('original', '')}\n")
        resultado_text.insert(tk.END, f"\nInstruções: {receita.get('instructions', 'Sem instruções.')}\n")
        resultado_text.insert(tk.END, "-"*50 + "\n")

# Função para gerar lista de compras
def gerar_lista_compras():
    global receitas_atuais
    if not receitas_atuais:
        messagebox.showwarning("Aviso", "Pesquise receitas primeiro antes de gerar a lista de compras.")
        return

    lista = []
    for receita in receitas_atuais:
        for ing in receita.get("extendedIngredients", []):
            lista.append(ing.get('original', ''))
    
    if lista:
        messagebox.showinfo("Lista de Compras", "\n".join(lista))
    else:
        messagebox.showinfo("Lista de Compras", "Nenhum ingrediente encontrado.")

# Função acionada pelo botão de procurar
def procurar():
    global receitas_atuais
    dieta = dieta_entry.get()
    ingredientes = ingredientes_entry.get()
    if not dieta and not ingredientes:
        messagebox.showwarning("Aviso", "Por favor insira dieta ou ingredientes.")
        return
    
    receitas_atuais = obter_receitas(dieta, ingredientes)
    mostrar_receitas(receitas_atuais)

# Configuração da Janela
COR_FUNDO = "#f0f4f8"

app = tk.Tk()
app.title("Kitchen Helper")
app.geometry("800x700")
app.configure(bg=COR_FUNDO)

# Título
titulo = tk.Label(app, text="🍳 Kitchen Helper", font=("Helvetica", 18, "bold"), bg=COR_FUNDO, fg="#333333")
titulo.pack(pady=15)

# Formulário
tk.Label(app, text="Tipo de Dieta (ex: vegan, keto, gluten free):", bg=COR_FUNDO, font=("Helvetica", 10)).pack(pady=(5, 0))
dieta_entry = tk.Entry(app, width=50, font=("Helvetica", 10))
dieta_entry.pack(pady=5)

tk.Label(app, text="Ingredientes (separados por vírgulas):", bg=COR_FUNDO, font=("Helvetica", 10)).pack(pady=(5, 0))
ingredientes_entry = tk.Entry(app, width=50, font=("Helvetica", 10))
ingredientes_entry.pack(pady=5)

# Botão Procurar
btn_procurar = tk.Button(app, text="Procurar Receitas", command=procurar, bg="#4CAF50", fg="white", font=("Helvetica", 10, "bold"), padx=10, pady=5)
btn_procurar.pack(pady=10)

# Caixa de Resultados
resultado_text = tk.Text(app, wrap="word", width=80, height=20, font=("Consolas", 10))
resultado_text.pack(pady=10)

# Botão Lista de Compras
btn_compras = tk.Button(app, text="Gerar Lista de Compras", command=gerar_lista_compras, bg="#2196F3", fg="white", font=("Helvetica", 10, "bold"), padx=10, pady=5)
btn_compras.pack(pady=10)

app.mainloop()