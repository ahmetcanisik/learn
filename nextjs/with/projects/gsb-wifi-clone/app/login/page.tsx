import {redirect} from "next/navigation";
import Image from "next/image";
import Alert from "@/ui/components/Alert";

export default function Login({searchParams}: { searchParams: { from?: string, logout?: '0' | '1' } }) {
    if (searchParams?.logout === '1') redirect("/");

    return (
        <div>
            <div className="w-full flex justify-center py-8">
                <Image src="/img/banner.jpg" alt="T.C. GENÇLİK VE SPOR BAKANLIĞI KREDİ VE YURTLAR GENEL MÜDÜRLÜĞÜ"
                       width={1133} height={145}/>
            </div>
            <div className="flex flex-col justify-center items-center">
                <Alert variant="soft" color="success"
                       label="Welcome. Enter your login information and press 'Login' button to access internet."/>
                <Alert variant="soft" color="danger"
                       label="Değerli öğrencilerimiz; 'Kotanızdan Düşmeden' üniversite internet sitelerinize ve Ulakbim’e kullanıcı adı ve şifrenizi girmeden internet adreslerini tarayıcınızdan yazarak erişebilirsiniz.Diğer internet erişimleriniz için Kullanıcı adı ve şifre ile giriş yaptıysanız, Kotanızdan düşmeden üniversite sitelerine ve Ulakbim’ e, erişim için çıkış yapmanız gerekmektedir."/>
                <form>
                    <div className="w-full md:w-1/3 m-auto flex flex-col py-10 gap-4 justify-center items-center">
                        <label htmlFor="uname">
                            <span className="label-text">User name: </span>
                            <input id="uname" name="uname" type="text"/>
                        </label>
                        <label htmlFor="passwd">
                            <span className="label-text">Password: </span>
                            <input id="passwd" name="passwd" type="password"/>
                        </label>

                        <button type="submit">Login</button>
                        <button>New User</button>
                    </div>
                </form>
                <Alert variant="soft" color="danger"
                       label="*For effective use of system you should disable popup blocker"/>
                <Alert size="sm" variant="soft" color="success"
                       label="* If you are using mobile device for connection, be sure that you are connected to GSB WiFi network and 2G/3G connection is closed."/>
                {/*<p>Login Page</p>*/}
                {/*<Link href="/login?logout=1">exit</Link>*/}
            </div>
        </div>
    );
}