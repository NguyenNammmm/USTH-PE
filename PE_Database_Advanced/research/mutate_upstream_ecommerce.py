"""Expose vacuous upstream oracles without modifying upstream source files."""
from pathlib import Path
import json,sys
B=Path(__file__).resolve().parent;WORK=B.parents[2];CLONES=WORK/'tmp/database-advanced-repos'
(B/'repo-checks').mkdir(exist_ok=True)
sys.path.insert(0,str(CLONES/'vendor'));sys.path.insert(0,str(CLONES/'ecommerce-query-optimizer-demo/src'))
import pytest
class EmptyResults:
 @pytest.fixture(autouse=True)
 def erase_outputs(self,monkeypatch):
  import queries
  monkeypatch.setattr(queries,'filter_products',lambda *a,**kw:[])
  monkeypatch.setattr(queries,'search_products',lambda *a,**kw:[])
  monkeypatch.setattr(queries,'user_order_history',lambda *a,**kw:[])
result=pytest.main([str(CLONES/'ecommerce-query-optimizer-demo/tests'),'-q','--basetemp='+str(CLONES/'pytest-mutant-work')],plugins=[EmptyResults()])
out={'mutation':'All three query helper functions return [] unconditionally; SQL constants remain unchanged.','upstreamSuiteExitCode':int(result),'meaning':'A zero exit code means the upstream tests did not detect these broken helper functions. This motivates the PE independent oracle, not accepting all upstream tests as adequate.'}
(B/'repo-checks/upstream-ecommerce-mutation.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
