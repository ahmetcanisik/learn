const params = new URLSearchParams(window.location.search);

const homeworks = new window.Homeworks().get_homeworks;
let isHomeworkCreated = false;
let currentHomeworkIndex = (params.get("hw") && (params.get("hw")) <= homeworks.length - 1) ? params.get("hw") : 0;

if (currentHomeworkIndex === 0) {
    params.set("hw", "0");
}

function createElem(parent, type, id, className, text) {
    const elem = document.createElement(type);

    if (id) {
        elem.id = id;
    }

    if (className) {
        elem.className = className;
    }

    if (text) {
        elem.innerText = text;
    }

    if (parent) {
        parent.appendChild(elem);
    }

    return elem;
}

function createHomework(parent, update = false, homework = {}) {
    if (homework.length <= 0) {
        throw new Error("homeworks length less then zero!");
    }
    
    const prevPagID = "previous-homework";
    const nextPagID = "next-homework";
    const hHSubtitleID = "homework-header-subtitle";
    const hTitleID = "homework-title";
    const hMCodeBlockID = "homework-list";
    const hFLessonID = "homwork-lesson";
    const hFAuthorID = "homework-author";
    const hID = "homework";
    const hHeaderID = "homework-header";
    const hMainID = "homework-main";
    const hFooterID = "homework-footer";
    const mobilePagID = "homework-mobile-pagination";
    const mPrevPagID = "homework-mobile-prev-pag";
    const mNextPagID = "homework-mobile-next-pag";

    const prevPagIcon = "<<";
    const nextPagIcon = ">>";

    const domTitle = document.querySelector("title");
    domTitle.innerHTML = "";

    const prevPag = update ? document.getElementById(prevPagID) : createElem(parent, 'button', prevPagID, 'btn pagination-btn', prevPagIcon);
    prevPag.addEventListener("click", () => prevHomwork(false, parent));

    const h = update ? document.getElementById(hID) : createElem(parent, 'main', hID, "homework");

    if (homework.title || homework.homeworkID) {
        const hHeader = update ? document.getElementById(hHeaderID) : createElem(h, 'header', hHeaderID, 'homework-title');
        if (homework.homeworkID) {
            const hHSubtitle = update ? document.getElementById(hHSubtitleID) : createElem(hHeader, 'span', hHSubtitleID, 'homework-subtitle');
            const text = `${homework.homeworkID}. Ödev`;
            hHSubtitle.innerText = text;
            domTitle.innerHTML += `${text} - `;
        }

        if (homework.title) {
            const hTitle = update ? document.getElementById(hTitleID) : createElem(hHeader, 'span', hTitleID);
            hTitle.innerText = homework.title;
            domTitle.innerHTML += `${homework.title} | `;
        }
    }

    if (homework.execfn) {
        const hMain = update ? document.getElementById(hMainID) : createElem(h, "main", hMainID);
        const hMCodeBlock = update ? document.getElementById(hMCodeBlockID) : createElem(hMain, 'div', hMCodeBlockID, 'homework-codeblock');
        hMCodeBlock.innerHTML = "";
        homework.execfn(hMCodeBlock);
    }

    if ((homework.lesson && homework.depart) || homework.author) {
        const hFooter = update ? document.getElementById(hFooterID) : createElem(h, 'footer', hFooterID, 'homework-subtitle');

        if (homework.lesson && homework.depart) {
            const hFLesson = update ? hFAuthorID : createElem(hFooter, hFLessonID, "div");
            hFLesson.innerText = `${homework.lesson} ${homework.depart}`;
            domTitle.innerHTML += `${homework.lesson} - ${homework.depart} |`;
        }

        if (homework.author) {
            const hFAuthor = update ? document.getElementById(hFAuthorID) : createElem(hFooter, hFAuthorID, "div");
            hFAuthor.innerText = homework.author;
            domTitle.innerHTML += homework.author;
        }
    }

    const nextPag = update ? document.getElementById(nextPagID) : createElem(parent, 'button', nextPagID, 'btn pagination-btn', nextPagIcon);
    nextPag.addEventListener("click", () => nextHomework(false, parent));

    const mobilePag = update ? document.getElementById(mobilePagID) : createElem(parent, 'div', mobilePagID, 'mobile-pagination');
    
    const mPrevPag = update ? document.getElementById(mPrevPagID) : createElem(mobilePag, 'button', mPrevPagID, 'btn', prevPagIcon);
    mPrevPag.addEventListener("click", () => prevHomwork(false, parent));

    const mNextPag = update ? document.getElementById(mNextPagID) : createElem(mobilePag, 'button', mNextPagID, 'btn', nextPagIcon);
    mNextPag.addEventListener("click", () => nextHomework(false, parent));

    if (isHomeworkCreated === false) {
        isHomeworkCreated = true;
    }
}

function nextHomework(get = false, parent, currentIndex = currentHomeworkIndex, latestIndex = homeworks.length - 1) {
    
    currentHomeworkIndex = (latestIndex > currentIndex) ? currentIndex + 1 : 0;

    params.set("hw", currentHomeworkIndex);
    
    return get ? currentHomeworkIndex : createHomework(parent, true, homeworks[currentHomeworkIndex]);
}

function prevHomwork(get = false, parent, currentIndex = currentHomeworkIndex, latestIndex = homeworks.length - 1) {
    
    currentHomeworkIndex = (currentIndex > 0) ? currentIndex - 1 : latestIndex;

    params.set("hw", currentHomeworkIndex);
    
    return get ? currentHomeworkIndex : createHomework(parent, true, homeworks[currentHomeworkIndex]);
}

document.addEventListener("DOMContentLoaded", () => {
    const work = document.createElement("main");
    work.className = "work";

    if (!isHomeworkCreated) {
        createHomework(work, false, homeworks[currentHomeworkIndex]);
    }

    document.body.appendChild(work);
});