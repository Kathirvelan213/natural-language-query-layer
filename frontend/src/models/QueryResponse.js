export class QueryResponse {
  constructor(prompt, sql, result) {
    this.prompt = prompt;
    this.sql = sql;
    this.result = result;
  }
}

