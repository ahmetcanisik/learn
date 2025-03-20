import { isValidURL, convertToValidURL } from "./validate";
import * as cheerio from "cheerio";
import type { CheerioAPI } from "cheerio";

export interface URLAnalyzerReturn {
    url?: string;
    content?: CheerioAPI;
    error?: string;
    status?: number;
    statusText?: string;
    details?: string;
}

export async function URLAnalyzer(websiteUrl: string): Promise<URLAnalyzerReturn> {
  try {
    if (!isValidURL(websiteUrl)) {
      return { error: "Invalid url format!" };
    }

    const url = convertToValidURL(websiteUrl);

    if (!url) {
      return { error: "URL conversion failed!" };
    }

    const siteRes = await fetch(url);

    if (!siteRes.ok) {
      return {
        error: "Request failed!",
        status: siteRes.status,
        statusText: siteRes.statusText,
      };
    }

    const pageContent = await siteRes.text();

    return {
        url: url,
        content: cheerio.load(pageContent)
    };
  } catch (err: any) {
    return { error: "Exception occurred", details: err.message };
  }
}

