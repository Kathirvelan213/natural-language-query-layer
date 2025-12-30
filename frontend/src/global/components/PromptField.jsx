import { useState } from "react";
import "../styles/promptField.css";
import { FaPaperPlane } from "react-icons/fa";

export function PromptField({ onSubmit }) {
  const [prompt, setPrompt] = useState("");
  function handleSubmit() {
    onSubmit({ prompt: prompt });
    setPrompt("");
  }
  return (
    <div className="promptFieldPanel">
      <textarea
        className="promptFieldInput"
        placeholder="Ask Shard"
        rows={1}
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === "Enter") {
            e.preventDefault();
            handleSubmit();
          }
        }}></textarea>
      <div className="otherSettingsPanel">
        <div className="flex flex-1"></div>
        <button
          className="promptFieldButton"
          onClick={() => {
            handleSubmit();
          }}>
          <FaPaperPlane />
        </button>
      </div>
    </div>
  );
}
