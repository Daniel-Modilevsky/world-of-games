export type GameType = {
    name: string;
    url: string;
}

export type GuessGameType = {
    // difficultyAsRange: number; // Number of range
    secretNumber: number;
};

export type MemoryGameType = {
    // difficultyAsOptionsNumber: number; // Number of options to guess
    numbersToGuess: number[]; 
}

export type CurrencyGameType = {
    // difficultyAsRangeOfMistake: number; // Number of range
    dolarValue: number;
    shekelValue: number; 
}
