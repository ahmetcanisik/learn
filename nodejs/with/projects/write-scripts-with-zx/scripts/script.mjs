#!/usr/bin/env zx
import { $, fetch, cd, ps, chalk, minimist } from 'zx';
import { title } from "extra-methods";

/*
// console.log(await $`ls -la`.then(out => out.stdout));
// console.log(await $`python3 --version`.then(py => py.toString()));

// console.log($.sync`pwd`.toString())

// await retry(3, '1s', () => echo("echoco"))

async function findCommand(command){
    if (command && typeof command === "string") {
        if (await ps.lookup({ command: command })) {
            return true;
        }
    }

    return false;
}

const args = minimist(process.argv.slice(2), {
    alias: {
        "h": "help",
        "v": "version"
    }
});

function shortLongFlag(flag, callback) {
    if (flag) {
        if (typeof flag === "string") {
            flag.replaceAll("-", "");
            if (args[flag] || args[flag[0]]) callback(args[flag]);
        }

        if (typeof flag === "object") {
            flag.forEach(f => {
                f.replaceAll("-", "");
                if (args[f]) callback(args[f]);
            });
        }
    }
}

shortLongFlag("lang",  async (flag) => {
    try {
        if (await findCommand(flag)) {
            console.log(`${title(flag)} version found: `, chalk.green(await $`${flag} --version`))
        }
    } catch (e) { console.log(e) }
});

if (await findCommand('node')) console.log(chalk.greenBright("Node found!"));

console.log(chalk.green(await $`pwd`.then(currentDir => currentDir.toString())));
await $`mkdir -p test`

cd("test")
console.log(chalk.green(await $`pwd`.then(currentDir => currentDir.toString())));

for (let i = 0; i < 5; i++) {
    await $`mkdir -p test${i+1}`;
}*/

const obj = await fetch("https://api.ahmetcanisik.com/skills?name=html5");
console.log(await obj.json());