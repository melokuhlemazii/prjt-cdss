import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from prophet import Prophet

st.title("🏥 Health Manager Dashboard - Predictive Analytics & Hotspots")

# ====== Parameters ======
locations = ['Region A', 'Region B', 'Region C', 'Region D']
total_days = 30  # simulate past 30 days
forecast_days = 7  # predict next 7 days

# ====== Simulate Daily Data ======
np.random.seed(42)
records = []
for day in range(1, total_days + 1):
    for loc in locations:
        records.append({
            'Day': day,
            'Location': loc,
            'Treated': np.random.randint(20, 100),
            'Vaccinated': np.random.randint(10, 50),
            'Tested': np.random.randint(30, 80),
            'High_BP_Cases': np.random.randint(0, 10)
        })

health_data = pd.DataFrame(records)

# ====== Summary Metrics ======
st.header("📊 Summary Metrics")
metrics = ['Treated', 'Vaccinated', 'Tested', 'High_BP_Cases']
total_metrics = {metric: health_data[metric].sum() for metric in metrics}
cols = st.columns(len(metrics))
for col, (metric, value) in zip(cols, total_metrics.items()):
    col.metric(metric, value)

# ====== Location Selection ======
st.header("📍 Location Trends & Forecast")
selected_location = st.selectbox("Select Location", locations)
loc_data = health_data[health_data['Location'] == selected_location]

# ====== Forecast Each Metric ======
st.subheader(f"📈 Forecast for Next {forecast_days} Days in {selected_location}")
forecast_df = pd.DataFrame({'Day': range(total_days+1, total_days+forecast_days+1)})

for metric in metrics:
    prophet_data = loc_data[['Day', metric]].rename(columns={'Day':'ds', metric:'y'})
    prophet_data['ds'] = pd.to_datetime(prophet_data['ds'], unit='D')
    
    model = Prophet(daily_seasonality=False)
    model.fit(prophet_data)
    
    future = model.make_future_dataframe(periods=forecast_days)
    forecast = model.predict(future)
    
    forecast_df[metric] = forecast['yhat'][-forecast_days:].values

st.dataframe(forecast_df.set_index('Day'))

# ====== Trends (Actual Data) ======
st.subheader(f"📊 Actual Trends in {selected_location}")
folded = loc_data.melt(id_vars=['Day'], 
                       value_vars=metrics,
                       var_name='Category', value_name='Count')
folded['Category'] = folded['Category'].astype(str)

line_chart = alt.Chart(folded).mark_line(point=True).encode(
    x='Day:O',
    y='Count:Q',
    color='Category:N',
    tooltip=['Day','Category','Count']
).interactive()

st.altair_chart(line_chart, use_container_width=True)

# ====== Heatmap of Activities by Location ======
st.subheader("📌 Activity Heatmap by Location")
heatmap_data = health_data.groupby('Location')[metrics].sum().reset_index()
heatmap_folded = heatmap_data.melt(id_vars=['Location'], value_vars=metrics,
                                   var_name='Category', value_name='Count')
heatmap_folded['Category'] = heatmap_folded['Category'].astype(str)

heatmap = alt.Chart(heatmap_folded).mark_rect().encode(
    x='Location:N',
    y='Category:N',
    color='Count:Q',
    tooltip=['Location','Category','Count']
)
st.altair_chart(heatmap, use_container_width=True)

# ====== Hotspot Identification ======
st.header("🔥 Hotspot Regions")
thresholds = {'Treated': 300, 'Vaccinated': 100, 'Tested': 200, 'High_BP_Cases': 20}
hotspots = []
for loc in locations:
    loc_totals = health_data[health_data['Location']==loc][metrics].sum()
    for metric in metrics:
        if loc_totals[metric] > thresholds[metric]:
            hotspots.append(f"{loc} has high {metric} ({loc_totals[metric]})")

if hotspots:
    for msg in hotspots:
        st.warning(msg)
else:
    st.success("No hotspots detected. Operations are normal.")

# ====== Resource Allocation Suggestions ======
st.header("💡 Resource Allocation Suggestions")
st.markdown("""
- Allocate staff and mobile units to regions identified as hotspots.
- Ensure sufficient vaccine and medical stock in high-demand areas.
- Monitor trends in high BP cases for preventive programs.
- Use forecasted patient load for planning next week’s schedules and supplies.
""")


