import random
from datetime import datetime

#    Génère un fichier de logs web avec 100 lignes
#    Une liste @IP, URLs, de codes de statut HTTP et d'agents utilisateurs est définie.
def generate_web_logs(filename="apache.log", n=65):
    ips = ["192.168.1.10", "203.0.113.5", "198.51.100.23", "192.0.2.45", "192.168.1.11"]
    urls = ["/index.html", "/notfound.html", "/login", "/admin", "/contact", "/robots.txt"]
    codes = ["200", "404", "403", "500"]
    agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Googlebot/2.1 (+http://www.google.com/bot.html)",
        "curl/7.68.0",
        "spiderbot/1.0",
        "HealthCheckBot/1.0"
    ]

    with open(filename, "w") as f:
        for _ in range(n):
            ip = random.choice(ips)
            url = random.choice(urls)
            code = random.choice(codes)
            agent = random.choice(agents)
            line = f"{ip} - - [{datetime.now().strftime('%d/%b/%Y:%H:%M:%S +0000')}] \"GET {url} HTTP/1.1\" {code} \"{agent}\"\n"
            f.write(line)
    print(f"{filename} généré avec {n} lignes.")
    
if __name__ == "__main__":
    generate_web_logs()