"""
#Errado
    
"sao_paulo": {["Joao M","Maria S","Juan C"]}
    
#Errado

quantidade = sum(len(pessoas) for pessoas in lista.values())

#Errado

print(f"Quantidade total: {quantidade}")  
print(lista["rio_de_janeiro"])  



list = {
    "sao_paulo": {
        "pessoas": [
            "Joao M",
            "Maria S",
            "Juan C",
            "Patrick G"
        ]
    },
    "rio_de_janeiro": {
        "pessoas": [
            "Joao P",
            "Maria M",
            "Juan JR"
        ]
    }
}

quantidade = sum(len(local["pessoas"]) for local in list.values())

print(f"Quantidade total: {quantidade}")  # Saída: Quantidade total: 7
print(list["rio_de_janeiro"]["pessoas"])  # Saída: ['Joao P', 'Maria M', 'Juan JR']
print(list["sao_paulo"]["pessoas"]) # Saída: ['Joao M', 'Maria S', 'Juan C']
"""
lista = {
    "cidade": {
        "sao paulo": [
        "Joao M",
        "Maria S",
        "Juan C",
        "Patrick G"
        ],
        "rio de janeiro": [
            "Joao P",
            "Maria M",
            "Juan JR"
            ]
        }
    }

quantidade = sum(len(local) for local in lista["cidade"].values())
print(f"Quantidade total: {quantidade}")  # Saída: Quantidade total: 7
print(lista["cidade"]["rio de janeiro"])  # Saída: ['Joao P', 'Maria M', 'Juan JR']
