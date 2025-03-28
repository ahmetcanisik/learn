#!/usr/bin/env zx
import { fs } from "zx";

const text = await fs.readFile("./test.txt", "utf-8");

const splitText = text.split("\n");

console.log(splitText);