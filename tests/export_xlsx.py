import pandas as pd

data = {
  'Name': ['Bob', 'Jessica', 'Mary', 'John'],
  'City': ['SF', 'LA', 'NY', 'SF'],
  'Age': [21, 18, 19, 25]
}
df = pd.DataFrame(
  data
)
df.to_excel('武勋统计表.xlsx', index=False)
