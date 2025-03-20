import { isValidURL } from "@/helpers/validate";

test('http and https', () => {
    expect(isValidURL("https://example.com")).toBeTruthy();
    expect(isValidURL("http://example.com")).toBeTruthy();
});

test('ftp and tcp', () => {
    expect(isValidURL("ftp://example.com")).toBeFalsy();
    expect(isValidURL("tcp://example.com")).toBeFalsy();
});

test('if protocol not defined and :// prompted!', () => {
    expect(isValidURL("://example.com")).toBeFalsy();
});

test('only domain name', () => {
    expect(isValidURL("example.com")).toBeTruthy();
});

test('domain extension if not prompted', () => {
    expect(isValidURL("examplecom")).toBeFalsy();
});

test('if url is empty', () => {
    expect(isValidURL("")).toBeFalsy();
});

test('domain name is not specifyed', () => {
    expect(isValidURL("https://..com")).toBeFalsy();
});

test('domain extensions', () => {
    expect(isValidURL("example.com.tr")).toBeTruthy();
});

test('url leafs', () => {
    expect(isValidURL("https://raw.githubusercontent.com/ahmetcanisik/learn/refs/heads/main/README.md")).toBeTruthy();
})