import { useEffect, useState } from "react";
import { getChatList } from "../../apiConsumer/chatsAPI";
import "../styles/sidebar.css";
import { ChatNavItem } from "./ChatNavItem";
import { ChatSideBarHeading } from "./ChatSideBarHeading";
import {Link} from "react-router-dom"
import { FaArrowRight } from "react-icons/fa";
import logoSrc from "../../assets/logo2.png"

export function ChatSideBar({ conversations, selectedConv, onSelectConv, onNewConv }) {
  const [chatList, setChatList] = useState([]);
  useEffect(() => {
    setChatList(getChatList());
  }, []);
  return (
    <aside className="sidebar">
      <div className="logo-container">
        <img src={logoSrc} className="logo" />
        <div className="logo-text">Shard</div>
      </div>
      <hr className="w-[95%] justify-self-center border-white/5" />
      <div className="h-[300px]"></div>
      <Link to="/"className={`chat-nav-item `}>
        {"New Chat"}
        <FaArrowRight/>
      </Link>
      <ChatSideBarHeading heading={"Queries"} />
      <nav className="min-h-0 flex flex-col flex-1">
        <div className="chats-list">
          {chatList.map((chat) => (
            <ChatNavItem chat={chat} key={chat[0]} />
          ))}
        </div>
      </nav>
      <hr className="w-[95%] justify-self-center border-white/5 self-end" />
      <div className="h-[60px]"></div>
    </aside>
  );
}
