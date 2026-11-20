"""Copy legacy data/workflows into Studio; dry-run by default, never overwrite."""
import argparse,json,shutil,sys
from pathlib import Path
IDS={name:'PromptMageStudio'+name.removeprefix('DanbooruTagsTransformer') for name in ['DanbooruTagsTransformer'+s for s in ['Grimoire','GrimoireTurn','SpellScroll','Foundry','FoundryPlan','FoundryReviewSaved','FoundryReviewOutput','GrimoireBrief','ArchmageBeta','AppearanceOverrides','Resolution','ImageBatchUpload','ImageBatchSelector']]}
def convert(value):
    if isinstance(value,list):return [convert(x) for x in value]
    if isinstance(value,dict):return {k:IDS.get(v,v) if k in ('type','class_type') and isinstance(v,str) else convert(v) for k,v in value.items()}
    return value
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--user-directory',type=Path,required=True);p.add_argument('--apply',action='store_true');p.add_argument('--include-keys',action='store_true');a=p.parse_args()
    source=a.user_directory/'prompt_mage';target=a.user_directory/'prompt_mage_studio';copied=skipped=0
    if source.exists():
        for f in source.rglob('*'):
            if not f.is_file():continue
            relative=f.relative_to(source)
            if 'credentials' in relative.parts and not a.include_keys:continue
            out=target/relative
            if out.exists():skipped+=1;continue
            copied+=1
            if not a.apply:continue
            out.parent.mkdir(parents=True,exist_ok=True)
            if f.suffix=='.json' and 'credentials' not in relative.parts:
                out.write_text(json.dumps(convert(json.loads(f.read_text(encoding='utf-8'))),ensure_ascii=False,indent=2),encoding='utf-8')
            else:shutil.copy2(f,out)
            if 'credentials' in relative.parts:out.chmod(0o600)
    workflows=a.user_directory/'default'/'workflows'
    for f in workflows.glob('*.json'):
        raw=json.loads(f.read_text(encoding='utf-8'));new=convert(raw)
        if new==raw:continue
        out=f.with_name(f.stem+' - Studio.json')
        if out.exists():skipped+=1;continue
        copied+=1
        if a.apply:out.write_text(json.dumps(new,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'mode':'apply' if a.apply else 'dry-run','new_files':copied,'existing_files_skipped':skipped,'keys_included':a.include_keys}))
if __name__=='__main__':main()
