import json
import http.cookiejar
import os

def json_to_netscape(json_file, output_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        cookies_json = json.load(f)

    cookie_jar = http.cookiejar.MozillaCookieJar(output_file)

    for cookie in cookies_json:
        domain = cookie['Host raw'].lstrip('http://').lstrip('https://')
        initial_dot = domain.startswith('.')
        domain = domain.lstrip('.')
        expires = int(cookie['Expires raw'])
        
        cookie_item = http.cookiejar.Cookie(
            version=0,
            name=cookie['Name raw'],
            value=cookie['Content raw'],
            port=None,
            port_specified=False,
            domain=domain,
            domain_specified=True,
            domain_initial_dot=initial_dot,
            path=cookie['Path raw'],
            path_specified=True,
            secure=cookie['Send for'] == 'Encrypted connections only',
            expires=expires,
            discard=False,
            comment=None,
            comment_url=None,
            rest={'HttpOnly': cookie['HTTP only raw'] == 'true'},
            rfc2109=False
        )
        
        cookie_jar.set_cookie(cookie_item)

    cookie_jar.save(ignore_discard=True, ignore_expires=True)

# 使用脚本
json_file = 'cookies.json'  # 您的JSON文件路径
output_file = 'cookies.txt'  # 输出的Netscape格式文件路径

json_to_netscape(json_file, output_file)
print(f"Cookies已转换并保存到 {output_file}")
