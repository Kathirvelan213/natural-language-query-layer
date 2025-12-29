import "./styles/newQueryPage.css";
import { PromptField } from "../../global/components/PromptField";

export function NewQueryPage() {
  return (
    <div className="newQueryPage">
      <div className="logo-container-large">
        <div className="logo-text-large">Shard</div>
        <div className="subtitle">Natural Language Query Layer</div>
      </div>
      <div className="content-center">
        <PromptField />
      </div>
    </div>
  );
}
