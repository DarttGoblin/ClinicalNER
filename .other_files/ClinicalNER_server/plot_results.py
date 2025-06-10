import matplotlib.pyplot as plt
import numpy as np

# Metrics data from the LaTeX table
entities = ['DISEASE', 'GENE', 'PROTEIN', 'SYMPTOM']
bilstm_metrics = {
    'Precision': [0.00, 0.00, 0.00, 0.00],
    'Recall': [0.00, 0.00, 0.00, 0.00],
    'F1-score': [0.00, 0.00, 0.00, 0.00]
}

bilstm_crf_metrics = {
    'Precision': [1.00, 1.00, 1.00, 0.99],
    'Recall': [1.00, 1.00, 0.99, 1.00],
    'F1-score': [1.00, 1.00, 1.00, 1.00]
}

# Define bar width and positions
x = np.arange(len(entities))
width = 0.25

# Plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plotting for each metric
ax.bar(x - width, bilstm_metrics['Precision'], width, label='BiLSTM - Precision', color='lightcoral')
ax.bar(x, bilstm_metrics['Recall'], width, label='BiLSTM - Recall', color='indianred')
ax.bar(x + width, bilstm_metrics['F1-score'], width, label='BiLSTM - F1-score', color='firebrick')

ax.bar(x - width, bilstm_crf_metrics['Precision'], width, label='BiLSTM+CRF - Precision', color='lightgreen', bottom=bilstm_metrics['Precision'])
ax.bar(x, bilstm_crf_metrics['Recall'], width, label='BiLSTM+CRF - Recall', color='mediumseagreen', bottom=bilstm_metrics['Recall'])
ax.bar(x + width, bilstm_crf_metrics['F1-score'], width, label='BiLSTM+CRF - F1-score', color='seagreen', bottom=bilstm_metrics['F1-score'])

# Aesthetic
ax.set_ylabel('Score')
ax.set_title('Evaluation Metrics per Entity Type')
ax.set_xticks(x)
ax.set_xticklabels(entities)
ax.set_ylim(0, 1.2)
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=2)
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Save as .jpg
plt.tight_layout()
plt.savefig('per_class_metrics.jpg', dpi=300)
plt.show()