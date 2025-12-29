import { ChatSideBar } from "./components/ChatsSideBar";
import {Outlet} from "react-router-dom";

export function Layout(){
    return(
        <div className="flex w-screen h-screen">
            <ChatSideBar/>
            <main className="flex flex-col items-center justify-center flex-1">
                <Outlet/>
            </main>
        </div>
    )
}