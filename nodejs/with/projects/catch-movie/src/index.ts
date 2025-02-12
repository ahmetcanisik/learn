#!/usr/bin/env node
import * as cheerio from "cheerio";
import open from "open";
import { Command } from "commander";
import { ReadFile } from "filen";
import { title, input } from "extra-methods";
import Logil from "logil";

/**
 * Find HDFilmCehennemi Embed video url
 * @param url HDFilmCehennemi Video Link
 * @returns HDFilmCehennemi Embed Video Link
 */
async function findEmbedURL(url: string): Promise<string> {
  const res = await fetch(url);
  if (res.status === 200) {
    const $ = cheerio.load(await res.text());
    if ($("iframe")) {
      const foundedEmbed = $("iframe").attr("data-src");
      if (typeof foundedEmbed === "string") return foundedEmbed;
    }
    throw new Error("Not found iframe tag");
  }

  throw new Error(`Status: ${res.status}`);
}

async function main() {
  const { name, description, version } = await ReadFile(
    [__dirname, "..", "package.json"],
    { parseToJson: true }
  );

  const appName = title(name.replaceAll("-", " "));

  const logger = new Logil({
    icon: appName,
    prefix: "->"
  });

  const catchMovie = new Command();

  catchMovie
    .name(appName)
    .description(description)
    .version(version, "-v, --version", "Output the current version")
    .arguments("[command]")
    .argument("[hdfilmchennemiVideoURL]", "HDFilmCehennemi Video URL")
    .helpOption("-h, --help", "Display help for command")
    .action(async (videoURL) => {
      if (videoURL && typeof videoURL === "string") {
        open(await findEmbedURL(videoURL));
        return;
      }

      const putTheURL = await input("Enter your HDFilmCehennemi url: ");
      if (putTheURL && typeof putTheURL === "string") {
        await open(await findEmbedURL(putTheURL));
        logger.success(`Successfully opened the url: ${putTheURL}`);
        return;
      }
    });

  catchMovie.parse();
}

if (require.main === module) (async () => await main())();
