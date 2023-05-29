import React, { useEffect, useState } from "react";
import "./Page.scss";
import { INITIAL_CURRENCY_GAME, INITIAL_GUESS_GAME } from "../utils/constans";
import { CurrencyGameType, GuessGameType } from "../types/gameType";
import { getCurrencyGame } from "../api/api";
import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";
import { useNavigate } from "react-router-dom";

type CurrencyGamePageProps = {
  difficult: number;
};

export const CurrencyGamePage: React.FC<CurrencyGamePageProps> = ({
  difficult,
}: CurrencyGamePageProps) => {
  const [currencyGame, setCurrencyGame] = useState<CurrencyGameType>(
    INITIAL_CURRENCY_GAME
  );
  const [isUserSuggested, setIsUserSuggested] = useState<boolean>(false);
  const [isWin, setIsWin] = useState<boolean>(false);
  const [userGuess, setUserGuess] = useState<number>(0);

  const navigate = useNavigate();

  useEffect(() => {
    getCurrencyGame(difficult, setCurrencyGame);
  }, []);

  const isUserCurrect = () => {
    return currencyGame.dolarValue === userGuess;
  };

  const handleUserSubmit = () => {
    setIsUserSuggested(true);
    setIsWin(isUserCurrect());
  };

  const playAgain = () => {
    setIsWin(false);
    setIsUserSuggested(false);
    getCurrencyGame(difficult, setCurrencyGame);
  };

  return (
    <div className="container">
      <h1> Welcome to Currency Game! </h1>
      <p> The total USD$ value in ILS is: {currencyGame.shekelValue} </p>
      <div className="slider-container">
        <span>Enter your guess for the value in USD:</span>
        <TextField
          label="User guess"
          type="number"
          size="small"
          value={userGuess}
          onChange={(e) => {
            setUserGuess(parseInt(e.target.value));
          }}
        />
        <Button variant="contained" onClick={handleUserSubmit}>
          Submit
        </Button>
      </div>
      <div className={isUserSuggested ? "vissable" : "hidden"}>
        <p>
          Your guess is: {userGuess} and the real amount in ILS is:{" "}
          {currencyGame.dolarValue}
        </p>
        {isWin ? (
          <p> Congratulations, you win! </p>
        ) : (
          <p> Nice try but you lose this time, good luck next time! </p>
        )}
        <Button variant="text" onClick={playAgain}>
          Play again
        </Button>
        <Button variant="text" onClick={() => navigate("/")}>
          Back to all games
        </Button>
      </div>
    </div>
  );
};
