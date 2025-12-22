from ..llms.protocol import LLM

def generate_sql(llm:LLM,query: str) -> str:
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

    Allowed statements:
    - SELECT only

    Forbidden:
    - INSERT, UPDATE, DELETE, DROP, ALTER, CREATE
    - Markdown formatting
    - Natural language

    If you violate any rule, the response is invalid.
    """


    SCHEMA = """
    tables:

    users(
    id integer,
    email text,
    created_at timestamp
    )

    orders(
    id integer,
    user_id integer,
    amount numeric,
    created_at timestamp
    )
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