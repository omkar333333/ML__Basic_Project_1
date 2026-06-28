import pandas as pd
import polars as pl

data={
    "name":['pawan','kapil','lalit','ishan','om'],
    "age":[25,None,44,23,None],
    "salary":[50000,60000,70000,None,None]

}
df=pd.DataFrame(data)
dl=pl.Dataframe(df)
print(df)
