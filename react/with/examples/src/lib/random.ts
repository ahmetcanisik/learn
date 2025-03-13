export interface RandomOptionsType {
    /**
     * add numbers to random character.
     * excepted true or false
     */
    numbers?: boolean;
  
    /**
     * add characters(upper-lower or all) to random characters
     * upper: only upper case
     * lower: only lower case
     * true: lower and upper case
     * false: don't add characters to random character list.
     */
    chars?: "upper" | "lower" | true | false;
  
    /**
     * add special characters to random character list.
     * string: add spesific characters to random character list.
     * undefined: don't add special characters to random character list
     */
    specialChars?: string | undefined;
  
    /**
     * add turkish characters(upper-lower or all) to random characters
     * upper: only upper case turkish chars
     * lower: only lower case turkish chars
     * true: lower and upper case turkish chars
     * false: don't add turkish chars to random character list.
     */
    turkishChars?: "upper" | "lower" | true | false;
  }
  
  export const DEFAULT_RANDOM_OPTIONS: RandomOptionsType = {
    numbers: true,
    chars: false,
    turkishChars: false,
    specialChars: undefined,
  };
  
  function random(
    len: number,
    options: RandomOptionsType = DEFAULT_RANDOM_OPTIONS
  ): string {
    options = {
      ...DEFAULT_RANDOM_OPTIONS,
      ...options,
    };
  
    let r = "";
    let c = "ABCDEFGHIJKLMNOPRSTUVYZXW";
  
    if (options) {
      const t = "ÇĞİÖŞÜ";
  
      const uc = options.chars === true || options.chars === "upper" ? c : "";
      const lc =
        options.chars === true || options.chars === "lower"
          ? c.toLowerCase()
          : "";
      const n = options.numbers ? "0123456789" : "";
      const tu =
        options.turkishChars === true || options.turkishChars === "upper"
          ? t
          : "";
      const tl =
        options.turkishChars === true || options.turkishChars === "lower"
          ? t.toLowerCase()
          : "";
      const s =
        options.specialChars && typeof options.specialChars === "string"
          ? options.specialChars
          : "";
  
      c = uc + lc + n + tu + tl + s;
    }
  
    for (let i = 0; i < len; i++) {
      r += c[Math.floor(Math.random() * c.length)];
    }
  
    return r;
  }
  
  export default random;  