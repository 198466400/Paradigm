import readline from 'readline';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
const __dirname = path.dirname(fileURLToPath(import.meta.url));
const KEY = process.env.MISTRAL_API_KEY;
if (!KEY) { console.error('ERROR: set MISTRAL_API_KEY'); process.exit(1); }
const LOG = path.join(__dirname,'..','logs');
if (!fs.existsSync(LOG)) fs.mkdirSync(LOG,{recursive:true});
const logFile = path.join(LOG,'session-'+new Date().toISOString().replace(/[:.]/g,'-').slice(0,19)+'.jsonl');
const log = (r,c) => fs.appendFileSync(logFile, JSON.stringify({ts:new Date().toISOString(),role:r,content:c})+'\n');
const p = (c,t) => `\x1b[${c}m${t}\x1b[0m`;
async function ask(system, user) {
  const r = await fetch('https://api.mistral.ai/v1/chat/completions',{
    method:'POST',
    headers:{'Content-Type':'application/json','Authorization':`Bearer ${KEY}`},
    body:JSON.stringify({model:'mistral-small-latest',messages:[{role:'system',content:system},{role:'user',content:user}],max_tokens:150})
  });
  if (!r.ok) throw new Error(`Mistral ${r.status}`);
  return (await r.json()).choices[0].message.content.trim();
}
function sev(msg) {
  if (/emergency|crisis|suicide|danger/i.test(msg)) return ['HIGH','31'];
  if (/scared|alone|overwhelmed|struggling/i.test(msg)) return ['MEDIUM','33'];
  return ['LOW','32'];
}
async function run(msg) {
  log('input', msg);
  const [level, color] = sev(msg);
  process.stdout.write(p('90','  [Angell] '));
  const angell = await ask('You are Angell, constructive stabilizing agent. Find what is safe and supportive. Under 60 words.', msg);
  console.log(p('32', angell));
  process.stdout.write(p('90','  [D3min]  '));
  const demin = await ask('You are D3min, adversarial critical agent. Find risks and challenge assumptions. Under 60 words.', msg);
  console.log(p('31', demin));
  const out = await ask('You are Herald, constitutional AI mediator. Synthesize Angell and D3min into one honest human-centered response. Under 80 words. Lead with the human need.', `MESSAGE: ${msg}\nANGELL: ${angell}\nD3MIN: ${demin}`);
  console.log('\n'+p('36','┌─ HERALD ──────────────────────────────'));
  console.log(p(color,`│  SEVERITY: ${level}`));
  console.log(p('97',`│  ▶ ${out}`));
  console.log(p('36','└────────────────────────────────────────')+'\n');
  log('output',{angell,demin,out,level});
}
const rl = readline.createInterface({input:process.stdin,output:process.stdout});
console.log(p('36','\n╔══════════════════════════════════════╗'));
console.log(p('36','║ ')+p('97','HERALD-LITE v3.0')+p('90',' · i.c. snow       ')+p('36','║'));
console.log(p('36','╚══════════════════════════════════════╝\n'));
const prompt = () => rl.question(p('36','HERALD > '), async i => {
  const msg = i.trim();
  if (!msg){prompt();return;}
  if (msg==='quit'){rl.close();return;}
  try { await run(msg); } catch(e){ console.error(p('31',`  [ERROR] ${e.message}`)); }
  prompt();
});
prompt();
