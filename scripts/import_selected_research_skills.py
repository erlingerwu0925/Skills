#!/usr/bin/env python3
"""Vendor five public research Skill sources and expose categorized Codex entrypoints.
Imports upstream files only. Does not execute upstream scripts or install dependencies.
"""
import json, re, shutil, subprocess, tempfile
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
COL=ROOT/"collections"; TARGET=ROOT/".agents"/"skills"; CAT=ROOT/"categories"
LIMIT=25*1024*1024
SOURCES=[
 ("kd","K-Dense-AI/scientific-agent-skills","01-research-toolkit/K-Dense","skills",160,True),
 ("aris","wanshuiyin/Auto-claude-code-research-in-sleep","02-autonomous-research/ARIS","skills",70,False),
 ("ars","Imbad0202/academic-research-skills-codex","03-academic-paper/ARS-Codex","skills",1,False),
 ("rsk","YCC-Lover/research-starter-skills","04-research-starter/Research-Starter","skills",7,False),
 ("index","brycewang-stanford/Auto-Research-Skills","05-research-index/Auto-Research-Skills",None,0,False)]
TYPES={
 "01-literature":("文献检索与证据核验","literature arxiv scholar citation reference source search lookup bibliograph zotero reading openalex pubmed crossref deepxiv"),
 "02-research-design":("研究设计与假设","hypothes idea research-design experiment-plan experimental-design novelty protocol grant invention"),
 "03-data-experiments":("数据分析、工具与实验","experiment statistic data analysis benchmark model train compute genomic neuro protein chem molecular simulation matlab pymc bio gpu dataset lab torch"),
 "04-writing-review":("论文写作、汇报与评审","write paper review rebuttal manuscript poster slide presentation figure publish latex abstract format proofread"),
 "05-automation":("自动化科研与持续迭代","pipeline loop agent automation workflow autoskill meta refine monitor queue orchestrat academic-research-suite research-starter-paper"),
 "06-specialized":("专业领域及其他", "")}
def run(*args,cwd=None):
 return subprocess.run(args,cwd=cwd,text=True,capture_output=True,check=True).stdout.strip()
def copy_files(src,dst,skips=()):
 for p in src.rglob("*"):
  rel=p.relative_to(src)
  if any(z in {".git","__pycache__",".venv","node_modules",".pytest_cache"} for z in rel.parts):continue
  if rel.parts and rel.parts[0] in skips:continue
  if p.is_symlink():continue
  if not p.is_file():continue
  if p.stat().st_size>LIMIT:
   SKIPPED.append({"file":str(rel),"bytes":p.stat().st_size});continue
  to=dst/rel;to.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,to)
def extract_description(p):
 s=p.read_text(encoding="utf-8-sig",errors="replace")[:12000]
 m=re.search(r"(?m)^description:\s*(.*)$",s)
 if not m:return "科研任务辅助技能"
 line=m.group(1).strip()
 if line in ("|",">",">-","|-",""):
  bits=[]
  for q in s[m.end():].splitlines()[1:]:
   if not q.startswith((" ","\t")):break
   bits.append(q.strip())
  line=" ".join(bits)
 return " ".join(line.strip("'\" ").split())[:300]
def get_category(name):
 for key,(_,words) in TYPES.items():
  if any(w in name.lower() for w in words.split()):return key
 return "06-specialized"
def add_wrapper(sid,repo,orig,src_path):
 alias=orig if sid=="rsk" else sid+"-"+orig
 dest=TARGET/alias;dest.mkdir(parents=True,exist_ok=True)
 d=extract_description(ROOT/src_path)
 desc=(sid.upper()+" "+d).replace("\\","/")
 txt="---\nname: "+alias+"\ndescription: "+json.dumps(desc,ensure_ascii=False)+"\n---\n\n# "+alias+"\n\n"
 txt+="Read the complete, canonical upstream SKILL.md from this repository before doing any work: "
 txt+=src_path.as_posix()+". Its references, scripts, and sibling Skill paths must be resolved relative to that canonical file, not this entrypoint.\n\n"
 txt+="Respect its prerequisites and licenses. Do not invent references, outcomes, or test results. Do not execute third-party scripts without checking authorization and dependencies.\n\n"
 txt+="Original project: https://github.com/"+repo+"\n"
 (dest/"SKILL.md").write_text(txt,encoding="utf-8")
 return alias

