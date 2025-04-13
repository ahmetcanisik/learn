interface AsciicIcons {
  x: string;
  y: string;
  tl: string;
  tr: string;
  bl: string;
  br: string;
  a: string;
}

interface AsciicOptions {
  paddingX?: number;
  paddingY?: number;
  textAlign?: 'left' | 'center' | 'right';
}

class Asciic {
  // icons
  private i: AsciicIcons = {
    x: "─",
    y: "│",
    tl: "┌",
    tr: "┐",
    bl: "└",
    br: "┘",
    a: "►",
  };

  // example Asciic.new("Hello World!")
  new(message: string | string[], options?: AsciicOptions): string {
    let maxLength = 0;
    const messages = typeof message === "string" ? [message] : message;

    messages.forEach((msg) => {
      maxLength = msg.length > maxLength ? msg.length : maxLength;
    });

    const paddingX =
      options && options.paddingX !== undefined ? options.paddingX : 2;
    const paddingY =
      options && options.paddingY !== undefined ? options.paddingY : 1;
    const textAlign =
      options && options.textAlign !== undefined ? options.textAlign : 'left';

    // Calculate dimensions based on message length and padding
    const width = maxLength + (paddingX * 2); // Width includes message + left/right padding
    const innerWidth = width - 2; // Width between the vertical borders
    
    let result = "";

    // Top border
    result += this.i.tl + this.i.x.repeat(innerWidth) + this.i.tr + "\n";

    // Top padding
    for (let p = 0; p < paddingY; p++) {
      result += this.i.y + " ".repeat(innerWidth) + this.i.y + "\n";
    }

    messages.forEach((msg) => {
      // Calculate padding based on text alignment
      let leftPadding = 0;
      let rightPadding = 0;
      
      if (textAlign === 'center') {
        // For center, distribute padding evenly
        leftPadding = Math.floor((innerWidth - msg.length) / 2);
        rightPadding = innerWidth - msg.length - leftPadding;
      } else if (textAlign === 'right') {
        // For right, fixed padding on right
        rightPadding = paddingX;
        leftPadding = innerWidth - msg.length - rightPadding;
      } else { // left is default
        // For left, fixed padding on left
        leftPadding = paddingX;
        rightPadding = innerWidth - msg.length - leftPadding;
      }
      
      // Ensure padding is never negative
      leftPadding = Math.max(leftPadding, 0);
      rightPadding = Math.max(rightPadding, 0);
      
      result +=
        this.i.y +
        " ".repeat(leftPadding) +
        msg +
        " ".repeat(rightPadding) +
        this.i.y +
        "\n";
    });

    // Bottom padding
    for (let p = 0; p < paddingY; p++) {
      result += this.i.y + " ".repeat(innerWidth) + this.i.y + "\n";
    }

    // Bottom border
    result += this.i.bl + this.i.x.repeat(innerWidth) + this.i.br;

    return result;
  }
}

// Default (left alignment)
console.log("Left alignment (default):");
console.log(new Asciic().new([
  "UPDATE AVAILABLE!", 
  "please update your pnpm version!",
  "npm i -g pnpm"
],
{
    paddingX: 0,
    textAlign: 'left'
}));