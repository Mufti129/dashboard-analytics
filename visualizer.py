import streamlit as st
import plotly.express as px

def render_charts(results, mode):

    if mode == "Overview":
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Sales (Rp)", f"{results['total_sales']:,}")
        col2.metric("Total QTY", results["total_qty"])
        col3.metric("Total Orders", results["order_count"])

    elif mode == "Sales Analysis":
        fig = px.bar(results, x=results.index, y="Nominal")
        st.plotly_chart(fig, use_container_width=True)

    elif mode == "Cancel Rate":
        st.metric("Cancel Rate", f"{results['cancel_rate']*100:.2f}%")
        st.metric("Total Cancel", results["total_cancel"])
        st.metric("Total Orders", results["total_order"])

    elif mode == "Product Insights":
        fig = px.bar(results.head(10))
        st.plotly_chart(fig, use_container_width=True)

    elif mode == "QTY Rank":
        st.dataframe(results)
