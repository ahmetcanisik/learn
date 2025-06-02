class Mathf {
    static addition(...numbers) {
        let result = 0;

        numbers.forEach((n, i) => {
            if (typeof n !== "number") {
                throw new Error("please provide only numbers!");
            }

            if (i === 0) {
                result = n;
            }

            result += n;
        });

        return result;
    }

    static subtraction(...numbers) {
        let result = 0;

        numbers.forEach((n, i) => {
            if (typeof n !== "number") {
                throw new Error("please provide only numbers!");
            }

            if (i === 0) {
                result = n;
            }
            result -= n;
        });

        return result;
    }

    static multiply(...numbers) {
        let result = 0;

        numbers.forEach((n, i) => {
            if (typeof n !== "number") {
                throw new Error("please provide only numbers!");
            }

            if (i === 0) {
                result = n;
            }

            result *= n;
        });

        return result;
    }

    static divide(...numbers) {
        let result = 0;

        numbers.forEach((n, i) => {
            if (typeof n !== "number") {
                throw new Error("please provide only numbers!");
            }

            if (i === 0) {
                result = n;
            }

            result /= n;
        });

        return result;
    }
}

function splitToWords(sentence) {
    if (!sentence || typeof sentence !== "string") {
        throw new Error("please specify a valid sentence!");
    }

    const splitted = sentence.trim().split(" ");

    if (!splitted || splitted.length <= 0) {
        throw new Error("words not found!");
    }

    return {
        wordsLength: splitted.length,
        sWords: splitted
    }
}

function listWords(parent, value) {
    if (!value.trim()) {
        alert("please enter some words!");
    }

    const { wordsLength, sWords } = splitToWords(value);

    const ol = document.createElement("ol");

    sWords.forEach(word => {
        const li = document.createElement("li");
        li.innerText = word;
        ol.appendChild(li);
    });

    parent.innerHTML = "";
    const sentence = document.createElement("div");
    sentence.innerText = `"${value}"`;
    parent.appendChild(sentence);

    parent.appendChild(ol);

    const lengthLi = document.createElement("div");
    lengthLi.innerText = `toplam kelime sayısı: ${wordsLength}`;
    parent.appendChild(lengthLi);
}

