Array.prototype.ilkVeSonElemen = function() {
    return [
        this[0],
        this[this.length - 1]
    ]
};

const a = ["ilk elemen", "ikinci elemen", "üçüncü elemen", "dördüncü elemen", "sonuncu eleman"];
console.log(a.ilkVeSonElemen());