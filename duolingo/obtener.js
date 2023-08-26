const puppeteer = require('puppeteer');
const fs = require('fs');

const baseUrl = 'https://www.duolingo.com/u/';

(async () => {
  const browser = await puppeteer.launch({ headless: "new" });

  const promises = [];
  const csvData = [];

  for (let i = 4000500; i <= 4001500; i++) {
    const url = baseUrl + i;
    const page = await browser.newPage();
    const promise = page.goto(url, { waitUntil: 'networkidle0' })
      .then(() => {
        const redirectedUrl = page.url();
        const rowData = [i, redirectedUrl];
        console.log(rowData.join(','));
        csvData.push(rowData.join(','));
      })
      .catch(error => {
        console.error(`Error al cargar la URL ${url}:`, error);
      })
      .finally(() => {
        page.close();
      });
    promises.push(promise);
  }

  await Promise.all(promises);
  await browser.close();

  const csvContent = csvData.join('\n');
  fs.writeFileSync('output.csv', csvContent, 'utf8');
  console.log('Archivo CSV generado exitosamente.');
})();