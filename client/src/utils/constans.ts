import { GameType, GuessGameType, MemoryGameType, CurrencyGameType } from "../types/gameType";

export const INITIAL_DIFFICULTY = 3;

export const GAMES:GameType[] = [
    {
        name: 'Guess Game',
        url: '/games/guess'
    },
    {
        name: 'Memory Game',
        url: '/games/memory'
    },
    {
        name: 'Currency Game',
        url: '/games/currency'
    },
];


export const INITIAL_SCORE = 25;

export const INITIAL_GUESS_GAME: GuessGameType = {
    secretNumber: 4,
};

export const INITIAL_MEMORY_GAME: MemoryGameType = {
    numbersToGuess: [1, 2, 3],
};

export const INITIAL_CURRENCY_GAME: CurrencyGameType = {
    dolarValue: 84,
    shekelValue: 26.4,
};


