import "../styles/sideBar.css";
import {Link} from "react-router-dom"

export function ChatNavItem({ chat, isSelected, onClick }) {
  return (
    <Link to={`/chat/${chat[0]}`}
      className={`chat-nav-item ${isSelected ? "selected" : ""}`}    
    >
      {chat[1] || "Untitled Chat"}
    </Link>
  );
}