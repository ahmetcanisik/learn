export default function El({
    children
}: {
    children: React.ReactNode;
}) {
    return (
        <div>
            <div></div>
            {children}
        </div>
    );
}