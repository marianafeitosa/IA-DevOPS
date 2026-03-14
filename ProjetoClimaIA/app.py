import statistics

def classificar_temperatura(temp):
    if temp <= 15:
        return "frio"
    elif 16 <= temp <= 25:
        return "agradável"
    else:
        return "calor"


def recomendar_roupa(classificacao):
    if classificacao == "frio":
        return "Use casaco, blusa de manga longa e calça."
    elif classificacao == "agradável":
        return "Use camiseta ou camisa leve e calça ou bermuda."
    else:
        return "Use roupas leves como camiseta, shorts e beba bastante água."


def coletar_temperaturas():
    temperaturas = []
    dias = int(input("Quantos dias deseja registrar? "))

    for i in range(dias):
        temp = float(input(f"Digite a temperatura do dia {i+1}: "))
        temperaturas.append(temp)

    return temperaturas


def analisar_temperaturas(temperaturas):
    media = statistics.mean(temperaturas)
    classificacao = classificar_temperatura(media)
    recomendacao = recomendar_roupa(classificacao)

    return media, classificacao, recomendacao


def main():
    print("=== Sistema de Recomendação de Roupas ===")

    temperaturas = coletar_temperaturas()

    media, classificacao, recomendacao = analisar_temperaturas(temperaturas)

    print("\nResultado da análise:")
    print(f"Média de temperatura: {media:.2f}°C")
    print(f"Clima: {classificacao}")
    print(f"Recomendação: {recomendacao}")


if __name__ == "__main__":
    main()