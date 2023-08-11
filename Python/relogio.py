import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")
    time_label.config(text=current_time)
    time_label.after(1000, update_time)  # Atualiza a cada segundo

# Configuração da janela
root = tk.Tk()
root.title("Relógio Simples")
root.geometry("300x150")

# Rótulo para exibir o tempo
time_label = tk.Label(root, text="", font=("Helvetica", 48))
time_label.pack(pady=40)

update_time()  # Inicializa a atualização do tempo

root.mainloop()
