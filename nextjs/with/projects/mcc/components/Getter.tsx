'use client';
import { useEffect, useState } from "react";
import { getMoney } from "@/helpers/getter";

export default function GetMoney({ url }: { url: string }) {
    const [error, setError] = useState("");
    const [loading, setLoading] = useState(true);
    const [money, setMoney] = useState('');

    useEffect(() => {
        setLoading(true);
        getMoney(url, 'trendyol')
            .then((data) => {
                if (data.error) {
                    setError(data.error);
                    return;
                }

                if (data.target) {
                    setMoney(data.target.money);
                }
            })
            .catch((err) => setError(err.message))
            .finally(() => setLoading(false));
    }, []); // Boş bağımlılık dizisi, sadece bir kez çalışmasını sağlar

    if (loading) return <div>Yükleniyor...</div>;
    if (error) return <div>Hata: {error}</div>;

    return (
        <div>
            <div>
                {money}
            </div>
        </div>
    );
}