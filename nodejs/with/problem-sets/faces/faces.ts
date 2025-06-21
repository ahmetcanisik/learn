import input from '@inquirer/input';

async function main()
{
    const faces = await input({ message: "" });
    
    faces.trim().replaceAll(":)", "🙂").replaceAll(":(", "🙁");
    
    console.log(faces);
}

(async () => {
    await main();
})();