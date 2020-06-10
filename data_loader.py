import pandas as pd


def load_data():
    print("LOADING_DATA")

    # Leyendo el excel
    excel = pd.read_excel('ABBREV.xlsx')

    # Leyendo los nombres de los alimentos
    name = excel['Shrt_Desc'].values

    # Leyendo las propiedades de los alimentos
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

    zinc = excel['Zinc_(mg)'].values
    copper = excel['Copper_mg)'].values
    manganese = excel['Manganese_(mg)'].values
    selenium = excel['Selenium_(ug)'].values
    vitamin_c = excel['Vit_C_(mg)'].values
    thiamin = excel['Thiamin_(mg)'].values
    ribolavin = excel['Riboflavin_(mg)'].values
    niacin = excel['Niacin_(mg)'].values
    pantothenic_acid = excel['Panto_Acid_mg)'].values
    vitamin_b6 = excel['Vit_B6_(mg)'].values
    folic_acid = excel['Folic_Acid_(ug)'].values
    choline = excel['Choline_Tot_(mg)'].values
    vitamin_b12 = excel['Vit_B12_(ug)'].values
    vitamin_a = excel['Vit_A_IU'].values
    lycopene = excel['Lycopene_(ug)'].values
    vitamin_e = excel['Vit_E_(mg)'].values
    vitamin_d = excel['Vit_D_IU'].values
    vitamin_k = excel['Vit_K_(ug)'].values
    cholesterol = excel['Cholestrl_(mg)'].values

    print("DATA_LOADED")

    return {
        'name': name,
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
        'sodium': sodium,
        'zinc': zinc,
        'copper': copper,
        'manganese': manganese,
        'selenium': selenium,
        'vitamin_c': vitamin_c,
        'thiamin': thiamin,
        'ribolavin': ribolavin,
        'niacin': niacin,
        'pantothenic_acid': pantothenic_acid,
        'vitamin_b6': vitamin_b6,
        'folic_acid': folic_acid,
        'choline': choline,
        'vitamin_b12': vitamin_b12,
        'vitamin_a': vitamin_a,
        'lycopene': lycopene,
        'vitamin_e': vitamin_e,
        'vitamin_d': vitamin_d,
        'vitamin_k': vitamin_k,
        'cholesterol': cholesterol
    }
