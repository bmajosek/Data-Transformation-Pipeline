import pandas as pd

class Transformations:
    def filter(self, df: pd.DataFrame, column_name: str, predicate: str, value):
        """
        Filters the DataFrame rows based on a column and a predicate.
        """
        if not column_name in df:
            raise ValueError(f"There is no column: {column_name}")            
        if predicate == "greater":
            return df[df[column_name] > value]
        elif predicate == "less":
            return df[df[column_name] < value]
        elif predicate == "equal":
            return df[df[column_name] == value]
        else:
            raise ValueError(f"Unsupported predicate: {predicate}")

    def select(self, df: pd.DataFrame, column_names: list):
        """
        Selects specific columns from the DataFrame.
        """
        return df[column_names]

    def sort(self, df: pd.DataFrame, by: str, ascending: bool = True):
        """
        Sorts the DataFrame by a specific column.
        """
        return df.sort_values(by=by, ascending=ascending)

    def execute(self, df: pd.DataFrame, operation: str, params: dict) -> pd.DataFrame:
        """
        Executes a transformation operation on the DataFrame.
        """
        if operation == "filter":
            return self.filter(df, **params)
        elif operation == "select":
            return self.select(df, **params)
        elif operation == "sort":
            return self.sort(df, **params)
        else:
            raise ValueError(f"Unsupported operation: {operation}")
