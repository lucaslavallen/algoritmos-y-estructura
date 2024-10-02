from ejercicio23.arbol_avl23 import BinaryTree

criaturas = [
    {
        "nombre": "Ceto",
        "derrotado": None
    },
    {
        "nombre": "Tifon",
        "derrotado": "Zeuz"
    },
    {
        "nombre": "Equidna",
        "derrotado": "Argos Panoptes"
    },
    {
        "nombre": "Dino",
        "derrotado": None
    },
    {
        "nombre": "Pefredo",
        "derrotado": None
    },
    {
        "nombre": "Enio",
        "derrotado": None
    },
    {
        "nombre": "Escila",
        "derrotado": None
    },
    {
        "nombre": "Caribdis",
        "derrotado": None
    },
    {
        "nombre": "Euriale",
        "derrotado": None
    },
    {
        "nombre": "Esteno",
        "derrotado": None
    },
    {
        "nombre": "Medusa",
        "derrotado": "Perseo"
    },
    {
        "nombre": "Ladon",
        "derrotado": "Heracles"
    },
    {
        "nombre": "Aguila del Caucaso",
        "derrotado": None
    },
    {
        "nombre": "Quimera",
        "derrotado": "Belerofonte"
    },
    {
        "nombre": "Hidra de Lerna",
        "derrotado": "Heracles"
    },
    {
        "nombre": "Leon de Nemea",
        "derrotado": "Heracles"
    },
    {
        "nombre": "Esfinge",
        "derrotado": "Edipo"
    },
    {
        "nombre": "Dragon de la Colquida",
        "derrotado": None
    },
    {
        "nombre": "Cerbero",
        "derrotado": None
    },
    {
        "nombre": "Cerdo de Cromion",
        "derrotado": "Teseo"
    },
    {
        "nombre": "Ortro",
        "derrotado": "Heracles"
    },
    {
        "nombre": "Toro de Creta",
        "derrotado": "Teseo"
    },
    {
        "nombre": "Jabali de Calidon",
        "derrotado": "Atalanta"
    },
    {
        "nombre": "Carcinos",
        "derrotado": None
    },
    {
        "nombre": "Gerion",
        "derrotado": "Heracles"
    },
    {
        "nombre": "Cloto",
        "derrotado": None
    },
    {
        "nombre": "Laquesis",
        "derrotado": None
    },
    {
        "nombre": "Artropos",
        "derrotado": None
    },
    {
        "nombre": "Minotauro de Creta",
        "derrotado": "Teseo"
    },
    {
        "nombre": "Harpias",
        "derrotado": None
    },
    {
        "nombre": "Argos Panoptes",
        "derrotado": "Hermes"
    },
    {
        "nombre": "Aves de Estinfalo",
        "derrotado": None
    },
    {
        "nombre": "Talos",
        "derrotado": "Medea"
    },
    {
        "nombre": "Sirenas",
        "derrotado": None
    },
    {
        "nombre": "Piton",
        "derrotado": "Apolo"
    },
    {
        "nombre": "Cierva de Cerinea",
        "derrotado": None
    },
    {
        "nombre": "Basilisco",
        "derrotado": None
    },
    {
        "nombre": "Jabali de Erimanto",
        "derrotado": None
    }
]

arbol = BinaryTree()

for criatura in criaturas:
    arbol.insert_node(criatura["nombre"], {"derrotado": criatura["derrotado"]})
