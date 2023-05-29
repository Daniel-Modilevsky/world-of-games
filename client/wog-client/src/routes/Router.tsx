import React, { useState } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { HomePage } from "../pages/HomePage";
import { GuessGamePage } from "../pages/GuessGamePage";
import { MemoryGamePage } from "../pages/MemoryGamePage";
import { CurrencyGamePage } from "../pages/CurrenctGamePage";
import Header from "../components/layout/Header";
import { INITIAL_DIFFICULTY } from "../utils/constans";

type RouterProps = {};

export const Router: React.FC<RouterProps> = () => {
  const [difficult, setDifficult] = useState<number>(INITIAL_DIFFICULTY);

  return (
    <BrowserRouter>
      <Header/>
        <Routes>
          <Route path="/" element={<HomePage difficult={difficult} setDifficult={setDifficult} />} />
          <Route path="/games/guess" element={<GuessGamePage difficult={difficult} />} />
          <Route path="/games/memory" element={<MemoryGamePage difficult={difficult} />} />
          <Route path="/games/currency" element={<CurrencyGamePage difficult={difficult} />} />
        </Routes>
    </BrowserRouter>
  );
};