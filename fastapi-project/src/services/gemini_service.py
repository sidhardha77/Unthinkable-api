import google.generativeai as genai


class GeminiService:
    def __init__(self):
        genai.configure(api_key="api_key")
        self.model = genai.GenerativeModel("models/gemini-flash-lite-latest")

    def generate(self, prompt: str):
        # for m in genai.list_models():
        #     print(m.name)
        response = self.model.generate_content(prompt)
        return response.text