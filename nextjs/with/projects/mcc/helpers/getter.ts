import { URLAnalyzer } from './analyzer';
import { isValidURL } from './validate';

export async function getMoney(websiteUrl: string | string[], category: 'trendyol' | 'hepsiburada' | 'daraaksesuar') {
    if (!isValidURL(websiteUrl)) {
        return null;
    }

    const $ = await URLAnalyzer(websiteUrl);
}