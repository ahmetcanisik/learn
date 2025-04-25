import puppeteer from 'puppeteer';

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();

  await page.goto('https://tineye.com/');
  const [fileChooser] = await Promise.all([
    page.waitForFileChooser(),
    page.click('#upload-button')
  ]);
  await fileChooser.accept(['/Users/canisik/Downloads/picture.png']);

  await page.waitForSelector('.match-list');
  const results = await page.$$eval('.match-list li', (links: any) => links.map((el: any) => el.innerText));
  console.log(results);

  await browser.close();
})();