/**
 * @description main function for this program.
 */
async function main() {
    try {
        const countryCode = await findUserCountry();

        if (countryCode) {
            document.location.href = `/${countryCode}`;
        } else {
            console.error("country code is not valid = ", countryCode);
        }
    } catch (err) {
        throw new Error("Your country code is not found!", err);
    }
}


// start my code when document content loaded.
document.addEventListener("DOMContentLoaded", async () => {
    await main();
});