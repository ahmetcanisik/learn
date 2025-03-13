import { ViewApp, Link } from "@/components";

function App() {
    return (
        <div>
            <ViewApp>
                <ul className="flex flex-col">
                    <li><Link href="/calculator">Calculator</Link></li>
                    <li><Link href="/captcha">Captcha</Link></li>
                </ul>
            </ViewApp>
        </div>
    );
}

export default App;