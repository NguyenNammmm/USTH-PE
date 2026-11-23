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
for name in ['AD50', 'AD65']:
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
 '23.1': ('AD50', 'Transaction chỉ truy cập', 'Đơn hàng nằm ở siteA', '4. Tự lập trace', '4. Rubric kiểm', 'Local/global transaction ACID and independent node failures; local correctness not global atomicity.'),
 '23.1.1': ('AD50', 'Transaction chỉ truy cập', 'Mô hình chương23', '4. Tự lập trace', '4. Rubric kiểm', 'Per-node local TM log/concurrency/recovery and initiating TC start/subtransactions/global outcome; shared-memory common-failure/log exception.'),
 '23.1.2': ('AD50', 'Xét coordinator C', 'Ví dụ thứ ba:', '3. Thiết kế message', '3. Giữ business', 'Node/message/link/partition failures and TCP versus transaction outcome; crash-recovery rather than Byzantine assumptions.'),
 '23.2': ('AD50', 'Atomicity yêu cầu', 'Đơn hàng nằm ở siteA', '4. Tự lập trace', '4. Rubric kiểm', 'All-node atomic outcome and validity/safety versus conditional termination; commit protocol role.'),
 '23.2.1': ('AD50', 'Bất biến safety:', 'Ví dụ thứ nhất:', '1. Một participant', '1. Sau YES', 'Two phases, durable promise/outcome, unanimous readiness, safety invariant under durable identity/authority.'),
 '23.2.1.1': ('AD50', 'Trong phiên bản sách', 'coordinator:\n', '1. Một participant', '1. Sau YES', 'Force coordinatorprepare, force ready with local log beforeYES, durable commit/abort beforedecisionmessages; timeoutauthority, ACK/complete and forgetting.'),
 '23.2.1.2': ('AD50', 'Các nhánh recovery', 'Ví dụ thứ hai:', '2. P1 đã prepared', '2. Hai trường hợp', 'Participant and coordinator failure cases, outcome/no-ready/in-doubt evidence and query-status, partition blocking and indistinguishable local observations.'),
 '23.2.1.3': ('AD50', 'Nếu restart phải chờ', 'Ví dụ U prepared', '5. Node restart', '5. Local recovery', 'Ready includeswrite-locklist; localrecovery then reacquireprotection beforeadmission; nonconflictingtransactionscontinue whileindoubt/conflictingonesstillblock.'),
 '23.2.2': ('AD50', 'Nhóm lưu decision bằng', 'Một majority D còn', '5. Node restart', '5. Local recovery', 'Consensusdecisiongroup distinct from2PCparticipants; recover chosenoutcome,otherwisecollectvotes/repropose,onechosenoutcomedespiteoldrequests; majoritylivenessconditions/minorityblocking;3PCassumptions.'),
 '23.2.3': ('AD50', 'Protocol trong §23.2.3', 'Ví dụ outbox42', '6. Receiver gửi ACK', '6. Inbox42 chưa bền', 'Cross-org autonomy, four-part durableoutbox/inbox protocol,receivercommitbeforeACK,atomicbusiness+processed,dedupretention/cutofftradeoff,workflowexceptions/compensation and logicaleffectonce scope.'),
 '23.3': ('AD65', 'Trong mô hình message', 'Ví dụ 1: T1 giữ', '1. Vẽ local', '1. A:T2→T1', 'Distributed extension assumesatomiccommit; separates unreplicated/singleversion base fromreplica/MVextensions.'),
 '23.3.1': ('AD65', 'Centralized lock manager', 'Ví dụ 1: T1 giữ', '1. Vẽ local', '1. A:T2→T1', 'Lock authority distribution and global2PLboundary; managersnotmerelyindependentlocalprotocols.'),
 '23.3.1.1': ('AD65', 'Trong mô hình message', 'Centralized lock manager', '1. Vẽ local', '1. A:T2→T1', 'Singlemanagerrequest/grant/unlockmessaging,simpledeadlockgraph,bottleneck/failure/recoveryauthoritytradeoff.'),
 '23.3.1.2': ('AD65', 'Trong mô hình message', 'Ví dụ 1: T1 giữ', '1. Vẽ local', '1. A:T2→T1', 'Per-itemlocalmanager,similarremotemessagecost,distributedloadwithglobaldeadlockdespiteacycliclocalgraphs.'),
 '23.3.2': ('AD65', 'Collector có thể nhận', 'Ví dụ cụ thể ngoài', '5. Collector còn', '5. Collector thấy', 'Lockorder/waitdie/timeout extensions,localgraphunion/globaldetector,realversusconstructedgraph,stale-falsecycleglobal2PLcaveat,distributedabortandunnecessaryconcurrentvictims.'),
 '23.3.3': ('AD65', 'Lease chỉ áp khi', 'Trong cách dùng clock', '6. Thời gian thật', '6. Trường hợp đầu', 'Expiry/renewACK/faulttolerantauthority,clockuncertainty/action+deliverybounds/late-rejection/fencing;preparedwriteprotectionnotrevocablebytimer.'),
 '23.3.4': ('AD65', 'Distributed TO dùng', 'Ca numeric: site A', '2. Dùng logical', '2. Send mang', 'Globallyuniquetimestamp specifies sharedserializationorder; no localclock reinterpretation.'),
 '23.3.5': ('AD65', 'Một timestamp server', 'Clock gần đồng bộ', '2. Dùng logical', '2. Send mang', 'Centralcounterversusdistributedcounter,node/threadties leastsignificant,successiveuniqueness,physicalsyncversusLamportadvance,slow-clockrestartstarvation.'),
 '23.3.6': ('AD65', 'Mỗi site có thể làm', 'Clock gần đồng bộ', '9. A giữ R(X)', '9. T20 đọc X được', 'LocalRWtimestampchecks withsameglobalTS,slowcounterretrycost,dirtyreadcommitdependency/readwaitincludingprepared2PCandMVTOextension.'),
 '23.3.7': ('AD65', '§23.3.7 còn có', 'Ca numeric: site A', '8. Site A đã bắt đầu', '8. A phải rollback', 'Full5distributedvalidationrules:globalvalidationTS,abortlatepredecessor,locallycomparablestart/finish,validatebeforeprepare,commitonlyglobaloutcome;oldreadpreparedconflict and weakeratomicversionguard.'),
 '23.5': ('AD65', 'Multiversion 2PL có thể', 'Ban đầu x ở A=100', '3. Với clock interval', '3. Chọn tc206', 'MV2PL/globallyconsistenttime,distributedSI andfederation are separateextensionswithdifferentguarantees.'),
 '23.5.1': ('AD65', '§23.5.1 còn xét', 'Ví dụ 3: lúc chọn', '3. Với clock interval', '3. Chọn tc206', 'Centralcommitcounterbottleneck,perfectclockidealizationversusuncertainty/commitwait,lockintervalserializationargument,externalorder,safetime/pendingcommitreads andearliersnapshotfreshnesstradeoff.'),
 '23.5.2': ('AD65', 'Distributed snapshot isolation', 'Ví dụ T ghi cả x', '7. Dựng graph A/B', '7. Ở A, L đọc', 'Independentlocalsnapshotscanreadpartialglobaltransaction;coordinatedvisibility/WWvalidationneeded;SIstillnotserializable,sourceomitsfullimplementationandlessonkeepsscope.'),
 '23.5.3': ('AD65', 'Một kỹ thuật trong', 'Ngay cả global requests', '7. Dựng graph A/B', '7. Ở A, L đọc', 'Autonomouslocal/globaltransactions,localserializableinsufficiencyevensequentialglobalworkoriginal3txcycle,ticketdirectconflict/orderwithtransactioncontrol andcapabilitylimits.')
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
        'sourceReadEvidence': {'ownBodyRead': True, 'readBatches': [[1, 145], [146, 306], [307, 444], [445, 556], [557, 718], [719, 859], [860, 936], [1260, 1395], [1396, 1453]],
                               'figurePagesVisuallyInspected': [1128, 1131, 1138] if name == 'AD50' else [1142, 1144, 1146],
                               'baselineCredit': False, 'scope': 'Direct source own bodies and full currentAD50/65; no credit for otherchapter23sources.'},
        'semanticStatus': 'complete', 'contentComparison': judgment,
        'evidence': [anchor(name, e, 'teaching'), anchor(name, x, 'worked-example-or-algorithm'),
                     anchor(name, q, 'activity'), anchor(name, a, 'answer')], 'gaps': []})
assert len(rows) == 24
result = {'date': '2026-11-05', 'scope': 'TenAD50 and fourteenAD65 own-body units23.1–23.3/23.5 only.',
          'counts': {'assigned': 24, 'complete': 24}, 'units': rows,
          'checks': 'qa/distributed-commit-lock-full-checks.json:18checks,2448finite2PCstates and actual sequentialSQLiteinbox/outboxfixture; noXA/clock/distributedengineexecution.',
          'sourceInterpretation': [
              'Persistentmessagingdeliversrepeatednetworkmessages butonecommittedlocaleffectunderatomicdedup;externalAPIsnotautomaticallycovered.',
              'Cutoffdedupretentionwithrejectingoldmessages changesdeliveryacceptance; cannotbothforgetIDsandacceptarbitrarilylateduplicateswithoutotherevidence.',
              'Falsecycle release-then-acquireexample is qualified outsideglobal2PL; local serializability federationexample is not claimed strict2PL/nativeexecution.',
              'Consensusreplicatingdecisiondoesnotremoveunanimousparticipantreadinessorunconditionallivenessunderasynchrony.'
          ]}
(O / 'semantic-distributed-commit-lock.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
print('Distributedcommit/locksourceunits', len(rows))
