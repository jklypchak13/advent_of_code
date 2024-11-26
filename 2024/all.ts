import {day_functions} from "./days.js"

for(let i=1;i<=25;i++){
	const fun = day_functions[i-1];
	const result = fun();
	console.log("---------------------------");
	console.log(`Day ${i} Part 1:${result.p1}`);
	console.log(`Day ${i} Part 2:${result.p2}`);
	console.log("---------------------------");
}


