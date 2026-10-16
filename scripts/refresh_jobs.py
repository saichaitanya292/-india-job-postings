"""Collect jobs from explicitly configured Greenhouse and Lever public boards."""
import json, os, re, urllib.request
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'data'/'jobs.json'
UA='IndiaJobHub/1.0 public job board feed collector'
INDIA=re.compile(r'india|hyderabad|bengaluru|bangalore|pune|chennai|mumbai|gurugram|gurgaon|noida|new delhi|delhi|kolkata|ahmedabad|kochi|remote',re.I)
def get_json(url):
 req=urllib.request.Request(url,headers={'User-Agent':UA,'Accept':'application/json'})
 with urllib.request.urlopen(req,timeout=25) as res:return json.loads(res.read().decode('utf-8'))
def category(title,text=''):
 s=(title+' '+text).lower()
 if re.search(r'\b(qa|quality|sdet|test automation|software tester|testing)\b',s):return 'QA & Testing'
 if re.search(r'machine learning|\bai\b|artificial intelligence|nlp|computer vision|deep learning|llm',s):return 'AI / Machine Learning'
 if re.search(r'data analyst|data scientist|analytics|data engineer|business intelligence',s):return 'Data & Analytics'
 if re.search(r'devops|cloud engineer|site reliability|platform engineer|kubernetes',s):return 'Cloud & DevOps'
 if re.search(r'software|developer|frontend|backend|full.?stack|java engineer|python engineer',s):return 'Software Engineering'
 return 'Other'
def fetch_greenhouse(board):
 data=get_json('https://boards-api.greenhouse.io/v1/boards/'+board+'/jobs?content=true');out=[]
 for j in data.get('jobs',[]):
  loc=(j.get('location') or {}).get('name','');title=j.get('title','')
  if not INDIA.search(loc):continue
  out.append({'id':'gh-'+board+'-'+str(j.get('id')),'title':title,'company':board.replace('-',' ').title(),'location':loc,'category':category(title,j.get('content','')),'posted':(j.get('updated_at') or '')[:10],'url':j.get('absolute_url',''),'source':'Greenhouse','description':re.sub('<[^>]+>',' ',j.get('content',''))[:1500]})
 return out
def fetch_lever(site):
 data=get_json('https://api.lever.co/v0/postings/'+site+'?mode=json');out=[]
 for j in data if isinstance(data,list) else []:
  loc=(j.get('categories') or {}).get('location','');title=j.get('text','')
  if not INDIA.search(loc):continue
  created=j.get('createdAt');posted=datetime.fromtimestamp(created/1000,timezone.utc).date().isoformat() if created else ''
  out.append({'id':'lever-'+site+'-'+str(j.get('id')),'title':title,'company':site.replace('-',' ').title(),'location':loc,'category':category(title,j.get('descriptionPlain','')),'posted':posted,'url':j.get('hostedUrl',''),'source':'Lever','description':(j.get('descriptionPlain') or '')[:1500]})
 return out
def main():
 jobs=[];failures=[]
 for board in filter(None,(x.strip() for x in os.getenv('GREENHOUSE_BOARDS','').split(','))):
  try:jobs.extend(fetch_greenhouse(board))
  except Exception as e:failures.append('Greenhouse '+board+': '+str(e))
 for site in filter(None,(x.strip() for x in os.getenv('LEVER_SITES','').split(','))):
  try:jobs.extend(fetch_lever(site))
  except Exception as e:failures.append('Lever '+site+': '+str(e))
 unique={j['url']:j for j in jobs if j.get('url')}
 if unique:
  ordered=sorted(unique.values(),key=lambda j:j.get('posted',''),reverse=True)
  OUT.write_text(json.dumps(ordered,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print('Wrote',len(ordered),'jobs from configured boards.')
 else:print('No real jobs collected. Configure GREENHOUSE_BOARDS and/or LEVER_SITES repository variables.')
 for failure in failures:print('WARNING:',failure)
if __name__=='__main__':main()
