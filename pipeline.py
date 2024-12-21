import pandas as pd
from transformer import LLMTransformer
from transformations import Transformations

class TransformationPipeline:
    def __init__(self, df: pd.DataFrame, model_name: str, huggingfacehub_api_token: str):
        """
        Initializes the transformation pipeline.
        """
        self.df = df
        self.llm_transformer = LLMTransformer(model_name, huggingfacehub_api_token)
        self.transformations = Transformations()

    def run(self, user_command: str) -> pd.DataFrame:
        """
        Runs a sequence of transformations on the DataFrame based on the user command.
        """
        transformations_list = self.llm_transformer.generate_transformations(user_command)
        df_current = self.df.copy()
        for transformation in transformations_list:
            operation = transformation["operation"]
            params = transformation["params"]
            df_current = self.transformations.execute(df_current, operation, params)

        return df_current
