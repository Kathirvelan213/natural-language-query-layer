def validate_sql(sql: str) -> bool:
    forbidden = ["insert", "update", "delete", "drop", "alter", "create"]
    sql_lower = sql.lower()
    return (
        sql_lower.strip().startswith("select")
        and not any(word in sql_lower for word in forbidden)
    )
