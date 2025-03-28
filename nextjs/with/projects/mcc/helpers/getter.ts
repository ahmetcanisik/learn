import { URLAnalyzer, type URLAnalyzerReturn } from './analyzer';
import { isValidURL } from './validate';
import * as cheerio from 'cheerio';
import fetch from 'node-fetch';

export type siteCategories = 'trendyol' | 'hepsiburada' | 'daraaksesuar';
export interface GetMoneyReturn {
    error?: string;
    target?: {
        url: string;
        money: string;
    };
}

export async function getMoney(websiteUrl: string, category: siteCategories): Promise<GetMoneyReturn> {
    if (!websiteUrl) {
        return {
            error: "please specify the url!"
        };
    }

    if (!isValidURL(websiteUrl)) {
        return {
            error: `${websiteUrl} isn't valid url!`
        };
    }

    const analyzedSite: URLAnalyzerReturn = await URLAnalyzer(websiteUrl);

    if (!analyzedSite || analyzedSite.error) {
        return {
            error: `${analyzedSite?.error} ${analyzedSite?.details}` || "Analysis failed"
        };
    }

    const content = analyzedSite.content;

    if (!content) {
        return {
            error: "site content not found!"
        };
    }

    const $ = cheerio.load(content);
    let moneyValue: string | null = null;

    switch (category) {
        case 'trendyol':
            const moneyTag = $(".pr-in-cn").text();
            const matches = moneyTag.match(/\d+(.?)+\s*TL/g);
            if (matches && matches.length > 0) {
                moneyValue = matches[0];
            }
            break;
        case 'hepsiburada':
            // Hepsiburada için para değeri çıkarma mantığı
            break;
        case 'daraaksesuar':
            // Daraaksesuar için para değeri çıkarma mantığı
            break;
    }

    if (moneyValue) {
        return {
            target: {
                url: websiteUrl,
                money: moneyValue
            }
        };
    }

    return {
        error: "Could not extract money information from the website!"
    };
}

export async function getProxiesFromURL(url: string) {
    try {
        const proxyListURLRes = await fetch("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/refs/heads/master/http.txt");

        if (!proxyListURLRes.ok) {
            throw new Error(`status = ${proxyListURLRes.status}\n${proxyListURLRes}\n`);
        }
    } catch (err: any) {
        return {
            error: `Gettting a proxy url's process done with errors!\n${err}`
        }
    }
}