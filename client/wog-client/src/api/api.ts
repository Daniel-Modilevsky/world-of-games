import axios from "axios";
import { INITIAL_CURRENCY_GAME, INITIAL_GUESS_GAME, INITIAL_MEMORY_GAME, INITIAL_SCORE } from "../utils/constans";
const BASE_URL = "http://localhost:8000";

// Score API ----------------------------------------------------------------
export const getScore = async (
    setScore: Function
) => {
  try{
    const { data } = await axios.get(`${BASE_URL}/score`);
    setScore(data);
  } catch (err) {
    setScore(INITIAL_SCORE);
  }
};


export const updateScore = async (
  newScore: number,
  setScore: Function
) => {
  try{
    const { data } = await axios.put(`${BASE_URL}/score`, { score: newScore });
    setScore(data);
  } catch (err) {
    setScore(newScore);
  }
};

// Guess Game API ----------------------------------------------------------------
export const getGuessGame = async (difficult: number, setGuessGame: Function) => {
    try{
      const { data } = await axios.get(`${BASE_URL}/guess?${difficult}`);
      setGuessGame(data);
    } catch (err) {
      setGuessGame(INITIAL_GUESS_GAME);
    }
}


// Memory Game API ----------------------------------------------------------------
export const getMemoryGame = async (difficult: number, setMemoryGame: Function) => {
    try{
      const { data } = await axios.get(`${BASE_URL}/memory?${difficult}`);
      setMemoryGame(data);
    } catch (err) {
      setMemoryGame(INITIAL_MEMORY_GAME);
    }
}


// Currency Game API ----------------------------------------------------------------
export const getCurrencyGame = async (difficult: number, setCurrencyGame: Function) => {
    try{
      const { data } = await axios.get(`${BASE_URL}/currency?${difficult}`);
      setCurrencyGame(data);
    } catch (err) {
      setCurrencyGame(INITIAL_CURRENCY_GAME);
    }
}