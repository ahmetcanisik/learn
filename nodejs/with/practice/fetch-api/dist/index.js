"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
function getApi(apiServer) {
    return __awaiter(this, void 0, void 0, function* () {
        try {
            const res = yield fetch(apiServer);
            if (res.status === 200) {
                const data = yield res.json();
                return data;
            }
        }
        catch (e) {
            console.error(`When sending request on the ${apiServer} catching errors -> `, e);
        }
    });
}
function main() {
    return __awaiter(this, void 0, void 0, function* () {
        const myHTMLSkill = yield getApi("https://api.ahmetcanisik.com/skills");
        myHTMLSkill.forEach((skill, index) => {
            let progressBar = "";
            for (let i = 0; i < (skill.progress / 10); i++) {
                progressBar += "*";
            }
            ;
            console.log(`${progressBar}\t\t -> ${skill.name}`);
        });
    });
}
(() => __awaiter(void 0, void 0, void 0, function* () { return yield main(); }))();
