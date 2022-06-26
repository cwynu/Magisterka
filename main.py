import pandas as pd
import plotly.express as px

# Longest fixation chart
df = pd.read_csv('Data\S1\Magisterka Recording13.tsv', delimiter="\t")
fig = px.line(df, x='Gaze event duration [ms]', y='Ungrouped', color='Ungrouped',
              labels={'Ungrouped': 'AOI TAG'}, title='Longest fixation on AOI for Sceen 01 Record 13')
fig.show()


# AOI hit duration at timeline chart
df = pd.read_csv('Data\S1\Magisterka Recording13.tsv', delimiter="\t")
fig = px.scatter(df, x='Recording timestamp [ms]', y='Gaze event duration [ms]', color='Ungrouped',
                labels={'Ungrouped': 'AOI TAG'}, title='AOI hit duration chart for Sceen 01 Record 13')
fig.show()

# AOI hit percent
df = pd.read_csv('Data\S1\Magisterka Recording13.tsv', delimiter="\t")

Text = {'AoiDuration': 0, 'WholeDuration': 0, 'PercentUsage': 0 }
NPC_corp = {'AoiDuration': 0, 'WholeDuration': 0, 'PercentUsage': 0 }
NPC_face = {'AoiDuration': 0, 'WholeDuration': 0, 'PercentUsage': 0 }
Player = {'AoiDuration': 0, 'WholeDuration': 0, 'PercentUsage': 0 }
Fire = {'AoiDuration': 0, 'WholeDuration': 0, 'PercentUsage': 0 }
Truck = {'AoiDuration': 0, 'WholeDuration': 0, 'PercentUsage': 0 }

AoiTags = {'Text': Text, 'NPC_corp': NPC_corp, 'NPC_face': NPC_face, 'Player': Player, 'Fire': Fire, 'Truck': Truck}

for Text in AoiTags:
    AoiTags[Text]['WholeDuration'] = int((df['Gaze event duration [ms]']).sum())

for i in range (0, 2400):
    if (df['AOI hit [Desktop 2022.06.12 - 22.07.32.02 - Text]'][i]) == 1:
        AoiTags['Text']['AoiDuration'] += int(df['Gaze event duration [ms]'][[i]])

for i in range(0, 2400):
    if (df['AOI hit [Desktop 2022.06.12 - 22.07.32.02 - Player]'][i]) == 1:
        AoiTags['Player']['AoiDuration'] += int(df['Gaze event duration [ms]'][[i]])

for i in range(0, 2400):
    if (df['AOI hit [Desktop 2022.06.12 - 22.07.32.02 - Fire]'][i]) == 1:
        AoiTags['Fire']['AoiDuration'] += int(df['Gaze event duration [ms]'][[i]])

for i in range(0, 2400):
    if (df['AOI hit [Desktop 2022.06.12 - 22.07.32.02 - Truck]'][i]) == 1:
        AoiTags['Truck']['AoiDuration'] += int(df['Gaze event duration [ms]'][[i]])

for i in range(0, 2400):
    if (df['AOI hit [Desktop 2022.06.12 - 22.07.32.02 - NPC corp]'][i]) == 1:
        AoiTags['NPC_corp']['AoiDuration'] += int(df['Gaze event duration [ms]'][[i]])

for i in range(0, 2400):
    if (df['AOI hit [Desktop 2022.06.12 - 22.07.32.02 - NPC face]'][i]) == 1:
        AoiTags['NPC_face']['AoiDuration'] += int(df['Gaze event duration [ms]'][[i]])

AoiTags['Text']['PercentUsage'] =  ('%.2f' %  (AoiTags['Text']['AoiDuration'] * 100 / AoiTags['Text']['WholeDuration']))+ ('%')
AoiTags['NPC_corp']['PercentUsage'] = ('%.2f' %  (AoiTags['NPC_corp']['AoiDuration'] * 100 / AoiTags['NPC_corp']['WholeDuration']))+ ('%')
AoiTags['NPC_face']['PercentUsage'] = ('%.2f' %  (AoiTags['NPC_face']['AoiDuration'] * 100 / AoiTags['NPC_face']['WholeDuration']))+ ('%')
AoiTags['Player']['PercentUsage'] = ('%.2f' %  (AoiTags['Player']['AoiDuration'] * 100 / AoiTags['Player']['WholeDuration']))+ ('%')
AoiTags['Fire']['PercentUsage'] = ('%.2f' %  (AoiTags['Fire']['AoiDuration'] * 100 / AoiTags['Fire']['WholeDuration']))+ ('%')
AoiTags['Truck']['PercentUsage'] = ('%.2f' %  (AoiTags['Truck']['AoiDuration'] * 100 / AoiTags['Truck']['WholeDuration']))+ ('%')

print ( pd.DataFrame(AoiTags) )
