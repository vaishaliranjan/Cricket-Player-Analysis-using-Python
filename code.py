import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
data = pd.read_csv("Virat_Kohli.csv")
print(data.head())
#to check if we have null values
print(data.isnull().sum())
#to get Total runs
print(data["Runs"].sum())
#to get Average Runs
print(data["Runs"].mean())
""" TO GET THE RUNS SCORED """

matches = data.index
fig = px.line(data, x=matches, y="Runs",
 title='Runs Scored by Virat Kohli
Between 18-Aug-08 - 22-Jan-17')
fig.write_html('first_figure.html', auto_open=True)
""" ALL THE MATCHED AT DIFFERENT BATTING POSITIONS
"""

data["Pos"] = data["Pos"].map({3.0: "Batting At 3",
4.0: "Batting At 4", 2.0: "Batting At 2",
 1.0: "Batting At 1",
7.0:"Batting At 7", 5.0:"Batting At 5",
 6.0: "batting At 6"})
Pos = data["Pos"].value_counts()
label = Pos.index
counts = Pos.values
colors = ['gold','lightgreen', "pink", "blue",
"skyblue", "cyan", "orange"]
fig1 = go.Figure(data=[go.Pie(labels=label,
values=counts)])
fig1.update_layout(title_text='Number of Matches At
Different Batting Positions')
fig1.update_traces(hoverinfo='label+percent',
textinfo='value', textfont_size=30,
 marker=dict(colors=colors,
line=dict(color='black', width=3)))
fig1.write_html('second_figure.html', auto_open=True)
""" TOTAL RUNS BY VIRAT KOHLI """

label = data["Pos"]
counts = data["Runs"]
colors = ['gold','lightgreen', "pink", "blue",
"skyblue", "cyan", "orange"]
fig2 = go.Figure(data=[go.Pie(labels=label,
values=counts)])
fig2.update_layout(title_text='Runs By Virat Kohli At
Different Batting Positions')
fig2.update_traces(hoverinfo='label+percent',
textinfo='value', textfont_size=30,
 marker=dict(colors=colors,
line=dict(color='black', width=3)))
fig2.write_html('third_figure.html', auto_open=True)
""" NUMBER OF CETURIES IN FIRST INNINGS """

centuries = data.query("Runs >= 100")
fig3 = px.bar(centuries, x=centuries["Inns"], y =
centuries["Runs"],
 color = centuries["Runs"],
 title="Centuries By Virat Kohli in
First Innings Vs. Second Innings")
fig3.write_html('fourth_figure.html', auto_open=True)
""" SCORES AGAINST TEAMS """

fig4 = px.bar(data, x=data["Opposition"], y =
data["Runs"], color = data["Runs"],
 title="Most Runs Against Teams")
fig4.write_html('fifth_figure.html', auto_open=True)
#dataset for all the matches played by Vurat Kohli
where strike rate is more than 120
strike_rate = data.query("SR >= 120")
print(strike_rate)
fig5 = px.bar(strike_rate, x = strike_rate["Inns"],
 y = strike_rate["SR"],
 color = strike_rate["SR"],
 title="Virat Kohli's High Strike Rates in
First Innings Vs. Second Innings")
fig5.write_html('sixth_figure.html', auto_open=True)
""" RUNS SCORED AND FOURS PLAYED BY HIM IN EACH
INNINGS """

fig6 = px.scatter(data_frame = data, x="Runs",
 y="4s", size="SR",
trendline="ols",
 title="Relationship Between Runs
Scored and Fours")
fig6.write_html('seventh_figure.html',
auto_open=True)
""" RELATIONSHIP BETWEEN RUNS SCORED AND SIXES """

fig7 = px.scatter(data_frame = data, x="Runs",
 y="6s", size="SR",
trendline="ols",
 title= "Relationship Between Runs
Scored and Sixes")
fig7.write_html('eighth_figure.html', auto_open=True)
