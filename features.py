
from urllib.parse import urlparse

def extract_features(url):
    features = []
    parsed_url = urlparse(url)
    hostname = parsed_url.netloc
    path = parsed_url.path
    
    if len(url) > 54:
        features.append(1)
    else:
        features.append(0)
        
    if "@" in url:
        features.append(1)
    else:
        features.append(0)
        
    
    parts = hostname.split('.')
    is_ip = False
    if len(parts) == 4:
        
        if all(part.isdigit() for part in parts):
            is_ip = True
            
    if is_ip:
        features.append(1)
    else:
        features.append(0)
        
    if "https" in hostname:
        features.append(1)
    else:
        features.append(0)

    return features


safe_url = "https://www.google.com"
fake_url = "http://192.168.1.1/confirm-password"
suspicious_url = "http://paypal-secure-login.com@bad-actor.net"

print(f"URL: {safe_url} \nFeatures: {extract_features(safe_url)}\n")
print(f"URL: {fake_url} \nFeatures: {extract_features(fake_url)}\n")
print(f"URL: {suspicious_url} \nFeatures: {extract_features(suspicious_url)}")