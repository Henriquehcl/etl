import pandas as pd
import pandera as pa

df = pd.read_csv('ocorrencia.csv', sep=',', parse_dates=['ocorrencia_dia'], dayfirst=True)
# print(df.head(10))
# print(df.dtypes)
# limpeza de dados
# df.loc[df.ocorrencia_aerodromo == '****', ['ocorrencia_aerodromo']] = pd.NA
df.replace(['**', '###', '####', '****', '*****', '***!', 'NULL', ' '], pd.NA, inplace=True)
# print(df.isna().sum())  # exibir quantia de dados não informados
print(df.head())
# validação
schema = pa.DataFrameSchema(
    columns={
        'codigo_ocorrencia': pa.Column(pa.Int),
        'codigo_ocorrencia2': pa.Column(pa.Int),
        'ocorrencia_classificacao': pa.Column(pa.String),
        'ocorrencia_cidade': pa.Column(pa.String),
        'ocorrencia_uf': pa.Column(pa.String, pa.Check.str_length(2, 2), nullable=True),
        'ocorrencia_aerodromo': pa.Column(pa.String, nullable=True),
        'ocorrencia_dia': pa.Column(pa.String, nullable=True),
        'ocorrencia_hora': pa.Column(pa.String, pa.Check.str_matches(r'^([0-1]?[0-9]|[2][0-3]):([0-5][0-9])(:[0-5][0-9])?$'), nullable=True),
        'total_recomendacoes': pa.Column(pa.String)
    }
)
print(schema.validate(df))