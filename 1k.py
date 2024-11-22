import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta
import uuid

# Configurar Faker
fake = Faker()
Faker.seed(12345)

def generar_nombre_unico(i, prefijo=""):
    """Genera un nombre único combinando faker con un índice"""
    return f"{prefijo}{fake.first_name()}_{i}"

def generar_csvs():
    # 1. Pokemon
    pokemons = []
    roles = ["Atacante", "Defensor", "Velocista", "Apoyo", "Todo Terreno"]
    tipos_ataque = ["Físico", "Especial", "Mixto"]
    rangos_ataque = ["Corto", "Medio", "Largo"]
    
    for i in range(1000):
        pokemons.append({
            'nombre': generar_nombre_unico(i, "Pokemon_"),
            'rol': random.choice(roles),
            'tipo_de_ataque': random.choice(tipos_ataque),
            'rango_de_ataque': random.choice(rangos_ataque)
        })
    df_pokemon = pd.DataFrame(pokemons)
    df_pokemon.to_csv('pokemon.csv', index=False)

    # 2. RangoClasificatorio
    rangos = []
    nombres_rango = ["Principiante", "Experto", "Maestro", "Gran Maestro", "Elite"]
    for i in range(1000):
        rangos.append({
            'nombre': f"{random.choice(nombres_rango)}_{i}",
            'numero': random.randint(1, 5)
        })
    df_rangos = pd.DataFrame(rangos)
    df_rangos.to_csv('rangoclasificatorio.csv', index=False)

    # 3. CirculoUnite
    circulos = []
    for i in range(1000):
        circulos.append({
            'nombre': f"Circulo_{fake.company()}_{i}",
            'descripcion': fake.text(max_nb_chars=200),
            'id': str(uuid.uuid4())[:8],
            'nmiembros': random.randint(10, 100)
        })
    df_circulos = pd.DataFrame(circulos)
    df_circulos.to_csv('circulounite.csv', index=False)

    # 4. Holoatuendo
    holoatuendos = []
    categorias = ["Común", "Raro", "Épico", "Legendario"]
    for i in range(1000):
        holoatuendos.append({
            'Po_nombre': random.choice(df_pokemon['nombre']),
            'nombre': f"Skin_{i}_{fake.word()}",
            'precio_gemas': random.randint(100, 3000),
            'categoria': random.choice(categorias)
        })
    df_holoatuendos = pd.DataFrame(holoatuendos)
    df_holoatuendos.to_csv('holoatuendo.csv', index=False)

    # 5. PasedeCombate
    pases = []
    for i in range(1000):
        h1 = df_holoatuendos.sample(n=1).iloc[0]
        h2 = df_holoatuendos.sample(n=1).iloc[0]
        pases.append({
            'numero': i + 1,
            'isPremium': random.choice([True, False]),
            'H1_Po_nombre': h1['Po_nombre'],
            'H1_nombre': h1['nombre'],
            'H2_Po_nombre': h2['Po_nombre'],
            'H2_nombre': h2['nombre']
        })
    df_pases = pd.DataFrame(pases)
    df_pases.to_csv('pasedecombate.csv', index=False)

    # 6. Jugador
    jugadores = []
    for i in range(1000):
        jugadores.append({
            'Nombre': fake.unique.user_name() + str(i),
            'N_Combates': random.randint(0, 1000),
            'Id': str(uuid.uuid4())[:8],
            'P_deportividad': random.randint(0, 100),
            'Nivel': random.randint(1, 50),
            'PC_numero': random.choice(df_pases['numero'])
        })
    df_jugadores = pd.DataFrame(jugadores)
    df_jugadores.to_csv('jugador.csv', index=False)

    # 7. Movimiento
    movimientos = []
    for i in range(1000):
        movimientos.append({
            'Po_nombre': random.choice(df_pokemon['nombre']),
            'nombre': f"Mov_{i}_{fake.word()}",
            'descripcion': fake.sentence(),
            'nivel_aprendido': random.randint(1, 15),
            'rango_de_ataque': random.choice(rangos_ataque)
        })
    df_movimientos = pd.DataFrame(movimientos)
    df_movimientos.to_csv('movimiento.csv', index=False)

    # 8. LogrosdeJugador
    logros = []
    for jugador in df_jugadores['Nombre']:
        for i in range(3):  # 3 logros por jugador
            logros.append({
                'J_Nombre': jugador,
                'nombre': f"Logro_{i}_{fake.word()}",
                'fecha_de_adquisicion': fake.date_between(start_date='-1y'),
                'descripcion': fake.sentence()
            })
    df_logros = pd.DataFrame(logros)
    df_logros.to_csv('logrosdejugador.csv', index=False)

    # 9. RopadeJugador
    ropas = []
    tipos_ropa = ["Gorra", "Camiseta", "Pantalón", "Zapatos", "Accesorios"]
    for jugador in df_jugadores['Nombre']:
        for i in range(3):  # 3 ropas por jugador
            ropas.append({
                'J_Nombre': jugador,
                'nombre': f"Ropa_{i}_{fake.word()}",
                'tipo': random.choice(tipos_ropa)
            })
    df_ropas = pd.DataFrame(ropas)
    df_ropas.to_csv('ropadejugador.csv', index=False)

    # 10. MembresiaUnite
    meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 
             'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    años = ['2023', '2024', '2025']
    membresias = []
    for mes in meses:
        for año in años:
            membresias.append({
                'mes': mes,
                'año': año,
                'nro_gemas': random.randint(500, 2000),
                'marco_exclusivo': fake.word(),
                'fondo_exclusivo': fake.word()
            })
    df_membresias = pd.DataFrame(membresias)
    df_membresias.to_csv('membresiaunite.csv', index=False)

    # Generar tablas de relaciones
    # 11. Jugador_compra_MembresiaUnite
    compras_membresia = []
    for jugador in df_jugadores.sample(n=500)['Nombre']:  # 500 jugadores compran membresía
        membresia = df_membresias.sample(n=1).iloc[0]
        compras_membresia.append({
            'J_Nombre': jugador,
            'Me_mes': membresia['mes'],
            'Me_año': membresia['año']
        })
    pd.DataFrame(compras_membresia).to_csv('jugador_compra_membresiaunite.csv', index=False)

    # 12. Jugador_tiene_Pokemon
    jugador_pokemon = []
    for jugador in df_jugadores['Nombre']:
        # Cada jugador tiene entre 2 y 5 pokemon
        num_pokemon = random.randint(2, 5)
        pokemons_jugador = df_pokemon.sample(n=num_pokemon)
        for _, pokemon in pokemons_jugador.iterrows():
            jugador_pokemon.append({
                'J_Nombre': jugador,
                'Po_nombre': pokemon['nombre']
            })
    pd.DataFrame(jugador_pokemon).to_csv('jugador_tiene_pokemon.csv', index=False)

    # 13. Jugador_tiene_RangoClasificatorio
    jugador_rango = []
    for jugador in df_jugadores['Nombre']:
        rango = df_rangos.sample(n=1).iloc[0]
        jugador_rango.append({
            'J_Nombre': jugador,
            'R_nombre': rango['nombre'],
            'R_numero': rango['numero']
        })
    pd.DataFrame(jugador_rango).to_csv('jugador_tiene_rangoclasificatorio.csv', index=False)

    # 14. Jugador_esta_CirculoUnite
    jugador_circulo = []
    for jugador in df_jugadores.sample(n=800)['Nombre']:  # 800 jugadores en círculos
        circulo = df_circulos.sample(n=1).iloc[0]
        jugador_circulo.append({
            'J_Nombre': jugador,
            'C_nombre': circulo['nombre']
        })
    pd.DataFrame(jugador_circulo).to_csv('jugador_esta_circulounite.csv', index=False)

    # 15. PasedeCombate_incluye_RopadeJugador
    pase_ropa = []
    for _, ropa in df_ropas.iterrows():
        if random.random() < 0.7:  # 70% de probabilidad de que una ropa esté en un pase
            pase = df_pases.sample(n=1).iloc[0]
            pase_ropa.append({
                'J_Nombre': ropa['J_Nombre'],
                'R_J_Nombre': ropa['J_Nombre'],
                'R_nombre': ropa['nombre'],
                'PC_numero': pase['numero']
            })
    pd.DataFrame(pase_ropa).to_csv('pasedecombate_incluye_ropadejugador.csv', index=False)

if __name__ == "__main__":
    generar_csvs()
    print("CSVs generados exitosamente")