import { useState } from "react";
import "../styles/promptField.css";
import { FaPaperPlane } from "react-icons/fa";

export function PromptField({ value, onSubmit }) {
  const [prompt,setPrompt]=useState("");
  return (
    <div className="promptFieldPanel">
      <textarea className="promptFieldInput" placeholder="Ask Shard" rows={1} value={prompt} onChange={(e)=>setPrompt(e.target.value)}></textarea>
      <div className="otherSettingsPanel">
        <div className="flex flex-1"></div>
        <button className="promptFieldButton" onClick={()=>{onSubmit({prompt:prompt})}}>
          <FaPaperPlane />
        </button>
      </div>
    </div>
  );
}
