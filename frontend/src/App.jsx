import { useState } from "react";
import "./App.css";
import { QueryPage } from "./pages/queryPage/QueryPage";
import { Route, Routes } from "react-router-dom";
import { Layout } from "./global/Layout";
import { NewQueryPage } from "./pages/newQueryPage/newQueryPage";

function App() {
  return (
    <div>
      <Routes>
        <Route element={<Layout />}>
          <Route path="/" element={<NewQueryPage />} />
          <Route path="/chat/:id" element={<QueryPage />} />
        </Route>
      </Routes>
    </div>
  );
}

export default App;
