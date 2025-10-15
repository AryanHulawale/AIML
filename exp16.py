Total = int(input("Enter total number of samples: "))
TN = int(input("Enter True Negatives (TN): "))
FP = int(input("Enter False Positives (FP): "))
FN = int(input("Enter False Negatives (FN): "))
TP = int(input("Enter True Positives (TP): "))


Predicted_Yes = TP + FP
Actual_Yes = TP + FN

Accuracy = (TP + TN) / Total
ErrorRate = (FP + FN) / Total
Precision = TP / Predicted_Yes 
Recall = TP / Actual_Yes 

print("\nModel Performance Metrics:")
print(f"Accuracy: {Accuracy:.2f}")
print(f"Precision: {Precision:.2f}")
print(f"Recall (Sensitivity): {Recall:.2f}")
print(f"Error Rate: {ErrorRate:.2f}")
