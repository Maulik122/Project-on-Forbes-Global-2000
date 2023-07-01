import streamlit as st

st.title("""hello st2""")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

data = pd.read_csv("Forbes Global 2000 (Year 2022).xlsx - Sheet1.csv")


# #plot-6
# col1, col4 = st.columns(2)
# col2, col3 = st.columns(2)
# sort_by_sales = data.sort_values(by= "Sales", ascending=False)
# top10bysales = sort_by_sales.head(10)
# #st.dataframe(top10bysales)


# x = top10bysales['Company']
# y = top10bysales['Sales']
# with col1:
#     st.subheader("  Top 10 Company by Sales ")
#     fig1 = plt.figure(figsize=(10,10))
#     plt.bar(x, y, color= 'b')
#     plt.xticks(rotation=45, horizontalalignment='right')
#     plt.xlabel("Company")
#     plt.ylabel("Sales")
#     st.pyplot(fig1)

# #plot-7
# sort_by_profit = data.sort_values(by= "Profits", ascending=False)
# top10byprofit = sort_by_profit.head(10)

# x1 = top10byprofit['Company']
# y1 = top10byprofit['Profits']
# with col2:
#     st.subheader("Top 10 Company by Profits")
#     fig2 = plt.figure(figsize=(10,10))
#     plt.bar(x1, y1, color= 'cyan')
#     plt.xticks(rotation=35, horizontalalignment='right')
#     plt.xlabel("Company")
#     plt.ylabel("Profits")
#     st.pyplot(fig2)

# #plot-8
# sort_by_asset = data.sort_values(by= "Assets", ascending=False)
# top10byasset = sort_by_asset.head(10)

# x2 = top10byasset['Company']
# y2 = top10byasset['Assets']
# with col3:
#     st.subheader("Top 10 Company by Assets")
#     fig3 = plt.figure(figsize=(10,10))
#     plt.bar(x2, y2, color= 'g')
#     plt.xticks(rotation=35, horizontalalignment='right')
#     plt.xlabel("Company")
#     plt.ylabel("Assets")
#     st.pyplot(fig3)

# #plot-9
# sort_by_mv = data.sort_values(by= "Market_Value", ascending=False)
# top10bymv = sort_by_mv.head(10)

# x3 = top10bymv['Company']
# y3 = top10bymv['Market_Value']
# with col4:
#     st.subheader("Top 10 Company by Market Value")
#     fig4 = plt.figure(figsize=(10,10))
#     plt.bar(x3, y3, color= 'r')
#     plt.xticks(rotation=35, horizontalalignment='right')
#     plt.xlabel("Company")
#     plt.ylabel("Market Value")
#     st.pyplot(fig4)


#plot-3
fig1 = plt.figure(figsize=(10,10))
st.subheader("Sales by Industry")
sns.barplot(data=data, x='Industry', y= 'Sales', ci= None)
plt.xticks(rotation=45)
st.pyplot(fig1)

#plot-4
fig2 = plt.figure(figsize=(10,10))
st.subheader("Profits by Industry")
sns.barplot(data=data, x='Industry', y= 'Profits', ci= None)
plt.xticks(rotation=90)
st.pyplot(fig2)