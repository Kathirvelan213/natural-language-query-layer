import { useState } from "react";
import "../styles/promptField.css";
import { FaPaperPlane, FaLink } from "react-icons/fa";

export function PromptField({ onSubmit }) {
  const [prompt, setPrompt] = useState("");
  const [isConnected, setIsConnected] = useState(false);
  const [showConnectForm, setShowConnectForm] = useState(false);

  function handleSubmit() {
    onSubmit(prompt);
    setPrompt("");
  }
  return (
    <div className="promptFieldPanel relative">
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
        <div className="flex">
          <button className="connectButton" onClick={() => setShowConnectForm((v) => !v)}>
            <FaLink className="h-[12px]" />
            Connect
          </button>
        </div>
        <button
          className="promptFieldButton"
          onClick={() => {
            handleSubmit();
          }}>
          <FaPaperPlane />
        </button>
      </div>
      <ConnectionMenu isConnected={isConnected} setIsConnected={setIsConnected} showConnectForm={showConnectForm} setShowConnectForm={setShowConnectForm}/>
    </div>
  );
}
function ConnectionMenu({ isConnected, setIsConnected, setShowConnectForm, showConnectForm }) {
  const [connForm, setConnForm] = useState({
    host: "",
    port: "",
    database: "",
    user: "",
    password: "",
  });

  const handleConnectSubmit = (e) => {
    e.preventDefault();
    if (onConnect) {
      onConnect(connForm);
    }
    setShowConnectForm(false);
  };
  return (
    <div className={`connectPopover ${showConnectForm ? "open" : ""}`} aria-hidden={!showConnectForm}>
      <form onSubmit={handleConnectSubmit} className="connectForm">
        <div className="connectRow">
          <label>Host</label>
          <input type="text" value={connForm.host} onChange={(e) => setConnForm({ ...connForm, host: e.target.value })} disabled={!showConnectForm} />
        </div>
        <div className="connectRow">
          <label>Port</label>
          <input type="text" value={connForm.port} onChange={(e) => setConnForm({ ...connForm, port: e.target.value })} disabled={!showConnectForm} />
        </div>
        <div className="connectRow">
          <label>Database</label>
          <input
            type="text"
            value={connForm.database}
            onChange={(e) => setConnForm({ ...connForm, database: e.target.value })}
            disabled={!showConnectForm}
          />
        </div>
        <div className="connectRow">
          <label>User</label>
          <input type="text" value={connForm.user} onChange={(e) => setConnForm({ ...connForm, user: e.target.value })} disabled={!showConnectForm} />
        </div>
        <div className="connectRow">
          <label>Password</label>
          <input
            type="password"
            value={connForm.password}
            onChange={(e) => setConnForm({ ...connForm, password: e.target.value })}
            disabled={!showConnectForm}
          />
        </div>
        <div className="connectActions">
          <button type="button" onClick={() => setShowConnectForm(false)} disabled={!showConnectForm}>
            Cancel
          </button>
          <button type="submit" disabled={!showConnectForm}>
            Connect
          </button>
        </div>
      </form>
    </div>
  );
}
