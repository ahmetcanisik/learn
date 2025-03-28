'use client';
import { useEffect, useState } from "react";
import { URLAnalyzer } from "@/helpers/analyzer";

export default function Analyzer({ url }: { url: string }) {
    const [error, setError] = useState("");
    const [loading, setLoading] = useState(true);
    const [pageContent, setPageContent] = useState('');

    useEffect(() => {
        setLoading(true);
        URLAnalyzer(url)
            .then((data) => {
                if (data.error) {
                    setError(data.error);
                    return;
                }

                if (data.content) {
                    // Cheerio ile sayfadan bilgileri çekelim
                    setPageContent(data.content);
                }
            })
            .catch((err) => setError(err.message))
            .finally(() => setLoading(false));
    }, []); // Boş bağımlılık dizisi, sadece bir kez çalışmasını sağlar

    if (loading) return <div>Yükleniyor...</div>;
    if (error) return <div>Hata: {error}</div>;

    return (
        <div>
            <div dangerouslySetInnerHTML={{ __html: pageContent }} />
        </div>
    );
}