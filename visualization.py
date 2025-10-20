import pandas as pd
import plotly.express as px

def plot_environment(state):
    df = pd.DataFrame([state])
    fig = px.bar(df, x=df.columns[1:], y=df.iloc[0].values[1:], 
                 labels={"x":"Metric", "y":"Value"}, title="Current Environment")
    path = "backend/data/env_plot.html"
    fig.write_html(path)
    return path
