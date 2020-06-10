import pandas as pd


def load_data():
    print("LOADING_DATA")
    excel = pd.read_excel('ABBREV.xlsx')
    water = excel['Water_(g)'].values
    energy = excel['Energ_Kcal'].values
    protein = excel['Protein_(g)'].values
    lipid = excel['Lipid_Tot_(g)'].values
    carbohydrt = excel['Carbohydrt_(g)'].values
    fiber = excel['Fiber_TD_(g)'].values
    sugar = excel['Sugar_Tot_(g)'].values
    calcium = excel['Calcium_(mg)'].values
    iron = excel['Iron_(mg)'].values
    magnesium = excel['Magnesium_(mg)'].values
    phosphorus = excel['Phosphorus_(mg)'].values
    potassium = excel['Potassium_(mg)'].values
    sodium = excel['Sodium_(mg)'].values

    print("DATA_LOADED")

    return {
        'water': water,
        'energy': energy,
        'protein': protein,
        'lipid': lipid,
        'carbohydrt': carbohydrt,
        'fiber': fiber,
        'sugar': sugar,
        'calcium': calcium,
        'iron': iron,
        'magnesium': magnesium,
        'phosphorus': phosphorus,
        'potassium': potassium,
        'sodium': sodium
    }
