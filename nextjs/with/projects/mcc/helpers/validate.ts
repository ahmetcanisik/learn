export function isValidURL(url: string): boolean {
  // Handle empty, null, or undefined values
  if (!url) {
    return false;
  }

  // Handle domain names without protocol
  if (!url.includes("://")) {
    // Check if it's a valid domain name with extension and optional path
    return /^([\w-]+\.)+[a-zA-Z]{2,}(\.[a-zA-Z]{2,})?(\/.*)?$/.test(url);
  }

  // Extract protocol and validate
  const parts = url.split("://");
  if (parts.length !== 2 || !parts[0] || !parts[1]) {
    return false;
  }

  const protocol = parts[0];
  const domain = parts[1];

  // Only allow http and https protocols
  if (protocol !== "http" && protocol !== "https") {
    return false;
  }

  // Validate domain format with any extension and optional path
  if (!domain.match(/^([\w-]+\.)+[a-zA-Z]{2,}(\.[a-zA-Z]{2,})?(\/.*)?$/)) {
    return false;
  }

  return true;
}

export function convertToValidURL(url: string): string | null {
  if (!url) return null;

  // Remove any leading/trailing whitespace
  const trimmedUrl = url.trim();

  // If URL is already valid, return it
  if (isValidURL(trimmedUrl)) {
    // If it's already a full URL with protocol
    if (trimmedUrl.includes("://")) {
      return trimmedUrl;
    }
    // It's a valid domain without protocol, add https://
    return `https://${trimmedUrl}`;
  }

  // Check if it's potentially a valid domain without protocol but didn't pass validation
  if (
    !trimmedUrl.includes("://") &&
    /^([\w-]+\.)+[a-zA-Z]{2,}(\.[a-zA-Z]{2,})?(\/.*)?$/.test(trimmedUrl)
  ) {
    return `https://${trimmedUrl}`;
  }

  // URL is not valid and can't be automatically fixed
  return null;
}