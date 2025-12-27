class SchemaPromptAdapter:
    def adapt_to_prompt(self, normalized_schema: dict) -> str:
        tables = normalized_schema.get("tables", {})

        if not tables:
            return "No tables available."

        lines: list[str] = ["Tables and columns with types:"]

        for table_name, table_meta in tables.items():
            columns = table_meta.get("columns", {})
            col_list = ", ".join(f"{col_name}:{col_type}" for col_name, col_type in columns.items())
            lines.append(f"{table_name}({col_list})")

        return "\n".join(lines)