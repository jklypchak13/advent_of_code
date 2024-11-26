import {readFileSync} from "fs";
import {Result} from "../shared/types.js"

const INPUT_DATA = "day16/input.txt";
export function day16(){
    let res: Result = {p1: "", p2: ""};
    const input = readFileSync(INPUT_DATA, {encoding: "utf-8"});
    res.p1 = "0";
    res.p2 = "0";
    return res;
}

day16();
