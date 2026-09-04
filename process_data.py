import json, time

files = [
  "microservice_telemetry_primary.json",
  "api_request_logs_secondary.json",
  "worker_queue_metrics_summary.json"
]

start = time.perf_counter()

for file in files:
  with open(file) as f:
    json.load(f)

duration = (time.perf_counter() - start) * 1000

print("Processed files:", ", ".join(files))
print("Total files: 3")
print(f"Execution duration: {duration:.3f} ms")
print("Validation status: passed")
