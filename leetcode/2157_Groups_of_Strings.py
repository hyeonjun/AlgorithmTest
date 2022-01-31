from collections import Counter
class Solution:
    def groupStrings(self, words: list[str]) -> list[int]:
        n = len(words)

        words = ["".join(sorted(w)) for w in sorted(words, key=lambda x: len(x))]

        parent = list(range(n))

        def find(n):
            if parent[n] == n:
                return n
            parent[n] = find(parent[n])
            return parent[n]

        def union(a, b):
            a, b = find(a), find(b)
            if a < b:
                parent[b] = a
            else:
                parent[a] = b

        table = {words[i]: i for i in range(len(words))}  # words index
        visited = {}

        for i, word in enumerate(words):
            if len(word) == 1:  # 길이가 1이면 같은 길이 1은 모두 연결 가능
                union(i, 0)
                continue
            if table[word] != i:  # 같은 문자
                union(i, table[word])
                continue
            for j in range(len(word)):
                w = word[:j] + word[j + 1:]  # 문자 하나 삭제
                if w in table:
                    union(i, table[w])
                if w in visited:
                    union(i, visited[w])
                else:
                    visited[w] = i
        parent = [find(i) for i in range(n)]
        answer = Counter(parent)
        return [len(answer), max(answer.values())]


solution = Solution()
print(solution.groupStrings(["a","b","ab","cde"]))

