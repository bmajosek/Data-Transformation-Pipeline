import re
import json
from langchain.llms import HuggingFaceHub
from langchain.chains import LLMChain
from prompts import TRANSFORMATIONS_PROMPT

class LLMTransformer:
    def __init__(self, model_name: str, huggingfacehub_api_token: str):
        """
        Initializes the LLMTransformer with a Hugging Face model and API token.
        """
        self.llm = HuggingFaceHub(
            repo_id=model_name,
            huggingfacehub_api_token=huggingfacehub_api_token,
            model_kwargs={"max_length": 200}
        )
        self.chain = LLMChain(llm=self.llm, prompt=TRANSFORMATIONS_PROMPT)

    def generate_transformations(self, user_command: str):
        """
        Generates a sequence of transformations for a DataFrame based on a user command.
        """
        llm_response = self.chain.run(user_command=user_command)
        matches = re.findall(r"\[\s*{.*?}\s*\]", llm_response, flags=re.DOTALL)

        if not matches:
            raise ValueError("No JSON array found in LLM response.")

        json_array_str = matches[-1].strip()
        return json.loads(json_array_str)