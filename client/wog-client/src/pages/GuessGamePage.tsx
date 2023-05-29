import React, { useEffect, useState } from "react";
import "./Page.scss";
import { INITIAL_GUESS_GAME } from "../utils/constans";
import { GuessGameType } from "../types/gameType";
import { getGuessGame } from "../api/api";
import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";
import { useNavigate } from "react-router-dom";

type GuessGamePageProps = {
  difficult: number;
};

export const GuessGamePage: React.FC<GuessGamePageProps> = ({
  difficult,
}: GuessGamePageProps) => {
  const [guessGame, setGuessGame] = useState<GuessGameType>(INITIAL_GUESS_GAME);
  const [isUserSuggested, setIsUserSuggested] = useState<boolean>(false);
  const [isWin, setIsWin] = useState<boolean>(false);
  const [userGuess, setUserGuess] = useState<number>(0)

  const navigate = useNavigate();

  useEffect(() => {
    getGuessGame(difficult, setGuessGame);
  }, []);

  const isUserCurrect = () => {
    return guessGame.secretNumber === userGuess
  }

  const handleUserSubmit = () => {
    setIsUserSuggested(true)
    setIsWin(isUserCurrect())
  }

  const playAgain = () => {
    setIsWin(false);
    setIsUserSuggested(false);
    getGuessGame(difficult, setGuessGame);
  }


  return (
    <div className="container">
      <h1> Welcome to Guess the Number Game! </h1>
      <p> Guess a number between 1 to {difficult}: </p>
      <div className="slider-container">
        <TextField label="User guess" type="number" size="small" value={userGuess} onChange={(e)=>{setUserGuess(parseInt(e.target.value))}}/>
        <Button variant="contained" onClick={handleUserSubmit}>
          Submit
        </Button>
      </div>
      <div className={isUserSuggested? "vissable" : "hidden"}>
        <p> The secret number is {guessGame.secretNumber} and the guess number is {userGuess} </p>
        {isWin?  <p> Congratulations, you win! </p> :  <p> Nice try but you lose this time, good luck next time! </p> }
         <Button variant="text" onClick={playAgain}>
          Play again
        </Button> 
        <Button variant="text" onClick={()=>navigate('/')}>
          Back to all games
        </Button> 
      </div>
    </div>
  );
};
