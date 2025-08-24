km_percorridos = float(input("Quantos km foram percorridos? "))
dias_alugados = int(input("Quantos dias o carro foi alugado? "))

preco_total = (dias_alugados * 60) + (km_percorridos * 0.15)

print("Preço a pagar: R$", preco_total)
