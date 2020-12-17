A = float(30000)
B = float(100000)
Ano = int(0)

while A < B:
    A = A + (A*(2.5/100))
    B = B + (B*(1.8/100))
    Ano = Ano + 1

print(f'Após {Ano} anos a cidade B, com {B:.1f} habitantes, ultrapssa a cidade A, com {A:.1f} habitantes')