text = ["xsgrqznel","zy","yk","qdpoijn","sgcevyinq","m","gfencukmaiohbw","vf","xucfho","ewqrtk","kvtbcnzwyqusper","qkbmo","df","ic","jlbfxu","hcdkxspqu","bthluwdy","epzrg","vfyuxlazsmqkoj","pmuyiqnljdgr","dqcgrsuhnw","eujcordq","neirphybmdj","emhbnkvd","o","f","cjfwdbqlna","hxofjbmplrkvws","qfjlnkouxea","tiwcguvqnk","rnwjtm","qbpyuhtalwi","qs","vawlbkp","mvhfgbxwpy","wxqnpybocldmghv","cz","hdtk","h","snbkyrxvocl","oqrhbxjwslkczat","tfbzesgrmxjhpo","ebflnptqjuymaz","wuapyhkfidtbj","dimjq","xtjnmyfie","rg","qstjxw","kvzjobspxaq","cfusjbmdxyn","pnmh","nqkvm","vd","qlmvhaobxscj","tbsacwrqjvmiez","b","terzxvjbsnlahi","fyksj","cn","qi","qbilgophxz","lroeqf","wzorubxqaimydf","qrxfstophynlb","vcpjhg","tcdljo","bjftgakuicvers","pjckyvgxwd","chuqwfjvzdkmny","ltvwmbo","dehxajgkruoc","prhcdkubmfvi","lsca","btnhaxyzg","rbeyzqo","lhcd","rjqlkwycous","sidbtalx","xsdlqfbemzjg","g","j","er","xr","mtebgwoundsz","desrzflgb","rdacmnbwktzh","dhtsipjenl","h","cajfihzxvbm","esjnrf","zwldiuomcqh","bjzwnpvh","tywrh","olchpugdxwktqs","xsoydzt","jdeknm","avgoyne","jbchopakq","xo","tuenhryzvl","sxhmblpkud","xmtezwqsglkuny","iqwgpxcrm","ngtjxldckfib","hyj","j","efygxmqzo","kbhvructy","n","nsdtguzr","dpomkierl","pz","fybsnv","kbs","amzflkrqpustob","qjinbtxyhvf","s","lowpevqai","ng","gbq","qa","fakeqlspvm","agoihubckqpe","qitbu","xmud","vxbemrfnpsu","bthd","icvszbrkqowg","gsy","qlbtnydakcomj","yehr","isdevbtfj","uybrepaz","czwxnriekq","xfh","oh","mv","cbdvrwegtzos","oljuhzabgn","cyjukdaxnfrv","eigopwxyarnjd","vaioetdhyxjmq","ozfrah","lwmcjpsub","vlxdimprea","wc","hqjlfzyga","vgjnmbu","uskrlmaovg","hodurfpcnljbe","erantguib","bsyqwpe","ceoszfb","jioraw","isoetbavyjnpwqg","uydjgm","bycklfdtwonqjsm","yvxtr","dvmcotwkl","wz","wftjrymx","vb","sr","uozc","aobqdn","pcyzrhna","nxghatvesplb","hon","wxghdmczsfentaj","nh","telcwryxgpmbaki","ejdairchlfubgnz","xkbteuhszwn","twkdiaqbcmp","rkzgquehfv","gawtp","jupzlmotahd","bpcamwtsyzkgjr","rqhxj","lzei","vceyjwoautsfn","zbqryoctxhw","zr","tzfkiuvmrchex","dfpxny","urjyisnd","pkqxlchoifwut","e","zorwincxmhvabks","gheyvwl","dv","bmneaupgfwyvk","rtbgnfmlpwezvdh","vobwsh","lm","ihzre","lcqx","hltjbaofnirpkqe","mnwguxjrok","vztxlmgr","pjcaudey","zu","dumsh","vyawij","r","kasdqjow","fygbxcqurhtpmzi","wqpchufjimrk","knotgfrdpvzi","xsckbilvngpr","wvuxmylkrcp","cphxrywvqb","grol","sgx","t","ehsglmtwou","vhbgzqopxjs","sfu","nl","enbduyahkgr","fdiwqrkcxepobt","sorycnhgw","tfzupnsgyadchj","ybvtfoljhcrqzxa","iek","xoepzblswa","h","xpvglfir","lrkavotxwqbsfp","yelwtdfirxc","yqmfwvcuthbjrs","jtwydkclhpr","uhjzcw","sq","cpdiutomye","obauxqkptmv","rqxcbnlvgy","kx","pimdjnvqawelfht","okxchfd","tzcfpgjnoydrqk","wfbchxtoaslyge","bidoznvgre","qa","vo","z","fixbshrjgwlukc","kys","rfnxdaqwemoku","vlcbnzkjdu","pxcnkthjuo","jvneowk","dbjuyna","xzms","onimdjafpywthcu","gtlq","b","timldacy","rqibohpfn","sbrmncopl","teulxjwocnpfmd","bgesqofc","rgihaeuvbtqwxsp","ytfqvkgdpalcwos","hzswoxudjynti","ysqfkbcoaevdt","kgylrwixvhpufj","sdljhzqrew","oetgkxcuqszlm","jwqo","rpxgdyltscem","gbps","bzkjlfhedqow","oqructwf","xflmqutnakvs","ifltcujwgdnq","qrjoy","zgbkrnayiqm","vmdflxhbkrjzcpa","brdfjz","ybzl","kafrzvgi","ukgievpfwysdxht","g","xmd","gob","rbugxvj","cmujo","wipoldcryjtguv","lwr","lpso","z","azlqnmuwtgdeypv","dtrjogxiehav","swucyq","wfzpxvr","rlg","m","cqsteouydag","uedblvogsnzqjw","lbjhgkdmpafenvr","uc","nfpbjqrmakx","z","pizhqxcktl","ptz","jwtm","kwcgsmvju","bu","kpgnts","myedtiv","czhqeksgmiwavpx","balfes","qtvlaywzfm","wrkjfvtyuxe","nlmbjshuey","ilwdfkz","shyrtdbfp","qonzei","gmlhtxy","wqn","ozubsndlcaq","kolh","ec","dpkwharimlt","bcslveydjazfm","u","eyupasolhm","zyhgua","okesmyliz","kloty","jvzdhqbntaes","ajsn","e","yxjpqhgelictak","gphsxyaobrfi","aqxoel","ob","igvn","mewhgxkrzjsacoq","cznrta","hlpxs","g","dwujic","kisobxwedva","cmsbyjhfzr","jsi","nifpuadmglxyj","zqtiopvydkl","ykazbpoqdt","ehra","rsh","qmxnjve","mjdnevub","widltpchvsqj","rdleyfiwm","pnojberkgtzaqsx","dcfeytu","oshpnqfjgd","nqpzlhktwcfreyx","ea","iscojwk","kaqbmpscliuznyo","ik","szgbiqldm","zokbpqeanjigmd","xwynvidpauqeb","kcgdn","bogecpwkrhs","ebjyzocdmf","aplxv","skydjpwcqobrgt","tyohmeviqzbsa","hidfuyxwzvrol","qr","urqsvpihdezgyj","xgtapi","ex","fnqzdvwlparshc","aonmk","mjxsvf","nvbtshyludcfikq","mkgfjeypxuwqbaz","ykh","zdyevmgw","uoihtq","nxluw","y","ckretvjihg","skxqrdzfhnji","bctqnfakhiwy","fbcidznyrghwko","tehngdcxskwif","uhbkteoz","lajnwedyirfuxh","qfskpxmlcvg","ny","zdsvolmtcignqey","borjtufaz","el","uegqcapdjkw","exfatpqdhyrw","qu","dwolzpcu","pxzmj","gbjosynv","atg","hcurgaeisnb","vnqtw","fteypzhogku","mkbsndy","cusx","zrhkxawesp","uhj","wbekzotrnsfxl","xi","tuxh","atkpfwb","j","to","npwsuzkbr","afozpnkjb","lhdrfkmtzjives","g","l","qrnp","xokqi","swqrtmofkcy","pltqrayvhsmnzb","rnusqme","pg","u","vcuoksf","potmc","z","z","yikwclu","fgeqamscvxjy","sozmctlkbrn","xudkc","vfclegih","kwljfa","pcaiwbvenhtsoxq","rnsuvydizc","crqaudvtiz","ztn","vnorpcd","xqntzjosimpkdue","feyn","dwblmj","sqvepk","owblcikqyt","h","yfkpsivtqjrax","vfsardnejxqgmbo","vhqbfi","ptqvlhfwajrcmdz","ulksnmjrxf","nmowlrp","tidglc","dzintjvymbxphl","c","xkwpdaqsot","jzlcbghsxvdpry","uips","aliykzrgvom","vbcjezrlktfihd","srwc","csieramlthfbw","mbw","hbcal","nrdam","o","asxuvch","vntxmya","oikcesbvtg","t","pkgdwusoaml","ileohznaykqu","pan","hmgxb","m","roslevxhndc","l","viegpuat","sdeqjthrcuxyg","bfukpgneawl","ogyrpdlekjhb","objdp","mqtrezahf","rcnytu","etlgchqjxour","wlfbeaiznjstqy","vh","rwebumvxypdigh","gouvcknwsfb","lkwzycsbfmpt","qyxmczsuvnlgfd","tumgcfqiolyew","xd","v","cxirbmwvfueg","ubsitqeyrmvoklg","okfgiuyhqdwlxb","qao","vqcpbjnso","zilesa","ljficq","obn","q","ukxwa","uxwvlm","dpsbmnwxfe","htjlpmuicn","fo","vtzpqclhukgfnj","kd","kzfjp","jymf","lucxwf","yh","dgmpswviyfxubtr","tvprzh","lbxpwumzskgoie","gofriqpkzcjlnhe","gfnitulkdv","wnqxszuh","kpzaqhoi","efksj","ajqx","fvqlx","dfxitr","hyowcrme","hjxzvrycapwke","jeqasvhlk","tol","xf","ufaicyd","njmfblorexszhci","jyxrdb","yst","mfpotuqr","jixkncpztm","pjqenbmaoudyxcr","iwncvf","hornilmegvfcqtb","u","xlmpsqar","rspwijhzkqucme","kgijfoq","hvncxaer","pqh","qsnmzfkv","puyov","vlqo","bues","olpdhuvrs","khjt","wxsapzudmgcjny","kzbilygxpfrmsu","cbuos","yvshwfrnqckt","wvyia","tpnauwblx","zpavuxkjimdgylh","m","apkzrvuhne","x","sviz","byrncofv","wmtuchz","vwjrbfxln","aztuen","qia","qoazsrbkpnyvw","uz","sqflvmnrcdjo","fvhtus","cyzkrdpmafeut","il","xockn","gw","atxr","tj","bqphtlyf","syvfxmw","us","nkrhz","ujzyvps","tnibdfskjgprw","gvo","fkj","xvqodkazisbepu","fu","yimstcknrqowdvx","iagenfrwdxvqozm","t","ecfbyxdl","npsqrkdbew","byfzlter","qysvfwokgrbex","ogfdranskxtlbmu","t","doqn","uvfyqtlioperczs","nu","ahvdlixubr","wetjfhk","cbomgetrz","zuqle","qmu","lmesdnizva","eubjsyoipghv","ewxbvzafml","nxqyoabzvflsmr","ynicvzd","xoefsigclabnkp","rd","wskmcipz","esyntl","jmtprywxulgab","jobegzqnrlau","helq","nzrwjexgtmi","nqshpzau","vtharwbiszu","qopgdrhlmwuejs","amgwvqiul","rxmpyflsv","bzxvryulj","dgboxlfukcaw","eb","inajdykeqxrzolg","umwxeiar","xbwfo","htmrsgxwzdocjk","clxhenyiz","mahwipfqcn","pbsqtlfcmei","c","nlvkruxbsi","stlpmvqeyg","cbjyxtafsn","oarzin","bfiovyjp","pcwgtoyn","rydcg","ghomx","fishoclwmdxt","yexuvlzd"]
print(solution.groupStrings(text))
