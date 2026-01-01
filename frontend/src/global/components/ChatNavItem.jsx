import "../styles/sideBar.css";
import {Link} from "react-router-dom"

export function ChatNavItem({ chat, isSelected }) {
  return (
    <Link to={`/chat/${chat.chat_id}`}
      className={`chat-nav-item ${isSelected ? "selected" : ""}`}    
    >
      {chat.chat_name || "Untitled Chat"}
    </Link>
  );
}