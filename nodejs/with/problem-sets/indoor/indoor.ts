import input from '@inquirer/input';

async function main()
{
    const indoor = await input({ message: "" });

    console.log(indoor.trim().toLowerCase());
}

(async () => {
    await main();
})();