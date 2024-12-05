import * as path from "https://deno.land/std/path/mod.ts";
import { useReadFile } from "../readFile.ts";

async function part1() {
  const { read } = useReadFile(path.join(Deno.cwd(), "input.txt"));
  const lines = await read();
  let sum = 0;
  for (let l = 0; l < lines.length; l++) {
    const line = lines[l];
    const matches = line.match(/[0-9]/g);
    const number = parseInt(`${matches[0]}${matches[matches.length - 1]}`, 10);
    sum = sum + number;
  }
  return sum;
}

async function part2() {
  let sum = 0;
  const digits = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
  ];
  const { read } = useReadFile(path.join(Deno.cwd(), "input.txt"));
  const lines = await read();
  for (let l = 0; l < lines.length; l++) {
    const line = lines[l];
    const matchesForward = line
      .match(/[0-9]|one|two|three|four|five|six|seven|eight|nine/gi)
      ?.map((digit) => {
        if (digits.indexOf(digit) >= 0) return digits.indexOf(digit) + 1;
        return parseInt(digit, 10);
      });
    const matchesBackword = line
      .split("")
      .reverse()
      .join("")
      .match(/[0-9]|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin/gi)
      ?.map((digit) => {
        if (digits.indexOf(digit) >= 0) return digits.indexOf(digit) + 1;
        return parseInt(digit, 10);
      });
    const number = parseInt(`${matchesForward[0]}${matchesBackword[0]}`, 10);

    sum = sum + number;
  }
  return sum;
}

console.log(`Part 1: ${await part1()}`);
console.log(`Part 2: ${await part2()}`);
