export function is_valid_name(name) {
    return /^[\D\s]+$/.test(name);
}

export function is_school_number(number) {
    return /^\d{9}$/.test(number);
}

export function is_valid_note(note) {
    return /^([0123]{1}(\.\d){0,2}|4\.0)$/.test(note);
}