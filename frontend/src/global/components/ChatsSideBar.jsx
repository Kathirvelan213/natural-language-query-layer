import { useEffect, useState } from "react";
import { getChatList } from "../../apiConsumer/chatsAPI";
import "../styles/sidebar.css";
import { ChatNavItem } from "./ChatNavItem";
import { ChatSideBarHeading } from "./ChatSideBarHeading";

export function ChatSideBar({ conversations, selectedConv, onSelectConv, onNewConv }) {
  const [chatList, setChatList] = useState([]);
  useEffect(() => {
    setChatList(getChatList());
  }, []);

  
  return (
    <aside className="sidebar">
      <div className="logo-container">
        <img src="src/assets/logo2.png" className="logo" />
        <div className="logo-text">Shard</div>
      </div>
      <hr className="w-[95%] justify-self-center border-white/5" />
      <div className="h-[300px]"></div>
      <ChatSideBarHeading heading={"Queries"} />
      <nav className="min-h-0 flex flex-col flex-1">
        <div className="chats-list">
          {chatList.map((chat) => (
            <ChatNavItem conversationTitle={chat} key={chat[0]}/>
          ))}
        </div>
      </nav>
      <hr className="w-[95%] justify-self-center border-white/5 self-end" />
      <div className="h-[60px]"></div>
    </aside>
  );
}
