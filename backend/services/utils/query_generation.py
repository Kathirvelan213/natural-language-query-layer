from ..llms.protocol import LLM

def generate_sql(llm:LLM,schema: str, query: str) -> str:
    SCHEMA=schema
    
    SYSTEM_PROMPT = """
    You are a SQL query compiler.

    You MUST follow these rules:
    - Output ONLY raw SQL
    - Do NOT use markdown
    - Do NOT include backticks
    - Do NOT include explanations or comments
    - Output must start with SELECT
    - Output must end with a semicolon

    Formatting rules:
    - Format SQL across multiple lines
    - Place SELECT, FROM, WHERE, GROUP BY, ORDER BY on their own lines
    - Indent selected columns and conditions cleanly
    - Use standard SQL formatting conventions

    Data rules:
    - Text values MUST be wrapped in single quotes
    - Numeric values must NOT be quoted

    Allowed:
    - SELECT only

    Forbidden:
    - INSERT, UPDATE, DELETE, DROP, ALTER, CREATE
    - Markdown formatting
    - Natural language
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