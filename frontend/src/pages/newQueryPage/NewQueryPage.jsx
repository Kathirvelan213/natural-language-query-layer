import "./styles/newQueryPage.css";
import { PromptField } from "../../global/components/PromptField";
import { createChat } from "../../apiConsumer/chatsAPI";
import { useNavigate } from "react-router-dom";
import { performQueryAPI } from "../../apiConsumer/queryAPI";
import { useOutletContext } from "react-router-dom";

export function NewQueryPage() {
  const navigate = useNavigate();
  const { setChatList } = useOutletContext();

  async function handleNewQuery(prompt) {
    const newChatIdResponse = await createChat("Untitled Chat");
    const newChatId = newChatIdResponse.data.chat_id;
    setChatList((chatList) => [...chatList, newChatIdResponse.data]);
    console.log(newChatId);
    const response = await performQueryAPI({ chatId: newChatId, prompt: prompt });
    navigate(`/chat/${newChatId}`);
  }

  return (
    <div className="newQueryPage">
      <div className="logo-container-large">
        <div className="logo-text-large">Shard</div>
        <div className="subtitle">Natural Language Query Layer</div>
      </div>
      <div className="content-center">
        <PromptField onSubmit={handleNewQuery} />
      </div>
    </div>
  );
}
