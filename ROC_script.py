import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('ROC_2WZX.csv')

# Set threshold for IC50 (e.g., < 1000 is active)
threshold = 1000
data['binary_label'] = (data['Experimental IC50'] < threshold).astype(int)

# Invert binding affinity so higher = more likely active
data['score'] = -data['Binding Affinity (kcal/mol)']

true_labels = data['binary_label'].tolist()
scores = data['score'].tolist()

# Sort by predicted scores descending (higher = more likely active)
sorted_pairs = sorted(zip(true_labels, scores), key=lambda x: x[1], reverse=True)
true_labels, scores = zip(*sorted_pairs)

P = sum(true_labels)
N = len(true_labels) - P

tpr = []
fpr = []
TP = 0
FP = 0
prev_score = None

for i in range(len(true_labels)):
    if scores[i] != prev_score:
        tpr.append(TP / P if P else 0)
        fpr.append(FP / N if N else 0)
        prev_score = scores[i]
    if true_labels[i] == 1:
        TP += 1
    else:
        FP += 1

tpr.append(TP / P if P else 0)
fpr.append(FP / N if N else 0)

# Calculate AUC
auc = 0.0
for i in range(1, len(tpr)):
    auc += (fpr[i] - fpr[i-1]) * (tpr[i] + tpr[i-1]) / 2

plt.figure()
plt.plot(fpr, tpr, marker='o', linestyle='-', color='b', label=f'ROC curve (AUC = {auc:.3f})')
plt.plot([0, 1], [0, 1], linestyle='--', color='r', label='Random guess')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend(loc='lower right')
plt.grid(True)
plt.show()

print(f'AUC: {auc:.3f}')
