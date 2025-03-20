import { convertToValidURL } from '@/helpers/validate';

test('domain name to valid url', () => {
    expect(convertToValidURL("example.com")).toEqual("https://example.com");
});

test("it's same full url's", () => {
    expect(convertToValidURL("http://example.com")).toEqual("http://example.com");
});