import input from '@inquirer/input';

async function main()
{
    const playback = await input({ message: "" });

    console.log(playback.trim().replaceAll(" ", "..."));
}

(async () => {
    await main();
})();