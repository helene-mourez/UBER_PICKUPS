import pandas as pd

def load_zone_data():
    zone = pd.read_csv('/Users/nicolasbour/Desktop/Projets_IA/Projets_certif/bloc_03_Machine_Learning/UBER_PICKUPS/data/taxi-zone-lookup.csv')
    print('Set with labels :', zone.shape)
    return zone


def load_2014_data(files):
    raw_2014 = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)
    print('Set with labels :', raw_2014.shape)
    return raw_2014

def load_2015_data(files):
    raw_2015 = pd.read_csv('data/uber-trip-data/uber-raw-data-janjune-15.csv')
    print('Set with labels :', raw_2015.shape)
    return raw_2015

def dataframes_stats(zone, raw_2014, raw_2015):
    # Basic stats
    dataframes = {'zone':zone, 'raw_2014':raw_2014, 'raw_2015':raw_2015}

    for name, df in dataframes.items():
        print()
        print('-------------------Dataframe : ', name, '-------------------')
        print(f"Rows :  \t {df.shape[0]}")
        print(f"Columns : \t {df.shape[1]}")

        print()
        print("Basics statistics: ")
        df_desc = df.describe(include='all') # numeric variables and catégorielles

        print("Percentage of missing values")
        df_missing_values = df.isnull().sum()/df.shape[0]*100
        print(f"{name} : \n{df_missing_values}")
    print('Done...')
    return dataframes

def observe_missing_values(dataframes):
    for name, df in dataframes.items():
        for col in df.select_dtypes(include=["object", "string"]).columns:
            df[col] = df[col].str.lower()

        print('-------------------', name, '-------------------')
        print(df.head(1))

    return dataframes
