from pathlib import Path
import hashlib
import json

O = Path(__file__).resolve().parent
R = O.parent
W = R.parents[1]
load = lambda p: json.loads(Path(p).read_text(encoding='utf-8-sig'))
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
approved = load(O / 'root-reviewed-snapshots.json')['lessons']
source = W / 'tmp/database-source/chapter-23.txt'
lines = source.read_text(encoding='utf-8').splitlines()
texts = {}
for name in ['AD51', 'AD66']:
    p = R / 'lessons' / f'{name}.md'
    assert sha(p) == approved[name], 'Direct source/current lesson rereview required'
    texts[name] = [x.strip() for x in p.read_text(encoding='utf-8-sig').split('\n\n') if x.strip()]


def anchor(name, needle, kind):
    found = [(i + 1, p) for i, p in enumerate(texts[name]) if needle in p]
    assert len(found) == 1, (name, needle, len(found))
    i, p = found[0]
    return {'path': f'lessons/{name}.md', 'lessonSha256': approved[name], 'kind': kind,
            'paragraph': i, 'exactOpening': p[:350]}


items = {
 '23.4': ('AD51', 'Catalog phải biết item', 'Một giá trị được ghi', '2. Dựng hai membership', '2. Ví dụ như gợi ý', 'Robustnessreplicationgoal andcatalogitem-versuspartitionplacementmetadata, dataaccessprotocolsnotjustbyteequality.'),
 '23.4.1': ('AD51', 'Hai điều kiện của register', 'Ví dụ 1: N=5', '5. Thiết kế model', '5. Chấp nhận trace', 'Linearizable read/write object totalorder andreal-timeorder,replicascanbestaleifreadsprotocolcorrect,orthogonaltransactionserializability,asyncbenefits/lag/ACKloss,networkpartitionversusfailureambiguity.'),
 '23.4.2': ('AD51', '§23.4.2 dùng quorum', 'Quorum locking vẫn có thể', '4. Với weights A=2', '4. Read tối thiểu', 'ReplicaS/Xlockingprotocolfamilies initiallywriteall,beforefailureextension; distinctfromatomicregisterGET/PUTprotocol.'),
 '23.4.2.1': ('AD51', 'Primary-copy đặt một nơi', 'Với n replica trọng số1', '7. Rejoin một replica', '7. Update121 không có', 'Exactlyoneprimarylockauthorityperitem,simpleunreplicated-stylecontrolbutfailurelockstate/accessibilityissue; authorityhistoryneededbeforeone-node reads.'),
 '23.4.2.2': ('AD51', '§23.4.2 dùng quorum', 'Quorum locking vẫn có thể', '1. N=7,W=4', '1. R nhỏ nhất4', 'Majoritycompatibilitylocks,2qrequest/grant+qunlockcost,basicwritesallreplicas,one-itemdeadlockandglobalreplicalockorderremedy; quorumintersectionproof.'),
 '23.4.2.3': ('AD51', 'Biased protocol cho S', 'Với n replica trọng số1', '4. Với weights A=2', '4. Read tối thiểu', 'ReadoneS/writeallXbiasandcost/failureavailabilitytradeoff,deadlockcomplexitynoteliminated.'),
 '23.4.2.4': ('AD51', 'Biased protocol cho S', 'Ví dụ weighted:', '4. Với weights A=2', '4. Read tối thiểu', 'Nonnegativeweights,Qr+Qw>S/2Qw>S,weightedintersectionproof,tradeoffandmajority/biasedspecialcases.'),
 '23.4.3': ('AD51', 'Read-one/write-all dưới', 'Đổi nó thành', '7. Rejoin một replica', '7. Update121 không có', 'Read-onewrite-allavailablefailsunderpartition/reconnectionwithoutprotocolchange; returnedstalenodecannotservereadsblindly.'),
 '23.4.3.1': ('AD51', '§23.4.3.1 thay bằng', 'Ví dụ A,B,C,D,E', '6. Năm replica:', '6. Read chọn version8', 'Lockedmajorityreadmaxversion,writemax+1underXprotection,majority-at-commit/2PCscope,stale-replicareintegrationandlimitationsparticipant/coordinatorfailure,replicamajoritynotshardmajority.'),
 '23.4.3.2': ('AD51', 'Giảm read quorum', 'Một biến thể trong §23.4.3.2', '5. Thiết kế model', '5. Chấp nhận trace', 'Read/writequorumtradeoff,read-anywrite-allfailurecost,primarynewestlog/uniqueauthority,consensuslogalternativeandchainheadwrites/tailreads/inflightreconfiguration.'),
 '23.4.4': ('AD51', 'Với cách cập nhật mọi', 'Reconfiguration thay membership', '7. Rejoin một replica', '7. Update121 không có', 'Permanentfailurecatalogremoval,rejoinlogcatchupwhilewritescontinue,finalprotectionapplydelta/catalogbeforeunlock; majorityversionexception,catalogconsistency/scalability andcrossconfigurationhistory.'),
 '23.6': ('AD66', 'Eventual convergence thường', 'Chi nhánh A ghi', '4. Thiết kế UI', '4. Có thể đợi replica', 'Replicationweakerconsistency/availabilitytradeoff explicitconditionsandcontractratherthanunqualifiedconsistencylabel.'),
 '23.6.1': ('AD66', 'BASE trong §23.6.1', 'Xét một register', '8. Một hệ luôn trả', '8. Availability trong lập luận', 'BASEdefinitions,CAPaslinearizable-registerimpossibilitywithindistinguishabilityproof,localoperationsduringpartition/conflictresolutionresponsibility,notmajoritycount-aloneguarantee.'),
 '23.6.2': ('AD66', 'Primary commit trước khi', 'Ví dụ primary ghi X', '5. Primary ghi sequence11', '5. Áp12 rồi11', 'Lazyversussync,guaranteeddurableorderedpropagation/outbox/topicspartitionorder,primarygranularity/updateanywhere,freshnessboundedrouting/safesnapshotcut,primaryfailureACKriskandstickysessionlimits.'),
 '23.6.3': ('AD66', 'Index/summary/materialized view', 'Ví dụ row ID7 chuyển', '5. Primary ghi sequence11', '5. Áp12 rồi11', 'Threeasyncmaintenanceconditions:completeidentifiedupdates,correctversioneddeltaunderconcurrency,eventualderivedstateandreaderconsistency;partitionmovescan duplicate/miss andsafecutnotlocal2PL.'),
 '23.6.4': ('AD66', 'Khi chỉ một node', 'Sau khi giải conflict', '6. Hai siblings có', '6. Lấy max thành', 'Singlewriter/read-onlycacheinvalidationversusmultiwriter,peritemvectorowncomponentincrements,equality/domination/concurrencycases,mergeparents+newresolverevent;metadataassumptionsandnotbusinessresolution.'),
 '23.6.5': ('AD66', 'Operation-based replication', 'Ví dụ giỏ hàng', '1. So vectors', '1. (4,1) và', 'Foreground/backgroundconflictdetection,application-specificreconciliation,commutingidentifiedoperationsversusadd/remove/physicalofflineeffects,negativebalancepolicy andmanualresolution.'),
 '23.6.6': ('AD66', 'Nguồn còn trình bày cách', 'Khi dùng để kiểm chống', '7. Trong cùng một leaf', '7. Multiset values', 'Bucket/keyhash/valuecommitment/fullbucketindex,canonicalaggregate,parentidentity/order,downwarddiffandO(mlogL)+leafpayload/skewcost,widebranchtradeoff,signed/trustedrootmembershipverification;sourceh1/h2/h3andSHA1errataexplicit.')
}
units = [u for u in load(O / 'source-section-inventory.json')['bookSections'] if u['chapter'] == '23']
rows = []
for i, u in enumerate(units):
    if u['section'] not in items:
        continue
    name, e, x, q, a, judgment = items[u['section']]
    end = units[i + 1]['sourceLine'] - 1 if i + 1 < len(units) else u['scopeLineEnd']
    rows.append({'section': u['section'], 'title': u['title'], 'owners': [name],
        'source': {'path': 'tmp/database-source/chapter-23.txt', 'sha256': sha(source),
                   'ownBodyLines': [u['sourceLine'], end],
                   'ownBodySha256': hashlib.sha256('\n'.join(lines[u['sourceLine'] - 1:end]).encode()).hexdigest()},
        'sourceReadEvidence': {'ownBodyRead': True, 'readBatches': [[937, 1102], [1103, 1259], [1454, 1604], [1605, 1758], [1759, 1901], [1902, 1999]],
                               'figurePagesVisuallyInspected': [1173] if name == 'AD66' else [],
                               'baselineCredit': False, 'scope': 'Directfullown-bodyandcurrentAD51/66comparison; no sourcecreditfor23.7/23.8orotherchapters.'},
        'semanticStatus': 'complete', 'contentComparison': judgment,
        'evidence': [anchor(name, e, 'teaching'), anchor(name, x, 'worked-example-or-algorithm'),
                     anchor(name, q, 'activity'), anchor(name, a, 'answer')], 'gaps': []})
