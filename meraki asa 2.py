import plotly.express as px
import plotly.graph_objects as go

# Visualization 1: Bar Chart of Diagnoses by Gender
bar_chart = px.bar(data, x="Diagnosis", color="Gender", barmode="group", 
                   title="Count of Diagnoses by Gender")

# Visualization 2: Scatter Plot of Treatment Progress vs. Adherence to Treatment
# with Symptom Severity as a color scale and an age filter
scatter_plot = px.scatter(
    data, 
    x="Adherence to Treatment (%)", 
    y="Treatment Progress (1-10)",
    color="Symptom Severity (1-10)", 
    size="Mood Score (1-10)",
    hover_data=['Age', 'Gender', 'Diagnosis'],
    title="Treatment Progress vs Adherence to Treatment",
    labels={'Adherence to Treatment (%)': 'Adherence (%)', 'Treatment Progress (1-10)': 'Progress Score'},
)

# Display interactive charts
(bar_chart, scatter_plot)
