import { isValidURL, convertToValidURL } from "./validate";
import fetch from "node-fetch";
import { HttpsProxyAgent } from "https-proxy-agent";
import { HttpProxyAgent } from "http-proxy-agent";

export interface URLAnalyzerReturn {
    url?: string;
    content?: string;
    error?: string;
    status?: number;
    statusText?: string;
    details?: string;
}

// Agent oluşturma fonksiyonu - HTTP veya HTTPS için
function createAgent(url: string, proxyUrl?: string) {
  const isHttps = url.startsWith('https://');
  
  if (proxyUrl) {
    return isHttps 
      ? new HttpsProxyAgent(proxyUrl)
      : new HttpProxyAgent(proxyUrl);
  }
  
  return undefined;
}

export async function URLAnalyzer(websiteUrl: string, options: {
  timeout?: number,
  proxyUrl?: string,
  headers?: Record<string, string>
} = {}): Promise<URLAnalyzerReturn> {
  try {
    if (!isValidURL(websiteUrl)) {
      return { error: "URLAnalyzer: Invalid url format!" };
    }

    const url = convertToValidURL(websiteUrl);

    if (!url) {
      return { error: "URLAnalyzer: URL conversion failed!" };
    }

    // Agent ve fetch options oluşturma
    const agent = createAgent(url, options.proxyUrl);
    const fetchOptions: any = {
      agent,
      timeout: options.timeout || 30000, // Varsayılan 30 saniye
      headers: {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
        ...options.headers
      }
    };

    // İsteği gönderme
    const siteRes = await fetch(url, fetchOptions);

    if (!siteRes.ok) {
      return {
        error: "URLAnalyzer: Request failed!",
        status: siteRes.status,
        statusText: siteRes.statusText,
      };
    }

    return {
        url: url,
        content: await siteRes.text()
    };
  } catch (err: any) {
    return { 
      error: "URLAnalyzer: Exception occurred", 
      details: err.message 
    };
  }
}