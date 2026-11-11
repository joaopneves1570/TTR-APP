import json

# Abreviações das cores para manter a lista limpa e legível
cz = "cinza"
az = "azul"
vm = "vermelho"
vd = "verde"
am = "amarelo"
pr = "preto"
br = "branco"
lr = "laranja"
rs = "rosa"

# Lista completa com todas as 100 rotas do mapa original (EUA)
# Formato: (cidade_1, cidade_2, quantidade_vagoes, cor)
rotas = [
    # Costa Oeste e Noroeste
    ("Vancouver", "Seattle", 1, cz),
    ("Vancouver", "Seattle", 1, cz),
    ("Vancouver", "Calgary", 3, cz),
    ("Seattle", "Portland", 1, cz),
    ("Seattle", "Portland", 1, cz),
    ("Seattle", "Calgary", 4, cz),
    ("Seattle", "Helena", 6, am),
    ("Portland", "San Francisco", 5, vd),
    ("Portland", "San Francisco", 5, rs),
    ("Portland", "Salt Lake City", 6, az),
    ("San Francisco", "Salt Lake City", 5, lr),
    ("San Francisco", "Salt Lake City", 5, br),
    ("San Francisco", "Los Angeles", 3, am),
    ("San Francisco", "Los Angeles", 3, rs),
    ("Los Angeles", "Las Vegas", 2, cz),
    ("Los Angeles", "Phoenix", 3, cz),
    ("Los Angeles", "El Paso", 6, pr),

    # Região das Montanhas Rochosas e Canadá Oeste
    ("Calgary", "Winnipeg", 6, br),
    ("Calgary", "Helena", 4, cz),
    ("Helena", "Winnipeg", 4, az),
    ("Helena", "Duluth", 6, lr),
    ("Helena", "Omaha", 5, vm),
    ("Helena", "Denver", 4, vd),
    ("Helena", "Salt Lake City", 3, rs),
    ("Salt Lake City", "Las Vegas", 3, lr),
    ("Salt Lake City", "Denver", 3, vm),
    ("Salt Lake City", "Denver", 3, am),
    ("Phoenix", "Denver", 5, br),
    ("Phoenix", "Santa Fe", 3, cz),
    ("Phoenix", "El Paso", 3, cz),

    # Centro-Oeste e Sul Central
    ("Denver", "Omaha", 4, rs),
    ("Denver", "Kansas City", 4, pr),
    ("Denver", "Kansas City", 4, lr),
    ("Denver", "Oklahoma City", 4, vm),
    ("Denver", "Santa Fe", 2, cz),
    ("Santa Fe", "Oklahoma City", 3, az),
    ("Santa Fe", "El Paso", 2, cz),
    ("El Paso", "Oklahoma City", 5, am),
    ("El Paso", "Dallas", 4, vm),
    ("El Paso", "Houston", 6, vd),
    ("Winnipeg", "Sault St. Marie", 6, cz),
    ("Winnipeg", "Duluth", 4, pr),
    ("Duluth", "Sault St. Marie", 3, cz),
    ("Duluth", "Toronto", 6, rs),
    ("Duluth", "Chicago", 3, vm),
    ("Duluth", "Omaha", 2, cz),
    ("Duluth", "Omaha", 2, cz),
    ("Omaha", "Chicago", 4, az),
    ("Omaha", "Kansas City", 1, cz),
    ("Omaha", "Kansas City", 1, cz),
    ("Kansas City", "Saint Louis", 2, az),
    ("Kansas City", "Saint Louis", 2, rs),
    ("Kansas City", "Oklahoma City", 2, cz),
    ("Kansas City", "Oklahoma City", 2, cz),
    ("Oklahoma City", "Little Rock", 2, cz),
    ("Oklahoma City", "Dallas", 2, cz),
    ("Oklahoma City", "Dallas", 2, cz),
    ("Dallas", "Little Rock", 2, cz),
    ("Dallas", "Houston", 1, cz),
    ("Dallas", "Houston", 1, cz),
    ("Houston", "New Orleans", 2, cz),

    # Meio-Oeste e Grandes Lagos
    ("Sault St. Marie", "Montréal", 5, pr),
    ("Sault St. Marie", "Toronto", 2, cz),
    ("Toronto", "Montréal", 3, cz),
    ("Toronto", "Pittsburgh", 2, cz),
    ("Toronto", "Chicago", 4, br),
    ("Chicago", "Pittsburgh", 3, lr),
    ("Chicago", "Pittsburgh", 3, pr),
    ("Chicago", "Saint Louis", 2, vd),
    ("Chicago", "Saint Louis", 2, br),
    ("Saint Louis", "Pittsburgh", 5, vd),
    ("Saint Louis", "Nashville", 2, cz),
    ("Saint Louis", "Little Rock", 2, cz),
    ("Little Rock", "Nashville", 3, br),
    ("Little Rock", "New Orleans", 3, vd),

    # Costa Leste e Sudeste
    ("Montréal", "Boston", 2, cz),
    ("Montréal", "Boston", 2, cz),
    ("Montréal", "New York", 3, az),
    ("Boston", "New York", 2, am),
    ("Boston", "New York", 2, vm),
    ("New York", "Pittsburgh", 2, br),
    ("New York", "Pittsburgh", 2, vd),
    ("New York", "Washington", 2, lr),
    ("New York", "Washington", 2, pr),
    ("Pittsburgh", "Washington", 2, cz),
    ("Pittsburgh", "Raleigh", 2, cz),
    ("Pittsburgh", "Nashville", 4, am),
    ("Washington", "Raleigh", 2, cz),
    ("Washington", "Raleigh", 2, cz),
    ("Raleigh", "Nashville", 3, pr),
    ("Raleigh", "Atlanta", 2, cz),
    ("Raleigh", "Atlanta", 2, cz),
    ("Raleigh", "Charleston", 2, cz),
    ("Nashville", "Atlanta", 1, cz),
    ("Atlanta", "Charleston", 2, cz),
    ("Atlanta", "Miami", 5, az),
    ("Atlanta", "New Orleans", 4, am),
    ("Atlanta", "New Orleans", 4, lr),
    ("Charleston", "Miami", 4, rs),
    ("New Orleans", "Miami", 6, vm)
]

# Extrai as 36 cidades únicas
cidades_unicas = sorted({cidade for origem, destino, _, _ in rotas for cidade in (origem, destino)})
nodes = [{"id": cidade} for cidade in cidades_unicas]

# Cria as 100 arestas com IDs únicos
edges = [
    {
        "id": f"rota_{i}",
        "source": origem,
        "target": destino,
        "length": vagoes,
        "color": cor
    }
    for i, (origem, destino, vagoes, cor) in enumerate(rotas, start=1)
]

# Estrutura final do grafo
grafo = {
    "edition": "USA",
    "directed": False,
    "nodes": nodes,
    "edges": edges
}

# Gera o arquivo JSON
with open("ticket_to_ride_usa.json", "w", encoding="utf-8") as arquivo:
    json.dump(grafo, arquivo, ensure_ascii=False, indent=2)

print(f"Arquivo gerado com sucesso: {len(nodes)} cidades e {len(edges)} rotas!")
