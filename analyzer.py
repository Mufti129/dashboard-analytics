def run_analysis(df, mode):
    if mode == "Overview":
        return {
            "total_sales": df["Nominal"].sum(),
            "total_qty": df["QTY"].sum(),
            "order_count": len(df)
        }

    elif mode == "Sales Analysis":
        return df.groupby("Channel")[["Nominal", "QTY"]].sum()

    elif mode == "Cancel Rate":
        cancel = df[df["Status"] == "CANCEL"]
        return {
            "total_order": len(df),
            "total_cancel": len(cancel),
            "cancel_rate": len(cancel) / len(df)
        }

    elif mode == "Product Insights":
        return df.groupby("Nama Barang")["QTY"].sum().sort_values(ascending=False)

    elif mode == "QTY Rank":
        rank = df.groupby("Nama Barang")["QTY"].sum()
        return rank.sort_values(ascending=False).reset_index()

    else:
        return None
