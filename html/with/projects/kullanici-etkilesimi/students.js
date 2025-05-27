import { students } from "./data.js";
import {
    is_valid_name,
    is_school_number,
    is_valid_note
} from './checks.js';

function updateStudents(parent, noAlert = false) {
    parent.innerHTML = "";
    const studentsDiv = document.createElement("table");
    studentsDiv.innerHTML = `<thead><tr><th>Adı</th><th>Soyadı</th><th>Numarası</th><th>Notu</th><th>Bölümü</th></tr></thead>`;
    studentsDiv.id = "students";

    studentsDiv.className = "students"
    students.forEach(student => {
        studentsDiv.innerHTML += `
<tr>	
	<td>${student.name}</td>
    <td>${student.surname}</td>
    <td>${student.number}</td>
    <td>${student.note}</td>
    <td>${student.depart}</td>
</tr>
`;
    });
    parent.appendChild(studentsDiv);

    if (!noAlert){
        window.alert("Öğrenci Listesi Güncellendi!")
    }
}

function saveStudent(parent, name, surname, number, note, depart) {
    if (is_valid_name(name) === false) {
        return {
            errorOn: "name"
        };
    }

    if (is_valid_name(surname) === false) {
        return {
            errorOn: "surname"
        };
    }

    if (is_school_number(number) === false) {
        return {
            errorOn: "number"
        };
    }

    // Check if the student number is already in use
    if (students.find(s => s.number === number)) {
        return {
            errorOn: "number"
        };
    }

    if (is_valid_note(note) === false) {
        return {
            errorOn: "note"
        };
    }

    if (is_valid_name(depart) === false) {
        return {
            errorOn: "depart"
        };
    }
    
    students.push({
        name: name,
        surname: surname,
        number: number,
        note: note,
        depart: depart
    });

    window.alert(`${name} ${surname} başarıyla eklendi!`)
    updateStudents(parent, true);
}

async function main() {
    const studentsDiv = document.createElement("div");
    studentsDiv.className = "students";
    document.querySelector("main").appendChild(studentsDiv);

    updateStudents(studentsDiv, true);

    const form = document.getElementById("saveStudent");

    form.addEventListener("submit", (e) => {
        e.preventDefault();

        const s = {}
        const formData = new FormData(e.target);
        for (const [key, value] of formData.entries()) {
            s[key] = value;
        }
        const error = saveStudent(studentsDiv, s.name, s.surname, s.studentNumber, s.note, s.depart);

        if (error.errorOn) {
            e.target.name.classList.remove("error");
            e.target.surname.classList.remove("error");
            e.target.studentNumber.classList.remove("error");
            e.target.note.classList.remove("error");
            e.target.depart.classList.remove("error");


            if (error.errorOn === "name") {
                e.target.name.classList.add("error");
                e.target.name.focus();
            }
            if (error.errorOn === "surname") {
                e.target.surname.classList.add("error");
                e.target.surname.focus();
            }
            if (error.errorOn === "number") {
                e.target.studentNumber.classList.add("error");
                e.target.studentNumber.focus();
            }
            if (error.errorOn === "note") {
                e.target.note.classList.add("error");
                e.target.note.focus();
            }
            if (error.errorOn === "depart") {
                e.target.depart.classList.add("error");
                e.target.depart.focus();
            }
        }
    });
}

document.addEventListener("DOMContentLoaded", async () => await main())