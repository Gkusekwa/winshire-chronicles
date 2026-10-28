"""Split a chapter into ElevenLabs Eleven v4 passages (about 2,400 characters, on paragraph boundaries).

Audio tags come from the annotations; a [calm] tag resets the delivery after a tagged paragraph,
because v4 holds a tag until the next one. Invented names are written as /IPA/ from names.py.
Scene breaks become [long pause]; heavy paragraphs end with [pause].

    python3 elevenlabs_v4_passages.py 5        # writes Book 1/audiobook/ElevenLabs/production/text/ch05_NN.txt
"""
import json,re,sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from names import NAMES
import render_elevenlabs as R
ipa={n:p for n,_,p,a,st in NAMES if a or st=="confirm"}
rx=re.compile(r"\b("+"|".join(sorted(map(re.escape,ipa),key=len,reverse=True))+r")\b")
RESET="[calm]"
def chunks(n,limit=2400):
    segs=json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "Book 1", "audiobook", "Performance", f"{n:02d}.json")))["segments"]
    paras=[];last=None;tagged=False
    for s in segs:
        first=s.get("para")!=last or s["type"]=="title"; last=s.get("para")
        tag=R.tag_for(s,True,first)
        txt=rx.sub(lambda m:"/"+ipa[m.group(1)]+"/",s["text"])
        if first:
            if not tag and tagged and s["type"]!="title": tag=RESET+" "
            tagged=bool(tag) and tag!=RESET+" "
            paras.append(tag+txt)
        else:
            if tag: tagged=True
            paras[-1]+=" "+tag+txt
        p=s.get("pause_after_ms",0)
        if p>=1600: paras[-1]+=" [long pause]"
        elif p>=800 and s["type"]!="title": paras[-1]+=" [pause]"
    out=[];cur=""
    for p in paras:
        if cur and len(cur)+len(p)+2>limit: out.append(cur);cur=p
        else: cur=cur+"\n\n"+p if cur else p
    out.append(cur); return out
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","..","Book 1","audiobook","ElevenLabs","production","text")
if __name__=="__main__":
    os.makedirs(OUT,exist_ok=True)
    n=int(sys.argv[1]); cs=chunks(n)
    for i,c in enumerate(cs): open(os.path.join(OUT, f"ch{n:02d}_{i+1:02d}.txt"),"w").write(c)
    print(n,len(cs),sum(map(len,cs)))
