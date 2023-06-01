import React, { useState } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { HomePage } from "../pages/HomePage";
import { GuessGamePage } from "../pages/GuessGamePage";
import { MemoryGamePage } from "../pages/MemoryGamePage";
import { CurrencyGamePage } from "../pages/CurrenctGamePage";
import Header from "../components/layout/Header";
import { INITIAL_DIFFICULTY, INITIAL_SCORE } from "../utils/constans";
import { updateScore } from "../api/api";

type RouterProps = {};

export const Router: React.FC<RouterProps> = () => {
  const [difficult, setDifficult] = useState<number>(INITIAL_DIFFICULTY);
  const [score, setScore] = useState<number>(INITIAL_SCORE);

  const updateCounter = () => {
    updateScore((difficult * 3 + 5 + score), setScore)
  }


  return (
    <BrowserRouter>
      <Header/>
        <Routes>
          <Route path="/" element={<HomePage score={score} setScore={updateCounter} difficult={difficult} setDifficult={setDifficult} />} />
          <Route path="/games/guess" element={<GuessGamePage difficult={difficult} setScore={updateCounter}/>} />
          <Route path="/games/memory" element={<MemoryGamePage difficult={difficult} setScore={updateCounter} />} />
          <Route path="/games/currency" element={<CurrencyGamePage difficult={difficult} setScore={updateCounter}/>} />
        </Routes>
    </BrowserRouter>
  );
};