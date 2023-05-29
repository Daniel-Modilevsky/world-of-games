import React, { useEffect, useState } from "react";
import Button from '@mui/material/Button';
import Stack from '@mui/material/Stack';
import CurrencyExchangeIcon from '@mui/icons-material/CurrencyExchange';
import AccessTimeIcon from '@mui/icons-material/AccessTime';
import PsychologyAltIcon from '@mui/icons-material/PsychologyAlt';
import "./Page.scss";
import { useNavigate } from "react-router-dom";
import { GAMES } from "../utils/constans";
import { getScore } from "../api/api";
import Slider from '@mui/material/Slider';

type HomePageProps = {
  difficult: number,
  setDifficult: Function,
  score: number,
  setScore: Function,
};


export const HomePage: React.FC<HomePageProps> = ({difficult, setDifficult, score, setScore }: HomePageProps) => {
  const navigate = useNavigate();

  useEffect(()=>{
    getScore(setScore);
  },[])

  const handleChange = (event: Event, newValue: number | number[]) => {
    setDifficult(newValue as number);
  };

  return (
    <div className="container">
        <h1> Hello there and welcome to the <span className="primary">World Of Games</span>!</h1>
        <h2> This is our games: </h2>
        <p> 1. <b className="secondry">Memory Game</b> - a sequence of numbers will appear for 1 second and you have guess it back </p>
        <p> 2. <b className="secondry">Guess Game</b> - guess a number and see if you chose like the computer </p>
        <p> 3. <b className="secondry">Currency Game</b> - try and guess the value of a random amount of USD in ILS </p>
        <p>For playing please select the games difficulty from 1-10 when the deffault is 3:</p>
        <div className="slider-container">
          <Slider
            className="slider"
            defaultValue={difficult}
            valueLabelDisplay="on"
            step={1}
            marks
            min={1}
            max={10}
            onChange={handleChange}
          />
        </div>
        <Stack direction="row" spacing={2} className="center" alignItems={"center"}>
      <Button variant="outlined" endIcon={<PsychologyAltIcon />} onClick={()=>navigate(GAMES[0].url)}>
        {GAMES[0].name}
      </Button>
      <Button variant="outlined" endIcon={<AccessTimeIcon />} onClick={()=>navigate(GAMES[1].url)}>
        {GAMES[1].name}
      </Button>
      <Button variant="outlined" endIcon={<CurrencyExchangeIcon />} onClick={()=>navigate(GAMES[2].url)}>
       {GAMES[2].name}
      </Button>
    </Stack>
      <h2> Current world game score is:  <span className="primary">{score} </span></h2>
    </div>
  );
};
