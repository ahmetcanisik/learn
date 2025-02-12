import { input, title } from 'extra-methods';

export default async function lectures0() {
    console.log("What's your name? ");
    const name = (await input("My name is "));
    console.log(`Hello, ${title(name)}`);
}