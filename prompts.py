from langchain.prompts import PromptTemplate

TRANSFORMATIONS_PROMPT = PromptTemplate(
    input_variables=["user_command"],
    template="""You are an assistant that MUST return strictly valid JSON array and nothing else.
User command: {user_command}

Return a JSON array describing transformations.
Allowed operations: filter, select, sort. 
Examples: 
filter example: {{"operation":"filter","params":{{"column_name":"age","predicate":"greater","value":23}}}}
select example: {{"operation":"select","params":{{"column_names":["age","id"]}}}}
sort example: {{"operation":"sort","params":{{"by":"age","ascending":true}}}}
Output Example:
[
    {{"operation": "filter", "params": {{"column_name": "age", "predicate": "greater", "value": 23}}}},
    {{"operation": "select", "params": {{"column_names": ["age", "id"]}}}}
]
"""
)