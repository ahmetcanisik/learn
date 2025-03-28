#!/usr/bin/env zx
import { fs, fetch } from 'zx';

try {
    const proxyListURL = "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/refs/heads/master/http.txt";
    const proxyListURLRes = await fetch(proxyListURL);

    if (!proxyListURLRes.ok) {
        console.error(`status = ${proxyListURLRes.status}\n${proxyListURL}\n`);
        throw new Error(`status = ${proxyListURLRes.status}\n${proxyListURL}\n`);
    }

    const proxiesText = await proxyListURLRes.text();
    const proxies = proxiesText.split("\n");

    await fs.writeFile("test.json", JSON.stringify({
        proxies: proxies
    }, null, 2), "utf-8");

} catch (err) {
    console.error(`Gettting a proxy url's process done with errors!\n${err}`);
}