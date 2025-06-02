
interface ListIndexes {
    [key: number]: any;
}

interface ListType extends ListIndexes {
    reverse: () => void;
    toList: () => void;
}

export class List {
    items: Array<any> = [];

    constructor(...rest: any) {
        this.items = [...rest];
    }

    toString(): string {
        return JSON.stringify(this.items);
    }

    toObject(): ListType {
        const obj: any = {};
        
        // Önce tüm elemanları ve length'i ekleyelim
        for (let i = 0; i < this.items.length; i++) {
            obj[i] = this.items[i];
        }
        obj["length"] = this.items.length;

        obj.toList = function () {
            const newArr: Array<any> = [];
            Object.entries(this).forEach(([key, value]: any) => {
                if (key.match(/^\d{1,}$/g)) {
                    newArr.push(value);
                }
            })
            return new List(...newArr);
        }
        
        // Sonra reverse metodunu ekleyelim
        obj.reverse = function(): ListType {
            const lastIndex = this.length - 1;
            for (let i = 0; i < Math.floor(this.length / 2); i++) {
                const oppositeIndex = lastIndex - i;
                const temp = this[i];
                this[i] = this[oppositeIndex];
                this[oppositeIndex] = temp;
            }
            return this;
        };


        return obj as ListType;
    }
}