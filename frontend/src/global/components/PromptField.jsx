import "../styles/promptField.css";
import { FaPaperPlane } from "react-icons/fa";

export function PromptField({ value, onSubmit }) {
  return (
    <div className="promptFieldPanel">
      <textarea className="promptFieldInput" placeholder="Ask Shard" rows={1}></textarea>
      <div className="otherSettingsPanel">
        <div className="flex flex-1"></div>
        <button className="promptFieldButton">
          <FaPaperPlane />
        </button>
      </div>
    </div>
  );
}
