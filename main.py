from mira_sdk import MiraClient

# Initialize the client
client = MiraClient(config={"API_KEY": "YOUR_API_KEY"})

# Specify version and input data
version = "1.0.0"
input_data = {
    "tone": "gentle",
    "theme": "stars",
    "audience": "babies"
}

# Determine flow name
if version:
    flow_name = f"@ashutoshsinha/lullaby-generator/{version}"
else:
    flow_name = "@ashutoshsinha/lullaby-generator"

# Execute the flow and display the result
try:
    result = client.flow.execute(flow_name, input_data)
    print("Generated Lullaby:")
    print(result)
except Exception as e:
    print("An error occurred:", e)
