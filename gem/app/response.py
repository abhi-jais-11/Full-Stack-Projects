import google.generativeai as genai

# Configure the API key
genai.configure(api_key="AIzaSyDLgYxibq5nEouSP89Qzfv_69ZnFgFGM-A")

# Load the model (e.g., gemini-pro or gemini-1.5-pro)
model = genai.GenerativeModel("gemini-1.5-pro")


def generate_content(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"


# Generate content


if __name__ == "__main__":
    generate_content()
