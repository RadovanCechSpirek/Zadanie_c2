import random
import matplotlib.pyplot as plt

čisla = []
h = abs(int(input("Zadaj počet čísel koľko chceš vygenerovať: ")))
MIN = int(input("Zadaj rozsah: min číslo: "))
MAX = int(input("Zadaj rozsah: max číslo: "))

print("Vygenerované čísla sú:")

for a in range(h):
    čislo = random.randint(MIN, MAX)
    print(čislo)
    čisla.append(čislo)

print(f"Max: {max(čisla)}\nMin: {min(čisla)}\nPriemer: {sum(čisla)/len(čisla):.2f}")

plt.bar(range(1, h + 1), čisla, color='skyblue', edgecolor='black')
plt.title("Vygenerované náhodné čísla")
plt.xlabel("Poradie čísla")
plt.ylabel("Hodnota")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()