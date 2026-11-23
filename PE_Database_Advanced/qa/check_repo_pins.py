from pathlib import Path
import hashlib,json,subprocess
R=Path(__file__).resolve().parents[1];W=R.parents[1]
git='C:/Users/HOME/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/git/cmd/git.exe'
registry=json.loads((R/'research/repo-registry.json').read_text(encoding='utf-8'));checks=[]
for repo in registry['repos']:
 folder=W/repo['clonePath'];head=subprocess.check_output([git,'-C',str(folder),'rev-parse','HEAD'],text=True).strip()
 checks.append({'repository':repo['repository'],'kind':'pinnedHEAD','actual':head,'expected':repo['commit'],'passed':head==repo['commit']})
 for item in repo['sourceFiles']:
  actual=hashlib.sha256((folder/item['path']).read_bytes()).hexdigest()
  checks.append({'repository':repo['repository'],'kind':'selectedSourceFile','path':item['path'],'actual':actual,'expected':item['sha256'],'passed':actual==item['sha256']})
result={'scope':'Read-only provenance freshness of four pinned clones/selected files. Does not rerun repository or course tests.','passed':sum(c['passed'] for c in checks),'total':len(checks),'checks':checks}
(R/'qa/repo-pin-freshness.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps({'passed':result['passed'],'total':result['total']}));assert result['passed']==result['total']
