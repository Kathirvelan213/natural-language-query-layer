import { useEffect, useState } from "react";
import { ChatSideBar } from "./components/ChatsSideBar";
import { Outlet } from "react-router-dom";
import { getAllChats } from "../apiConsumer/chatsAPI";

export function Layout() {
  const [chatList, setChatList] = useState([]);
  useEffect(() => {
    const fetchChats = async () => {
      const chats = await getAllChats();
      setChatList(chats.data);
    };

    fetchChats();
  }, []);
  return (
    <div className="flex w-screen h-screen">
      <ChatSideBar chatList={chatList} setChatList={setChatList} />
      <main className="flex flex-col items-center justify-center flex-1">
        <Outlet context={{setChatList}}/>
      </main>
    </div>
  );
}