class Homeworks {
    #homeworks = [
        {
            homeworkID: 1,
            title: "İki değişkenin Dört işlemi",
            description: "İki değişken oluşturup bunları dört işleme tabi tutuyoruz.",
            tags: ["dört işlem", "fonksiyon", "değişken"],
            lesson: "Etkileşimli Web Arayüzü Geliştirme",
            author: "Ahmet Can IŞIK",
            depart: "WTK",
            school: "Harran University",
            execfn: this.first
        },
        {
            homeworkID: 2,
            title: "Dört işleme dört fonksiyon",
            description: "Dört işlem için ayrı fonksiyonlar tanımlıyoruz.",
            tags: ["dört işlem", "fonksiyon", "değişken"],
            lesson: "Etkileşimli Web Arayüzü Geliştirme",
            author: "Ahmet Can IŞIK",
            depart: "WTK",
            school: "Harran University",
            execfn: this.second
        },
        {
            homeworkID: 3,
            title: "Cümleyi kelimelerine ayırmak",
            description: "Kullanıcıdan alınan bir cümleyi kelimelerine ayırıyoruz.",
            tags: ["cümle", "kelime", "fonksiyon"],
            lesson: "Etkileşimli Web Arayüzü Geliştirme",
            author: "Ahmet Can IŞIK",
            depart: "WTK",
            school: "Harran University",
            execfn: this.third
        },
        {
            homeworkID: 4,
            title: "Karşılaştır babam karşılaştır",
            description: "Kullanıcıdan alınan iki sayının çarpım ve toplamlarını karşılaştırıyoruz.",
            tags: ["karşılaştırma", "fonksiyon", "değişken"],
            lesson: "Etkileşimli Web Arayüzü Geliştirme",
            author: "Ahmet Can IŞIK",
            depart: "WTK",
            school: "Harran University",
            execfn: this.fourth
        }
    ];

    first(parent) {
        const a = 5;
        const b = 3;

        for (let i = 0; i <= 3; i++) {
            let icon = "";
            let result = 0;

            switch (i) {
                case 0:
                    icon = "+";
                    result = a + b;
                    break;
                case 1:
                    icon = "-";
                    result = a - b;
                    break;
                case 2:
                    icon = "*";
                    result = a * b;
                    break;
                case 3:
                    icon = "/";
                    result = a / b;
                    break;
                default:
                    break;
            }

            const row = document.createElement('div');
            row.innerText = `${a} ${icon} ${b} = ${result}`;
            parent.appendChild(row);
        }
    }

    second(parent) {
        const a = 5;
        const b = 3;

        for (let i = 0; i <= 3; i++) {
            let icon = "";
            let result = 0;

            switch (i) {
                case 0:
                    icon = "+";
                    result = Mathf.addition(a, b);
                    break;
                case 1:
                    icon = "-";
                    result = Mathf.subtraction(a, b);
                    break;
                case 2:
                    icon = "*";
                    result = Mathf.multiply(a, b);
                    break;
                case 3:
                    icon = "/";
                    result = Mathf.divide(a, b);
                    break;
                default:
                    break;
            }

            const row = document.createElement('div');
            row.innerText = `${a} ${icon} ${b} = ${result}`;
            parent.appendChild(row);
        }
    }

    third(parent) {
        const input = document.createElement("input");
        input.className = "inp";
        input.placeholder = "Cümlenizi yazınız..."
        input.type = "text";
        parent.appendChild(input);

        input.addEventListener('keypress', (e) => {
            if (e.key === "Enter") {
                listWords(parent, e.target.value);
            }
        })

        const button = document.createElement("button");
        button.className = "btn";
        button.innerText = "kelimelerine ayır";
        parent.appendChild(button);

        button.addEventListener("click", () => {
            listWords(parent, input.value);
        });
    }

    fourth(parent) {
        const nums = [NaN, NaN];

        for (let i = 0; i <= 2; i++) {
            if (i == 2) {
                const button = document.createElement("button");
                button.className = "btn";
                button.innerText = "Karşılaştır";
                parent.appendChild(button);

                button.addEventListener("click", () => {
                    if (nums[0] === NaN || nums[1] === NaN) {
                        alert("Lütfen sayıları giriniz!");
                        return;
                    }

                    const resultDiv = document.getElementById("result-div") ?? document.createElement("div");
                    resultDiv.innerHTML = "";
                    resultDiv.id = "result-div";
                    const multiply = nums[0] * nums[1];
                    const addition = nums[0] + nums[1];
                    if (multiply > addition) {
                        resultDiv.innerText = `Çarpım(${multiply}) toplamdan(${addition}) büyüktür.`;
                    }
                    else if (multiply < addition) {
                        resultDiv.innerText = `Toplam(${addition}) çarpımdan(${multiply}) küçüktür.`;
                    } else {
                        resultDiv.innerText = `Çarpım ve toplam eşittir: ${multiply}`;
                    }
                    parent.appendChild(resultDiv);
                })
                break;
            }

            const input = document.createElement("input");
            input.type = "number";
            input.className = "inp";
            input.placeholder = `Sayı ${i + 1}`;
            parent.appendChild(input);

            input.addEventListener("input", (e) => {
                nums[i] = Number(e.target.value);
            });
        }
    }

    fiveth(parent) {
        
    }

    get get_homeworks() {
        return this.#homeworks;
    }
}

if (typeof window !== undefined) {
    window.Homeworks = Homeworks;
    window.Mathf = Mathf;
}

if (typeof module === "object") {
    module.exports = Homeworks;
    module.exports = Mathf;
}