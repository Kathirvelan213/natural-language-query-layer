import { useEffect, useState } from "react";
import { getAllChats } from "../../apiConsumer/chatsAPI";
import "../styles/sideBar.css";
import { ChatNavItem } from "./ChatNavItem";
import { ChatSideBarHeading } from "./ChatSideBarHeading";
import { Link } from "react-router-dom";
import { FaChevronDown } from "react-icons/fa";
import { FaPenToSquare  } from "react-icons/fa6";

import logoSrc from "../../assets/logo2.png";
import { LoginButton } from "./LoginButton";

export function ChatSideBar({ chatList, setChatList }) {
  return (
    <aside className="sidebar">
      <div className="logo-container">
        <img src={logoSrc} className="logo" />
        <div className="logo-text">Shard</div>
      </div>
      <hr className="w-[95%] justify-self-center border-white/5" />
      <div className="h-[300px]"></div>
      <Link to="/" className="new-chat">
        <div className="flex items-center">
          <FaPenToSquare className="-rotate-90 text-right mr-[7px] scale-y-[-1] h-[15px] w-[15px]" />
          New chat
        </div>
        <FaChevronDown className="-rotate-90 text-right mr-[7px]" />
      </Link>
      <ChatSideBarHeading heading={"Queries"} />
      <nav className="min-h-0 flex flex-col flex-1">
        <div className="chats-list">
          {chatList.map((chat) => (
            <ChatNavItem chat={chat} key={chat.chat_id} />
          ))}
        </div>
      </nav>
      <hr className="w-[95%] justify-self-center border-white/5 self-end" />
      {/* <div className="h-[60px]"></div> */}
      <div className="query-header">
        <LoginButton />
      </div>
    </aside>
  );
}
