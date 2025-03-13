/**
 * @description User country code is matched any country code when reload page with user country code.
 * @param {inspect: boolean} options
 */
async function findUserCountry(options = { inspect: false }) {
    try {
        // get ip address request
        const ipInfoRes = await fetch("https://ipinfo.io/json");

        // if ipInfoRes response is valid...
        if (ipInfoRes.status === 200) {

            // help me for this code analyze...
            if (options.inspect) console.log("ip info response status code is ", ipInfoRes.status);

            // get response body
            const ipInfo = await ipInfoRes.json()

            // if ip info is right...
            if (ipInfo) {

                // help me for this code analyze...
                if (options.inspect) console.log("ip informations;\n", JSON.stringify(ipInfo, null, 2));

                // get countryCode code
                const countryCode = ipInfo.country.toLowerCase();

                // if countryCode code is right...
                if (countryCode) {
                    try {

                        // help me for this code analyze...
                        if (options.inspect) console.log("Your country code is ", countryCode);

                        // get all countries database from github
                        const getAllCountriesRes = await fetch("https://raw.githubusercontent.com/dr5hn/countries-states-cities-database/refs/heads/master/json/countries.json");

                        // if get all countries response is right...
                        if (getAllCountriesRes.status === 200) {

                            // help me for this code analyze...
                            if (options.inspect) console.log("get all countries response status code is ", getAllCountriesRes.status);

                            // get all countries with json format.
                            const countries = await getAllCountriesRes.json();

                            // if all countries is right...
                            if (countries) {

                                // help me for this code analyze...
                                if (options.inspect) console.log("all countries datas are find!", JSON.stringify(countries[0], null ,2), "\n...");

                                // then loop in countries for the getting countryCode
                                let userCountryCode = countries.find((country) => countryCode === country.iso2.toLowerCase());

                                if (userCountryCode) {
                                    // help me for this code analyze...
                                    if (options.inspect) console.log(`matched! your country code is valid!`, userCountryCode);

                                    return countryCode;
                                }

                                throw new Error(`user country code(${countryCode}) is not matched any countries!`);
                            }

                            // if countries is not found!
                            else {
                                throw new Error("Countries is not found on countries database!");
                            }
                        }
                        // get all countries response is not valid!
                        else {
                            throw new Error("Failed to fetching all countries database! here is status code = ", getAllCountriesRes.status);
                        }
                    } catch (error) {

                        // if github response is not valid!
                        throw new Error("Failed to fetch countries database!", error);
                    }
                }
                // country code is not found!
                else {
                    throw new Error("country code is not found!");
                }
            }
            // else ip info is not right!
            else {
                throw new Error("ip informations is not found! please reload this page and check your connection!");
            }
        }
        // if ipInfoRes response status is not valid
        else {
            throw new Error("ipInfoRes fetch failed! here is the status code = ", ipInfoRes.status);
        }
    } catch (err) {

        // if ip response is not valid.
        throw new Error("Failed to finding your country code! ", err)
    }
}

if (typeof module === "object") {
    module.exports = findUserCountry;
}

if (typeof window !== "undefined") {
    window.findUserCountry = findUserCountry;
}