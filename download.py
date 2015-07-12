import vlermv, requests
@vlermv.cache('~/evolução-de-emprego')
def relatório(ano, mes, viewstate = None, jsessionid = None):
    '''
    >>> relatório(2014, 6, viewstate = 'j_id7021:j_id7024', jsessionid = 'D16B8DD8F15C2D2C9E45BB0C48286824.lbroute_v321p000')
    '''
    url = 'http://bi.mte.gov.br/eec/pages/consultas/evolucaoEmprego/consultaEvolucaoEmprego.xhtml'
    headers = {
        'Host': 'bi.mte.gov.br',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:39.0) Gecko/20100101 Firefox/39.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'http://bi.mte.gov.br/eec/pages/consultas/evolucaoEmprego/consultaEvolucaoEmprego.xhtml',
        'Cookie': 'JSESSIONID=%s; style=null' % jsessionid,
        'Connection': 'keep-alive',
    }
    data = {
        'j_id15': 'j_id15',
        'j_id15:mesSelected': '%02d' % mes,
        'j_id15:anoSelected': ano,
        'j_id15:nivelSetor': 'Brasil',
        'j_id15:j_id105': 'Gerar+Relat%F3rio',
        'j_id15:subsetor': '',
        'j_id15:setor': '',
        'javax.faces.ViewState': viewstate,
    }
    return requests.post(url, headers = headers, data = data)
