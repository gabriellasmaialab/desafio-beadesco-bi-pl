import pandas as pd

def basic_etl(df):

    new_df = df.copy()

    # Identifying the index where the value changes to "MEDIA DETAIL - Flight Promocional"
    index_change = new_df[new_df['Unnamed: 2'] == 'MEDIA DETAIL - Flight Promocional'].index[0]

    # Excluding empty rows and columns
    new_df = new_df.dropna(how='all', axis=0)
    new_df = new_df.dropna(how='all', axis=1)

    # Creating a new column with the values
    new_df['campaign'] = 'Always On'
    new_df.loc[index_change:, 'campaign'] = 'Flight Promocional'

    #Droping useless rows

    rows_to_drop = ["MEDIA DETAIL - Always On", "PLAYERS", "Total", "MEDIA DETAIL - Flight Promocional"]
    new_df = new_df[~new_df["Unnamed: 2"].isin(rows_to_drop)]

    # Turning the first rows as columns names
    new_df.columns = new_df.iloc[0]
    new_df = new_df[1:].reset_index(drop=True)

    # Fixing campaign column name
    new_df = new_df.rename(columns = {"Always On":"Campaign"})

    # Removing heading of the second table
    new_df = new_df[new_df['site'] != 'site']

    # Changing columns dtypes
    ls_num_cols = ['planned','real','delta','imp','clicks','CTR (%)', 'CPC', 'CPM']

    for col in ls_num_cols:
        new_df[col] = pd.to_numeric(new_df[col], errors='coerce')

    return new_df