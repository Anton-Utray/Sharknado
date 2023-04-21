#checar conteo nulos Columnas, Ascending False
def nancols(x):
    nan_cols = x.isna().sum()
    return nan_cols.sort_values(ascending=False)

#checar conteo nulos filas, Ascending False
def nanrows(x):
    nan_rows = x.isna().sum(axis=1)
    return nan_rows.sort_values(ascending=False)
