# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Alejandro Gómez Yepes
# Full terms: collection/LICENSE-CODE.txt
"""Verify and publish the exact collection to the GitHub Pages source branch.

Requires Git and GitHub CLI authenticated to the repository owner.
GitHub's built-in Pages workflow deploys this static branch without Jekyll.
No files in collection are rewritten. No force push is used.
"""
from pathlib import Path
import base64, json, os, subprocess, sys

root=Path(__file__).resolve().parent.parent
git='git'
gh='gh'
env=os.environ.copy()
env.update({'GIT_TERMINAL_PROMPT':'0','GCM_INTERACTIVE':'never'})

def command(args, data=None, allowed_failure=False):
    result=subprocess.run(args,cwd=root,env=env,input=data,capture_output=True,timeout=600)
    if result.returncode and not allowed_failure:
        raise RuntimeError(result.stderr.decode('utf-8','replace'))
    return result

def g(*args):
    return command([git,*args]).stdout.decode('utf-8').strip()

command([sys.executable,str(root/'scripts/verify_collection.py')])
identity=json.loads(command([gh,'api','user']).stdout)
assert identity['login']=='agyepes' and identity['id']==192377143,'Unexpected GitHub account'
head=g('rev-parse','HEAD')
assert g('symbolic-ref','--short','HEAD')=='main','Publish from the reviewed main branch'
manifest=json.loads((root/'collection/MANIFEST.json').read_text(encoding='utf-8'))
names=manifest['package']['expected_filenames']
for name in names:
    data=command([git,'show',head+':collection/'+name]).stdout
    assert data==(root/'collection'/name).read_bytes(),('Uncommitted collection file',name)
remote=g('remote','get-url','origin')
assert remote=='https://github.com/agyepes/power-electronics-interactive-html.git','Unexpected publishing repository'
token=command([gh,'auth','token','--hostname','github.com']).stdout.decode().strip()
assert token
for key in list(env):
    if key.startswith('GIT_TRACE') or key in ['GIT_CURL_VERBOSE','GH_DEBUG']:
        env.pop(key,None)
env.update({'GIT_CONFIG_COUNT':'2','GIT_CONFIG_KEY_0':'http.https://github.com/.extraheader',
    'GIT_CONFIG_VALUE_0':'AUTHORIZATION: basic '+base64.b64encode(('x-access-token:'+token).encode()).decode(),
    'GIT_CONFIG_KEY_1':'credential.helper','GIT_CONFIG_VALUE_1':''})
try:
    existing=g('ls-remote','--heads','origin','refs/heads/gh-pages')
    parent=None
    if existing:
        parent=existing.split()[0]
        g('fetch','origin','refs/heads/gh-pages')
        assert g('rev-parse','FETCH_HEAD')==parent,'Publishing branch changed during verification'
    entries=[]
    for name in names:
        entries.append('100644 blob '+g('rev-parse',head+':collection/'+name)+'\t'+name)
    for name,data in [('.nojekyll',b''),('.gitattributes',b'* -text\n')]:
        sha=command([git,'hash-object','-w','--stdin'],data=data).stdout.decode().strip()
        entries.append('100644 blob '+sha+'\t'+name)
    tree=command([git,'mktree'],data=('\n'.join(sorted(entries,key=lambda x:x.split('\t')[1]))+'\n').encode('utf-8')).stdout.decode().strip()
    argv=[git,'commit-tree',tree]
    if parent:argv+=['-p',parent]
    argv+=['-m','Publish verified collection '+manifest['collection']['version']+' from main '+head]
    commit=command(argv).stdout.decode().strip()
    g('push','origin',commit+':refs/heads/gh-pages')
    assert g('ls-remote','--heads','origin','refs/heads/gh-pages').split()[0]==commit
finally:
    env.clear();token=None
print(json.dumps({'sourceCommit':head,'pagesCommit':commit,'collectionFiles':len(names),'bytePreservation':True,'staticPublishingBranch':'gh-pages'},indent=2))
