import google.auth
import pandas_gbq
import pandas as pd

def gcp_conection():    
    credentials, project = google.auth.default(scopes=['https://www.googleapis.com/auth/cloud-platform'])
    sql = """
        select 1
    """
    df = pandas_gbq.read_gbq(sql, project_id="nome_projeto", credentials=credentials)
    return df

df = pd.DataFrame(gcp_conection())

print(df)
# print('Convertendo pra Excel')
# df.to_excel('camiho_destino', index=False)