assert len(rows) == 18
result = {'date': '2026-11-05', 'scope': 'ElevenAD51 and sevenAD66 sourceownbodies23.4/23.6 only.',
          'counts': {'assigned': 18, 'complete': 18}, 'units': rows,
          'checks': 'qa/replication-full-checks.json:14finitechecks,140quorumfixtures,729vectorpairs,256actualSHA256Merklefixturesandmembershippath;nocluster/signature/engineexecution.',
          'primaryDocsChecked': ['https://groups.csail.mit.edu/tds/papers/Gilbert/Brewer6.pdf', 'https://csrc.nist.gov/projects/hash-functions/nist-policy-on-hash-functions'],
          'sourceInterpretation': [
              'CAPsourceparagraphmixessequential-consistencyandACIDterminology;lessonusesprimaryGilbert-Lynchlinearizableobjectandoperationavailabilitydefinitions.',
              'Quorumintersectiondoesnotitselfimplementanatomicregister; lockingversionprotocolandregisterwrite-backexamplekeptdistinct.',
              'Merklesourcefigureusesinconsistenth2/h3labels,claimed8itemsdraws7,childIDsareprefixesnotambiguousnumericglobalIDs; authoredtreeusesfixed8leaveswithdomainseparatedorderedhashes.',
              'Sourcevalue-onlycollectionhashcanmisskey/valuepermutationinabucket;authoredencodingcommitskey/value/versionandbucket/pathidentity.',
              'SourceSHA1exampleishistorical;actualauthoredhashcheckusesSHA256anddoesnotclaimtoverifydigital signatures.'
          ]}
(O / 'semantic-replication.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
print('Replication source units', len(rows))
