import re
import requests

def is_suspicious(url):
    """Check if a URL has suspicious patterns"""
    phishing_patterns = [
        r"\.xyz$", r"\.top$", r"\.club$", r"\.info$",  # Common phishing domains
        r"free-", r"login-", r"-secure", r"verify-",  # Suspicious keywords
        r"[0-9]{5,}"  # Too many numbers in domain
    ]
    
    for pattern in phishing_patterns:
        if re.search(pattern, url):
            return True
    return False

def check_website(url):
    """Check website safety"""
    try:
        response = requests.get(url, timeout=5)
        status = response.status_code
        if status == 200:
            print(f"✅ {url} is accessible.")
            if is_suspicious(url):
                print("⚠️ Warning: This site may be a phishing site!")
            else:
                print("🛡️ This site looks safe.")
        else:
            print(f"❌ {url} is unreachable (Status Code: {status}).")
    except requests.RequestException:
        print(f"❌ Could not connect to {url}. It may be offline or dangerous.")

if __name__ == "__main__":
    url = input("🔗 Enter website URL (e.g., https://example.com): ")
    check_website(url)
