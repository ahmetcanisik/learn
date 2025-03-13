import Link from "next/link";

function HomePage() {
  return (
    <div>
      <h1>home page is here.</h1>
      <Link href="/login?from=home">Login</Link>
    </div>
  );
}

export default HomePage;