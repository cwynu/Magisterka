import pandas as pd
import plotly.express as px

df = pd.read_csv('Data/full5.tsv', delimiter="\t", low_memory=False)

# The range of fixation times chart
fig = px.scatter(df, x='Recording timestamp [ms]', y='Participant name', title='AOI TRUCK fixation at timestamp chart')
fig.show()

# AOI histogram
df = pd.read_csv('Data/full2.tsv', delimiter="\t", low_memory=False)
fig = px.histogram(df, x='Ungrouped', color='Ungrouped',
                    labels = {'Ungrouped': 'AOI TAG'}, title = 'AOI hit duration chart')
fig.show()

# AOI hit duration at timeline chart
df = pd.read_csv('Data/full.tsv', delimiter="\t", low_memory=False)
fig = px.scatter(df, x='Recording timestamp [ms]', y='Gaze event duration [ms]', color='Ungrouped',
                labels={'Ungrouped': 'AOI TAG'}, title='AOI hit duration chart')
fig.show()

# AOI TRUCK hit duration at timeline chart for person 01
df = pd.read_csv('Data/full3.tsv', delimiter="\t", low_memory=False)
fig = px.scatter(df, x='Recording timestamp [ms]', y='Gaze event duration [ms]', color='Ungrouped',
                labels={'Ungrouped': 'AOI TAG'}, title='AOI TRUCK hit duration chart for person 01')
fig.show()

# AOI percent usage
df = pd.read_csv('Data/full2.tsv', delimiter="\t", low_memory=False)
fig = px.pie(df, values='Gaze event duration [ms]', names='Ungrouped', title='AOI percent usage')
fig.update_traces(textposition='inside', textinfo='percent+label')
fig.show()



