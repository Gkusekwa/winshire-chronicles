const fs=require('fs'), path=require('path'), {chromium}=require('playwright');
// Run from the repo root: npm i @fontsource/im-fell-english @fontsource/im-fell-english-sc playwright; node Tools/art/cover_layouts/render.js
const R=process.cwd()+'/';
const P=R+'Tools/art/cover_layouts/';
const ED=R+'Covers/Art/';
const blobs={e7c94179e269b0767476f7d35e8448a3:'bone/book1.svg','7a6983dcfe063bb0b05c65c0a1f75690':'bone/book2.svg','53b23d2d5dcad9536912a284727abe0a':'bone/book3.svg',
 '4cba7997192fcc8e1d2ac7b99b5e31bf':'night/book1.svg','240a8d0d8b0b386c7c5c729be73468b4':'night/book2.svg','6acd76d2c6628758f363dccf01b31667':'night/book3.svg',
 '612a58c9a9c07a75cfd835692aff80bb':'band/book1.svg','4a5990fb44006957398c9a5610c16059':'band/book2.svg','c101e8a23ba01e72c0db1e5ee1cfa783':'band/book3.svg'};
const F=R+'node_modules/@fontsource/';
const css=`@font-face{font-family:'IM Fell English';src:url(file://${F}im-fell-english/files/im-fell-english-latin-400-normal.woff2)}
@font-face{font-family:'IM Fell English';font-style:italic;src:url(file://${F}im-fell-english/files/im-fell-english-latin-400-italic.woff2)}
@font-face{font-family:'IM Fell English SC';src:url(file://${F}im-fell-english-sc/files/im-fell-english-sc-latin-400-normal.woff2)}body{margin:0}`;
const boards={'Main':['bone',1],'Bone-2':['bone',2],'Bone-3':['bone',3],'Night-1':['night',1],'Night-2':['night',2],'Night-3':['night',3],'Band-1':['band',1],'Band-2':['band',2],'Band-3':['band',3]};
const bands={1:'#1F3D3B',2:'#6B2A1A',3:'#222B45'};
(async()=>{const b=await chromium.launch();const pg=await b.newPage({viewport:{width:800,height:1280},deviceScaleFactor:2});
for(const [f,[ed,n]] of Object.entries(boards)){
  let s=fs.readFileSync(P+f+'.dc.html','utf8');
  let body=s.split('<x-dc>')[1].split('</x-dc>')[0].replace(/<helmet>[\s\S]*?<\/helmet>/,'');
  body=body.replace(/\/_blob\/([0-9a-f]{32})/g,(m,id)=>'file://'+ED+blobs[id]).replace('{{band}}',bands[n]);
  const html=`<!doctype html><html><head><meta charset="utf-8"><style>${css}</style></head><body>${body}</body></html>`;
  const tmp=path.join(require('os').tmpdir(),'winshire_cover.html');fs.writeFileSync(tmp,html);
  await pg.goto('file://'+tmp);await pg.evaluate(()=>document.fonts.ready);await pg.waitForTimeout(300);
  const names={1:'The Watch Below',2:'The Hunt Beneath',3:'The Titan War'};const E=ed[0].toUpperCase()+ed.slice(1);
  fs.mkdirSync(R+'Covers/'+E,{recursive:true});
  await pg.screenshot({path:R+`Covers/${E}/Book ${n} - ${names[n]}.jpg`,type:'jpeg',quality:92,clip:{x:0,y:0,width:800,height:1280}});
}
await b.close();})();
