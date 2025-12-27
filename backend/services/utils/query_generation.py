from ..llms.protocol import LLM

def generate_sql(llm:LLM,schema: str, query: str) -> str:
    SCHEMA=schema
    
    SYSTEM_PROMPT = """
    You are a SQL query compiler.

    You MUST follow these rules:
    - Output ONLY raw SQL
    - Do NOT use markdown
    - Do NOT use code blocks
    - Do NOT include backticks
    - Do NOT include explanations
    - Do NOT include comments
    - Output must start directly with SELECT
    - Output must end with a semicolon

    Data type rules:
    - Text columns (including GUIDs/UUIDs) MUST be quoted with single quotes
    - Numeric columns (int, numeric, float) should NOT be quoted
    - When comparing text fields, always use quoted strings like 'value'

    Allowed statements:
    - SELECT only

    Forbidden:
    - INSERT, UPDATE, DELETE, DROP, ALTER, CREATE
    - Markdown formatting
    - Natural language

    If you violate any rule, the response is invalid.
    """

    full_prompt = f"""
    {SYSTEM_PROMPT}

    Database schema:
    {SCHEMA}

    User question:
    {query}

    SQL:
    """
    
    return llm.generate(full_prompt)