function Link({ href, children }: { href: string; children: React.ReactNode }) {
    return (
        <a href={href}>{children}</a>
    );
}

export default Link;