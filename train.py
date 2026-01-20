import os
import json
from datetime import datetime

os.makedirs("artifacts", exist_ok=True)

print("Training started...")

accuracy = 0.92

# Save metrics
metrics = {
    "accuracy": accuracy,
    "timestamp": str(datetime.now())
}

with open("artifacts/metrics.json", "w") as f:
    json.dump(metrics, f, indent=4)

# Save model (dummy model file)
with open("artifacts/model.pkl", "w") as f:
    f.write("dummy trained model")

# Save logs
with open("artifacts/train.log", "w") as f:
    f.write(f"Training completed with accuracy: {accuracy}")

print("Artifacts saved successfully")
