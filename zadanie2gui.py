import random
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox


def generuj_cisla():
    try:
        h = abs(int(entry_pocet.get()))
        MIN = int(entry_min.get())
        MAX = int(entry_max.get())

        if MIN > MAX:
            messagebox.showerror("Chyba", "Min musí byť menšie alebo rovné Max!")
            return

        cisla = [random.randint(MIN, MAX) for _ in range(h)]

        # Výpis výsledkov
        vysledok_text = f"Vygenerované čísla: {cisla}\n"
        vysledok_text += f"Max: {max(cisla)}\nMin: {min(cisla)}\nPriemer: {sum(cisla) / len(cisla):.2f}"
        text_vysledok.config(state='normal')
        text_vysledok.delete("1.0", tk.END)
        text_vysledok.insert(tk.END, vysledok_text)
        text_vysledok.config(state='disabled')

        # Graf
        plt.bar(range(1, h + 1), cisla, color='skyblue', edgecolor='black')
        plt.title("Vygenerované náhodné čísla")
        plt.xlabel("Poradie čísla")
        plt.ylabel("Hodnota")
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.show()

    except ValueError:
        messagebox.showerror("Chyba", "Zadajte platné celé čísla!")


# GUI
root = tk.Tk()
root.title("Generátor náhodných čísel")

# Polia vstupu
tk.Label(root, text="Počet čísel:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
entry_pocet = tk.Entry(root)
entry_pocet.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Min hodnota:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
entry_min = tk.Entry(root)
entry_min.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Max hodnota:").grid(row=2, column=0, padx=5, pady=5, sticky='e')
entry_max = tk.Entry(root)
entry_max.grid(row=2, column=1, padx=5, pady=5)

# Tlačidlo generovania
btn_generuj = tk.Button(root, text="Generovať", command=generuj_cisla)
btn_generuj.grid(row=3, column=0, columnspan=2, pady=10)

# Pole na výpis výsledkov
text_vysledok = tk.Text(root, height=10, width=50, state='disabled')
text_vysledok.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()