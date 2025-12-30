import { Prism as SyntaxHighlighter } from "react-syntax-highlighter";
import { oneDark } from "react-syntax-highlighter/dist/esm/styles/prism";

export function SqlBlock({ sql }) {
  return (
    <div className="bg-black rounded-md p-2 w-full">
      <SyntaxHighlighter
        language="sql"
        style={oneDark}
        customStyle={{
          background: "transparent",
          padding: 0,
          margin: 0,
          fontSize: "0.75rem",
        }}
        codeTagProps={{
          style: {
            background: "transparent",
          },
        }}
        wrapLines={true}>
        {sql}
      </SyntaxHighlighter>
    </div>
  );
}
