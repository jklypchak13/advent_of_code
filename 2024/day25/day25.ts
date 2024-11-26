import { argv } from 'process';

import {readFileSync} from "fs";
import {Result} from "../shared/types.js"

const INPUT_DATA = "day25/input.txt";
export function day25(){
    let res: Result = {p1: "", p2: ""};
    const input = readFileSync(INPUT_DATA, {encoding: "utf-8"});
    res.p1 = "0";
    res.p2 = "0";
    return res;
}

if (import.meta.url === argv[1]) {
    const result = day25();
    console.log(`Day 25 Part 1: ${result.p1}`);
    console.log(`Day 25 Part 2: ${result.p2}`);
} 
