
import ollama

# Step 1: Define the model
model_name = "llama3.2:1b"

# Step 2: Send a prompt to the local LLM
response = ollama.chat(
    model=model_name,
    messages=[
        {
            "role": "user",
            "content": "What is Artificial Intelligence? Explain in simple words."
        }
    ]
)

# Step 3: Display the generated response
print("\nLLM Response:")
print(response["message"]["content"])

