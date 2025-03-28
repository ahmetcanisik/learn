# React foundations

create like buttons of client components

```jsx
'use client';
import { useState } from 'react';

export function LikeButton() {
    const [like, setLike] = useState(0);

    const handleClick () => setLike(like + 1);

    return (
        <button onClick={handleClick}>like ({like})</button>
    );
}
```