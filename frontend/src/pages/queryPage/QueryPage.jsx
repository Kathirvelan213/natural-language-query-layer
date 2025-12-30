import { useEffect, useRef, useState } from "react";
import "./styles/queryPage.css";
import { PromptField } from "../../global/components/PromptField";
import { useParams } from "react-router-dom";
import { getChatConversation } from "../../apiConsumer/chatsAPI";
import { performQueryAPI } from "../../apiConsumer/queryAPI";

export function QueryPage() {
  const { id } = useParams();
  const [content, setContent] = useState([]);
  const bottomRef = useRef(null);

  useEffect(() => {
    setContent(getChatConversation(id));
  }, [id]);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [content]);

  function addQuery(newQueryResponse) {
    setContent((content) => [...content, newQueryResponse]);
  }

  async function handleNewQuery(prompt) {
    const response = await performQueryAPI(prompt);
    console.log(response.data);
    addQuery(response.data);
  }

  return (
    <div className="queryPage">
      <div className="chatContent">
        {content.map((query, idx) => {
          const records = query.result || [];
          const columns = records.length > 0 ? Object.keys(records[0]) : [];

          return (
            <div key={idx} className="query-block">
              <div className="prompt">{query.prompt}</div>
              <div className="sql">{query.sqlQuery}</div>
              <div className="result">
                {records.length === 0 ? (
                  <p>No results</p>
                ) : (
                  <table className="results-table">
                    <thead>
                      <tr>
                        {columns.map((col) => (
                          <th key={col}>{col}</th>
                        ))}
                      </tr>
                    </thead>
                    <tbody>
                      {records.map((record, i) => (
                        <tr key={i}>
                          {columns.map((col) => (
                            <td key={col}>{String(record[col] ?? "")}</td>
                          ))}
                        </tr>
                      ))}
                    </tbody>
                  </table>
                )}
              </div>
            </div>
          );
        })}
        <div ref={bottomRef} />
      </div>
      <div className="prompt-wrapper">
        <PromptField onSubmit={handleNewQuery} />
      </div>
    </div>
  );
}
