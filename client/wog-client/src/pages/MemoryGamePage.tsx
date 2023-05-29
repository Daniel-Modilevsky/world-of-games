import React, { useEffect, useState } from "react";
import "./Page.scss";
import { MemoryGameType } from "../types/gameType";
import { INITIAL_MEMORY_GAME } from "../utils/constans";
import { getMemoryGame } from "../api/api";
import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";
import { useNavigate } from "react-router-dom";

type MemoryGamePageProps = {
  difficult: number;
};

export const MemoryGamePage: React.FC<MemoryGamePageProps> = ({
  difficult,
}: MemoryGamePageProps) => {
  const [memoryGame, setMemoryGame] =
    useState<MemoryGameType>(INITIAL_MEMORY_GAME);
  const [isUserSuggested, setIsUserSuggested] = useState<boolean>(false);
  const [isWin, setIsWin] = useState<boolean>(false);
  const [numbers, setNumbers] = useState<number[]>([]);
  const [inputValue, setInputValue] = useState("");
  const [timeoutId, setTimeoutId] = useState<NodeJS.Timeout | null>(null);
  const [isTimeOn, setTimeOn] = useState<boolean>(false);

  const navigate = useNavigate();

  useEffect(() => {
    getMemoryGame(difficult, setMemoryGame);
  }, []);

  //Using timeout + clear the timeout
  const showSequence = () => {
    setTimeOn(true);

    // Clear any previous timeouts
    if (timeoutId) {
      clearTimeout(timeoutId);
    }

    // Set the new timeout
    const newTimeoutId = setTimeout(() => {
      setTimeOn(false);
    }, 2000);

    setTimeoutId(newTimeoutId);
  };

  const handleInputChange = (event: any) => {
    setInputValue(event.target.value);
  };

  const isUserCurrect = () => {
    let i = 0;
    for (i = 0; i < difficult; i++) {
      if (numbers[i] !== memoryGame.numbersToGuess[i]) {
        return false;
      }
    }
    return true;
  };

  const handleUserSubmit = () => {
    setIsUserSuggested(true);
    setIsWin(isUserCurrect());
  };

  const playAgain = () => {
    setIsWin(false);
    setIsUserSuggested(false);
    getMemoryGame(difficult, setMemoryGame);
  };

  const addNumber = () => {
    if (inputValue !== "") {
      setNumbers([...numbers, Number(inputValue)]);
      setInputValue("");
    }
  };

  return (
    <div className="container">
      <h1> Welcome to Memory Game! </h1>
      <p>
        {" "}
        There will be {difficult} numbers in the sequence from 1 to 100 for 2
        seconds:
        <Button variant="outlined" onClick={showSequence}>
          Show sequence
        </Button>{" "}
      </p>
      <div className={`secondry ${isTimeOn ? "vissavle" : "hidden"}`}>
        The sequence is:{" "}
        {memoryGame.numbersToGuess.map((sequenceNumber) => {
          return <span>{sequenceNumber} </span>;
        })}
      </div>
      <div className="slider-container">
        <TextField
          label="User guess"
          type="number"
          size="small"
          value={inputValue}
          onChange={handleInputChange}
        />
        <Button variant="outlined" onClick={addNumber}>
          Next Value
        </Button>
        <Button
          variant="outlined"
          onClick={() => {
            setNumbers([]);
          }}
        >
          Clear
        </Button>
        <Button variant="contained" onClick={handleUserSubmit}>
          Submit
        </Button>
      </div>
      <div>
        <b>Your sequence is: </b>
        {numbers.map((userChoice) => {
          return <span>{userChoice} </span>;
        })}
      </div>
      <div className={isUserSuggested ? "vissable" : "hidden"}>
        <p>
          The sequence was:{" "}
          {memoryGame.numbersToGuess.map((sequenceNumber) => {
            return <span>{sequenceNumber} </span>;
          })}
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
