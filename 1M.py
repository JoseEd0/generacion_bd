import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta
import uuid

# Configurar Faker
fake = Faker()
Faker.seed(12345)

# Lista de nombres de Pokémon reales
pokemon_names = [
    "Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard",
    "Squirtle", "Wartortle", "Blastoise", "Caterpie", "Metapod", "Butterfree",
    "Weedle", "Kakuna", "Beedrill", "Pidgey", "Pidgeotto", "Pidgeot",
    "Rattata", "Raticate", "Spearow", "Fearow", "Ekans", "Arbok",
    "Pikachu", "Raichu", "Sandshrew", "Sandslash", "Nidoran♀", "Nidorina",
    "Nidoqueen", "Nidoran♂", "Nidorino", "Nidoking", "Clefairy", "Clefable",
    "Vulpix", "Ninetales", "Jigglypuff", "Wigglytuff", "Zubat", "Golbat",
    "Oddish", "Gloom", "Vileplume", "Paras", "Parasect", "Venonat",
    "Venomoth", "Diglett", "Dugtrio", "Meowth", "Persian", "Psyduck",
    "Golduck", "Mankey", "Primeape", "Growlithe", "Arcanine", "Poliwag",
    "Poliwhirl", "Poliwrath", "Abra", "Kadabra", "Alakazam", "Machop",
    "Machoke", "Machamp", "Bellsprout", "Weepinbell", "Victreebel", "Tentacool",
    "Tentacruel", "Geodude", "Graveler", "Golem", "Ponyta", "Rapidash",
    "Slowpoke", "Slowbro", "Magnemite", "Magneton", "Farfetch'd", "Doduo",
    "Dodrio", "Seel", "Dewgong", "Grimer", "Muk", "Shellder",
    "Cloyster", "Gastly", "Haunter", "Gengar", "Onix", "Drowzee",
    "Hypno", "Krabby", "Kingler", "Voltorb", "Electrode", "Exeggcute",
    "Exeggutor", "Cubone", "Marowak", "Hitmonlee", "Hitmonchan", "Lickitung",
    "Koffing", "Weezing", "Rhyhorn", "Rhydon", "Chansey", "Tangela",
    "Kangaskhan", "Horsea", "Seadra", "Goldeen", "Seaking", "Staryu",
    "Starmie", "Mr. Mime", "Scyther", "Jynx", "Electabuzz", "Magmar",
    "Pinsir", "Tauros", "Magikarp", "Gyarados", "Lapras", "Ditto",
    "Eevee", "Vaporeon", "Jolteon", "Flareon", "Porygon", "Omanyte",
    "Omastar", "Kabuto", "Kabutops", "Aerodactyl", "Snorlax", "Articuno",
    "Zapdos", "Moltres", "Dratini", "Dragonair", "Dragonite", "Mewtwo", "Mew"
]

