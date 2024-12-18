import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates
import numpy as np

# Data dan tanggal dari tim pekerja proyek
data = {
    'Task': [
        'Inisiasi Proyek',
        'Analisis Kebutuhan Pengguna',
        'Riset Pengguna',
        'Penyusunan Dokumen Spesifikasi',
        'Desain',
        'Desain Arsitektur Sistem',
        'Desain Database',
        'Desain Antarmuka Pengguna',
        'Pengembangan',
        'Setup Lingkungan dan Pengembangan Backend',
        'Pengembangan Frontend',
        'Integrasi dan Pengujian',
        'Unit Testing',
        'Integration Testing',
        'User Acceptance Testing (UAT)',
        'Deployment',
        'Persiapan Server Produksi',
        'Migrasi Data',
        'Go-live Soft Launch',
        'Post-launch',
        'Monitoring dan Optimasi Sistem',
        'Pelatihan Pengguna dan Dukungan Teknis'
    ],
    'Start': [
        '2024-01-01', '2024-01-01', '2024-01-16', '2024-01-23',
        '2024-02-01', '2024-02-01', '2024-02-15', '2024-02-22',
        '2024-03-01', '2024-03-01', '2024-04-01',
        '2024-05-01', '2024-05-01', '2024-05-16', '2024-05-24',
        '2024-06-01', '2024-06-01', '2024-06-16', '2024-06-24',
        '2024-07-01', '2024-07-01', '2024-08-01'
    ],
    'Finish': [
        '2024-01-31', '2024-01-15', '2024-01-22', '2024-01-31',
        '2024-02-29', '2024-02-14', '2024-02-21', '2024-02-29',
        '2024-04-30', '2024-03-15', '2024-04-30',
        '2024-05-31', '2024-05-15', '2024-05-23', '2024-05-31',
        '2024-06-30', '2024-06-15', '2024-06-23', '2024-06-30',
        '2024-08-31', '2024-07-31', '2024-08-31'
    ]
}

df = pd.DataFrame(data)

df['Start'] = pd.to_datetime(df['Start'])
df['Finish'] = pd.to_datetime(df['Finish'])

df['Duration'] = (df['Finish'] - df['Start']).dt.days + 1

df['Task_Position'] = range(len(df))

colors = plt.cm.tab20(np.linspace(0, 1, len(df)))

plt.figure(figsize=(14, 8))
plt.barh(df['Task_Position'], df['Duration'], left=df['Start'].map(pd.Timestamp.toordinal), color=colors)

plt.yticks(df['Task_Position'], df['Task'], fontsize=10)
plt.xlabel('Tanggal', fontsize=12)
plt.title('Gantt Chart Proyek Perangkat Lunak', fontsize=14, fontweight='bold')
plt.grid(axis='x', linestyle='--', alpha=0.7)

plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
plt.xticks(rotation=45)

for index, row in df.iterrows():
    plt.text(row['Start'].toordinal() + row['Duration']/2, index, str(row['Duration']), 
             ha='center', va='center', color='white', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.show()
