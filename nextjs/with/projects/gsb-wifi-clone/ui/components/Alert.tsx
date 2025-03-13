import clsx from "clsx";

function Alert({color, label, children, variant, size}: {
    color?: 'default' | 'danger' | 'success';
    variant?: 'solid' | 'soft';
    size?: 'sm' | 'normal';
    label?: string;
    children?: React.ReactNode
} = {
    color: "default",
    variant: 'solid',
}) {
    return (
        <div
            className={clsx(
                "rounded p-2 text-center",
                {
                    "bg-red-200 text-red-600": color === "danger",
                    "bg-green-200 text-green-800": color === "success",
                    "bg-transparent font-bold": variant === "soft",
                    "text-xs": size === "sm",
                }
            )}
        >
            {children && children}
            {label && label}
        </div>
    );
}

export default Alert;