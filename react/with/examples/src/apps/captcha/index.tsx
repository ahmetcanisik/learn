import { useState, useEffect, useRef } from "react";
import html2canvas from "html2canvas";
import random from "@/lib/random";

function Captcha({ length }: { length: number }) {
    const [captchaText, setCaptchaText] = useState(random(length));
    const captchaRef = useRef<HTMLDivElement>(null);

    useEffect(() => {
        if (captchaRef.current) {
            html2canvas(captchaRef.current).then(canvas => {
                captchaRef.current?.appendChild(canvas);
            });
        }
    }, [length]);

    const validateCaptcha = (up: string) => {
        setCaptchaText(random(length));
    }

    return (
        <div>
            {/* Captcha metni */}
            <div ref={captchaRef} className="bg-gray-500 text-white">
                {captchaText}
            </div>
            <button onClick={validateCaptcha}>check</button>
        </div>
    );
}

export default Captcha;