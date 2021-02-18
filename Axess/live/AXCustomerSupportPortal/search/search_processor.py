log = contanier.logit
log("/live/AXCustomerSupportPortal/search/search_processor")

CM = container.CPEManager
request = container.REQUEST
run_sql = CM.manage_runSQL
prefix_sql_ids = "select cpeid from CPEManager_CPEs "
prefix_sql_cnt = "select count(1) from CPEManager_CPEs "
sql = ""
cpeident = params['CPESearchOptions']
where = []
args = ()
for ident in ('cpeid', 'cid', 'cid2','path','comments'):
  if cpeident.get(ident):
    where.append(
      "ident = %s".replace('ident', ident)
    )
    value = cpeident.get(ident)
    #IA custom hack to allow any MAC address writing
    if ident == 'cid2':
      value = value.replace(':','').replace('-','').lower()
    args = args + (value,)

for ident in ('ip',):
  if cpeident.get(ident):
    val = cpeident.get(ident)
    if val.endswith('*'):
      where.append(
        "ident LIKE %s".replace('ident', ident)
      )
      args = args + (val[:-1] + '%%',)
    else:
      where.append(
        "ident = %s".replace('ident', ident)
      )
      args = args + (val,)

valNum = 3
for ident in ('login', 'account', 'connectionID'):
  if cpeident.get(ident):
    val = cpeident.get(ident)
    cid = container.CPEManager.manage_runSQL(container.REQUEST,
                                             'select cid from AXServiceTable where value%s="%s";'% (valNum,val)
                                             )
    if cid:
      cid = cid[0][0]
      where.append(
        'cid = %s'
      )
      args = args + (cid,)
    else:
      raise Exception('Test')
valNum += 1

crit = []
if cpeident.get('any_param'):
  for ident in ('cpeid','ip','cid','cid2','path'):
    val = cpeident.get('any_param')
    crit.append(
      "ident LIKE %s".replace('ident', ident)
    )
    if ident == 'cid2':
      val = val.replace(':','').replace('-','').lower()
    args = args + ('%' + val + '%',)
  where.append(' OR '.join(crit))
if where:
  sql += ' where ' + ' AND '.join(where)

#IA: sort: latest arrival top
sql += ' order by lastMsg desc '

count = run_sql(None, prefix_sql_cnt + sql, args)[0][0]

limit = params['CommandOptions'].get('limit', 10)

if limit is not None:
  sql += ' limit %s'
  args = args + (limit,)

offset = params['CommandOptions'].get('offset', None)
if offset is not None:
  sql += ' offset %s'
  args = args + (offset,)

cpes = run_sql(None, prefix_sql_ids+sql, args)
cpes = [cpe[0] for cpe in cpes]
return count, cpes
