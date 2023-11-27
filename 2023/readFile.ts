export function useReadFile(filePath: string) {
  let fullContent: string | undefined;

  const read = async (): Promise<string[]> => {
    const decoder = new TextDecoder("utf-8");
    const data = await Deno.readFile(filePath);
    return decoder
      .decode(data)
      .split(/\r?\n/)
      .filter((line: string) => line.trim() !== "");
  };

  return { fullContent, read };
}