SKIPPED=[]
def main():
 COL.mkdir(exist_ok=True);TARGET.mkdir(parents=True,exist_ok=True);CAT.mkdir(exist_ok=True)
 manifest=[];commits={}
 with tempfile.TemporaryDirectory(prefix="skill-import-") as temp:
  for sid,repo,dest_rel,skillroot,minimum,sparse in SOURCES:
   print("Fetching",repo,flush=True)
   work=Path(temp)/sid
   url="https://github.com/"+repo+".git"
   if sparse:
    run("git","clone","--quiet","--depth","1","--filter=blob:none","--sparse",url,str(work))
    run("git","sparse-checkout","set",skillroot,cwd=work)
   else:run("git","clone","--quiet","--depth","1","--filter=blob:none",url,str(work))
   commits[sid]=run("git","rev-parse","HEAD",cwd=work)
   dest=COL/dest_rel
   if dest.exists():shutil.rmtree(dest)
   dest.mkdir(parents=True)
   if sid=="index":
    copy_files(work,dest,skips=("skills","systems","benchmarks","site","showcase","tests","examples","deploy","assets",".github"))
    (dest/"INDEX-NOTE.md").write_text(
     "这是大型自动科研技能聚合库的实质目录资料。其 skills/ 和 systems/ 包含众多外部 Git 子模块，"
     "本次未把数千个外部项目逐项安装到 Codex。\n"
     "完整项目与递归下载方法：https://github.com/"+repo+
     "\n递归下载：git clone --recurse-submodules https://github.com/"+repo+".git\n",
     encoding="utf-8")
    continue
   copy_files(work,dest)
   base=dest/skillroot
   count=0
   for directory in sorted(base.iterdir()):
    if not directory.is_dir() or not (directory/"SKILL.md").is_file():continue
    file=Path("collections")/dest_rel/skillroot/directory.name/"SKILL.md"
    alias=add_wrapper(sid,repo,directory.name,file)
    manifest.append({"name":alias,"origin":repo,"origin_commit":commits[sid],
      "type":get_category(directory.name),"canonical":file.as_posix(),
      "entry":".agents/skills/"+alias+"/SKILL.md"})
    count+=1
   print("Imported",count,"from",repo,flush=True)
   if count<minimum:raise RuntimeError("Missing skills in "+repo+"; found "+str(count))
 for c,(title,_) in TYPES.items():
  folder=CAT/c;folder.mkdir(exist_ok=True)
  lines=["# "+title,"","真实技能文件按类型保存在 collections/，Codex 调用入口放在 .agents/skills/。",""]
  for obj in sorted([x for x in manifest if x["type"]==c],key=lambda x:x["name"]):
   lines.append("- "+obj["name"]+" — [入口](../../"+obj["entry"]+") | [原始内容](../../"+obj["canonical"]+")")
  (folder/"README.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
 (COL/"README.md").write_text(
  "# 已分类的五套科研项目\n\n"+
  "\n".join("- "+sid+": [上游](https://github.com/"+repo+")；类别 "+dest+
            ("；仅导入资源索引，非全部子模块" if sid=="index" else "")
            for sid,repo,dest,_,_,_ in SOURCES)+
  "\n\n.skill 已在 .agents/skills/ 中生成轻量入口；真正的 SKILL.md 和配套文件保留上游相对结构。\n",
  encoding="utf-8")
 (ROOT/"RESEARCH_SKILLS_MANIFEST.json").write_text(
  json.dumps({"sources":[{"id":x[0],"repository":x[1],"commit":commits[x[0]]} for x in SOURCES],
    "total_installed_entrypoints":len(manifest),"skills":manifest,
    "skipped_oversized_files":SKIPPED},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 (ROOT/"RESEARCH_SKILLS_README.md").write_text(
  "# 自动科研 Skill 分类库\n\n已按类别收藏 1 Scientific Agent Skills、4 ARIS、"
  "6 ARS-Codex、7 Research Starter Skills、8 Auto-Research-Skills。\n\n"
  "## 分类入口\n\n"+
  "\n".join("- [ "+title+" ](categories/"+c+"/README.md)" for c,(title,_) in TYPES.items())+
  "\n\n- [五个来源按套分类](collections/README.md)\n"
  "- [科研技能机器可读清单](RESEARCH_SKILLS_MANIFEST.json)\n\n"
  "目录 collections/ 中保留原始技能与相对引用结构；.agents/skills/ 为 Codex 技能发现创建别名入口。"
  "第 8 项属于聚合索引，非已安装数千个子技能。脚本、网络查询和依赖需要另外配置；"
  "本次导入只复制源文件，不执行未经审查的上游代码。\n",encoding="utf-8")
 print("DONE",len(manifest),"entrypoints,",len(SKIPPED),"large files omitted",flush=True)
 if len(manifest)<230:raise RuntimeError("Unexpectedly few source skill entrypoints")

if __name__=="__main__":main()
