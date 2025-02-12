#!/usr/bin/env node
import lectures0 from "./lectures-0";
import { Command } from "commander";
import { ReadFile } from "filen";
import { title } from "extra-methods";

async function main() {
  const lectures = new Command();
  const { name, version, description } = await ReadFile(
    [__dirname, "..", "package.json"],
    { parseToJson: true }
  );

  lectures
    .name(title(name.replaceAll("-", " ")))
    .usage("[command]")
    .description(description)
    .version(version, "-v, --version", "Output the current version")
    .helpOption("-h, --help", "Display help for command")
    .argument("[lectureNumber]", "lecture number, ex: 0")
    .action(async (lectureNumber) => {
        if (typeof Number(lectureNumber) === "number") {
            const ln: number = Number(lectureNumber);
            if (ln === 0) await lectures0();
        }
    })

    lectures.parse();
}

if (require.main === module) (async () => await main())();
