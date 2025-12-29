import { useState } from 'react';
import "./styles/queryPage.css";
import { ChatSideBar } from '../../global/components/ChatsSideBar';



export function QueryPage() {
  return (
    <div className='main-container'>
      <ChatSideBar/>
    </div>
  );
}