def generar_csvs():
    # 1. Pokemon
    print("Generando pokemon.csv...")
    pokemons = [{
        'nombre': pokemon_names[i % len(pokemon_names)],
        'rol': random.choice(["Atacante", "Defensor", "Velocista", "Apoyo", "Todo Terreno"]),
        'tipo_de_ataque': random.choice(["Físico", "Especial"]),
        'rango_de_ataque': random.choice(["Corto", "Medio", "Largo"])
    } for i in range(1000000)]
    df_pokemon = pd.DataFrame(pokemons)
    df_pokemon.to_csv('pokemon.csv', index=False)

    # 2. RangoClasificatorio
    print("Generando rangoclasificatorio.csv...")
    rangos = [{
        'nombre': f"{random.choice(['Principiante', 'Experto', 'Maestro', 'Gran Maestro', 'Elite'])}_{i}",
        'numero': random.randint(1, 5)
    } for i in range(1000000)]
    df_rangos = pd.DataFrame(rangos)
    df_rangos.to_csv('rangoclasificatorio.csv', index=False)

    # 3. CirculoUnite
    print("Generando circulounite.csv...")
    circulos = [{
        'nombre': f"Circulo_{fake.company()}_{i}",
        'descripcion': fake.text(max_nb_chars=200),
        'id': str(uuid.uuid4())[:8],
        'nmiembros': random.randint(1, 30)
    } for i in range(1000000)]
    df_circulos = pd.DataFrame(circulos)
    df_circulos.to_csv('circulounite.csv', index=False)

    # 4. Holoatuendo
    print("Generando holoatuendo.csv...")
    holoatuendos = [{
        'Po_nombre': random.choice(df_pokemon['nombre']),
        'nombre': f"Skin_{i}_{fake.word()}",
        'precio_gemas': random.randint(100, 3000),
        'categoria': random.choice(["Común", "Raro", "Épico", "Legendario"])
    } for i in range(1000000)]
    df_holoatuendos = pd.DataFrame(holoatuendos)
    df_holoatuendos.to_csv('holoatuendo.csv', index=False)

    # 5. PasedeCombate
    print("Generando pasedecombate.csv...")
    pases = [{
        'numero': i + 1,
        'isPremium': random.choice([True, False]),
        'H1_Po_nombre': random.choice(df_holoatuendos['Po_nombre']),
        'H1_nombre': random.choice(df_holoatuendos['nombre']),
        'H2_Po_nombre': random.choice(df_holoatuendos['Po_nombre']),
        'H2_nombre': random.choice(df_holoatuendos['nombre'])
    } for i in range(1000000)]
    df_pases = pd.DataFrame(pases)
    df_pases.to_csv('pasedecombate.csv', index=False)

    # 6. Jugador
    print("Generando jugador.csv...")
    jugadores = [{
        'Nombre': fake.unique.user_name() + str(i),
        'N_Combates': random.randint(0, 1000),
        'Id': str(uuid.uuid4())[:8],
        'P_deportividad': random.randint(0, 100),
        'Nivel': random.randint(1, 50),
        'PC_numero': random.choice(df_pases['numero'])
    } for i in range(1000000)]
    df_jugadores = pd.DataFrame(jugadores)
    df_jugadores.to_csv('jugador.csv', index=False)

    # 7. Movimiento
    print("Generando movimiento.csv...")
    movimientos = [{
        'Po_nombre': random.choice(df_pokemon['nombre']),
        'nombre': f"Mov_{i}_{fake.word()}",
        'descripcion': fake.sentence(),
        'nivel_aprendido': random.randint(1, 15),
        'rango_de_ataque': random.choice(["Corto", "Medio", "Largo"])
    } for i in range(1000000)]
    df_movimientos = pd.DataFrame(movimientos)
    df_movimientos.to_csv('movimiento.csv', index=False)

    # 8. LogrosdeJugador
    print("Generando logrosdejugador.csv...")
    logros = [{
        'J_Nombre': jugador,
        'nombre': f"Logro_{i}_{fake.word()}",
        'fecha_de_adquisicion': fake.date_between(start_date='-1y'),
        'descripcion': fake.sentence()
    } for jugador in df_jugadores['Nombre'] for i in range(3)]
    df_logros = pd.DataFrame(logros)
    df_logros.to_csv('logrosdejugador.csv', index=False)

    # 9. RopadeJugador
    print("Generando ropadejugador.csv...")
    ropas = [{
        'J_Nombre': jugador,
        'nombre': f"Ropa_{i}_{fake.word()}",
        'tipo': random.choice(["Gorra", "Camiseta", "Pantalón", "Zapatos", "Accesorios"])
    } for jugador in df_jugadores['Nombre'] for i in range(3)]
    df_ropas = pd.DataFrame(ropas)
    df_ropas.to_csv('ropadejugador.csv', index=False)

    # 10. MembresiaUnite
    print("Generando membresiaunite.csv...")
    meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 
             'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    años = ['2023', '2024', '2025']
    membresias = [{
        'mes': mes,
        'año': año,
        'nro_gemas': random.randint(500, 2000),
        'marco_exclusivo': fake.word(),
        'fondo_exclusivo': fake.word()
    } for mes in meses for año in años]
    df_membresias = pd.DataFrame(membresias)
    df_membresias.to_csv('membresiaunite.csv', index=False)

    # Generar tablas de relaciones
    # 11. Jugador_compra_MembresiaUnite
    print("Generando jugador_compra_membresiaunite.csv...")
    compras_membresia = [{
        'J_Nombre': jugador,
        'Me_mes': membresia['mes'],
        'Me_año': membresia['año']
    } for jugador in df_jugadores.sample(n=500000)['Nombre'] for membresia in df_membresias.sample(n=1).to_dict('records')]
    df_compras_membresia = pd.DataFrame(compras_membresia)
    df_compras_membresia.to_csv('jugador_compra_membresiaunite.csv', index=False)

    # 12. Jugador_tiene_Pokemon
    print("Generando jugador_tiene_pokemon.csv...")
    jugador_pokemon = [{
        'J_Nombre': jugador,
        'Po_nombre': pokemon
    } for jugador in df_jugadores['Nombre'] for pokemon in df_pokemon.sample(n=random.randint(2, 5))['nombre']]
    df_jugador_pokemon = pd.DataFrame(jugador_pokemon)
    df_jugador_pokemon.to_csv('jugador_tiene_pokemon.csv', index=False)

    # 13. Jugador_tiene_RangoClasificatorio
    print("Generando jugador_tiene_rangoclasificatorio.csv...")
    jugador_rango = [{
        'J_Nombre': jugador,
        'R_nombre': rango['nombre'],
        'R_numero': rango['numero']
    } for jugador in df_jugadores['Nombre'] for rango in df_rangos.sample(n=1).to_dict('records')]
    df_jugador_rango = pd.DataFrame(jugador_rango)
    df_jugador_rango.to_csv('jugador_tiene_rangoclasificatorio.csv', index=False)

    # 14. Jugador_esta_CirculoUnite
    print("Generando jugador_esta_circulounite.csv...")
    jugador_circulo = [{
        'J_Nombre': jugador,
        'C_nombre': circulo['nombre']
    } for jugador in df_jugadores.sample(n=800000)['Nombre'] for circulo in df_circulos.sample(n=1).to_dict('records')]
    df_jugador_circulo = pd.DataFrame(jugador_circulo)
    df_jugador_circulo.to_csv('jugador_esta_circulounite.csv', index=False)

    # 15. PasedeCombate_incluye_RopadeJugador
    print("Generando pasedecombate_incluye_ropadejugador.csv...")
    pase_ropa = [{
        'J_Nombre': ropa['J_Nombre'],
        'R_J_Nombre': ropa['J_Nombre'],
        'R_nombre': ropa['nombre'],
        'PC_numero': pase['numero']
    } for _, ropa in df_ropas.iterrows() if random.random() < 0.7 for pase in df_pases.sample(n=1).to_dict('records')]
    df_pase_ropa = pd.DataFrame(pase_ropa)
    df_pase_ropa.to_csv('pasedecombate_incluye_ropadejugador.csv', index=False)

if __name__ == "__main__":
    generar_csvs()
    print("CSVs generados exitosamente")