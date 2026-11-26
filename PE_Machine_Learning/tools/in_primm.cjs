/* In toàn bộ giáo trình, kể cả những phiếu đang ẩn trên màn hình. */
const fs = require('node:fs');
const path = require('node:path');
const { pathToFileURL } = require('node:url');
const { chromium } = require('playwright');
const target = path.resolve(__dirname, '../docs/PRIMM/Machine-Learning-PE-PRIMM');
async function main() {
  const chrome = process.env.PE_CHROME || ['C:/Program Files/Google/Chrome/Application/chrome.exe','C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'].find(fs.existsSync);
  const browser = await chromium.launch({headless:true,...(chrome?{executablePath:chrome}:{})});
  try {
    const page = await browser.newPage();
    await page.goto(pathToFileURL(target+'.html').href,{waitUntil:'load'});
    await page.emulateMedia({media:'print'});
    await page.locator('.terms,.repairs').evaluateAll(items=>items.forEach(item=>item.open=true));
    await page.evaluate(()=>document.fonts.ready);
    await page.pdf({path:target+'.pdf',format:'A4',preferCSSPageSize:true,printBackground:true,
      displayHeaderFooter:true,headerTemplate:'<span></span>',
      footerTemplate:'<div style="font:8px Arial;color:#47615b;width:100%;margin:0 16mm;display:flex;justify-content:space-between"><span>PROGRAMMING EDUCATION · MACHINE LEARNING</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>',
      outline:true,tagged:true});
    console.log(target+'.pdf');
  } finally {await browser.close();}
}
main().catch(error=>{console.error(error);process.exitCode=1;});
