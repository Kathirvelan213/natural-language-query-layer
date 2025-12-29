import "../styles/sidebar.css";

export function ChatNavItem({ conversationTitle, isSelected, onClick }) {
  return (
    <a
      className={`chat-nav-item ${isSelected ? "selected" : ""}`}    
      onClick={onClick}
    >
      {conversationTitle || "Untitled Chat"}
    </a>
  );
}