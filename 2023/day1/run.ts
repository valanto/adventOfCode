import * as path from "https://deno.land/std/path/mod.ts";
import { useReadFile } from "../readFile.ts";

async function run() {
  const { fullContent, read } = useReadFile(path.join(Deno.cwd(), "foo.txt"));
  console.log(await read());
}

run();
