import io
import pandas as pd
from domino.data_sources import DataSourceClient

ds = DataSourceClient().get_datasource("S3_Auto_Data")

data = io.BytesIO(ds.get("GT_Data_2022-01-11.csv"))
df = pd.read_csv(data)

df