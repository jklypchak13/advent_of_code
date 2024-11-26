import { argv } from 'process';

import {readFileSync} from "fs";
import {Result} from "../shared/types.js"

const INPUT_DATA = "day4/input.txt";
const SAMPLE_DATA = "day4/sample.txt";

export function day4(){
    let res: Result = {p1: "", p2: ""};
    const input = readFileSync(INPUT_DATA, {encoding: "utf-8"});
    res.p1 = "0";
    res.p2 = "0";
    return res;
}

if (import.meta.filename === argv[1]) {
    const result = day4();
    console.log(`Day 4 Part 1: ${result.p1}`);
    console.log(`Day 4 Part 2: ${result.p2}`);
} 
