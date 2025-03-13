import findUserCountry from "find-user-country";

document.addEventListener("DOMContentLoaded", async () => {
    const api = document.getElementById("api");

    api.innerHTML = await findUserCountry();
})