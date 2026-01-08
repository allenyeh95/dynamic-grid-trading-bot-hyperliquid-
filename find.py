import requests
import json

def get_hyperliquid_markets():
    """FIND Hyperliquid SYMBOL"""
    try:
       
        url = "https://api.hyperliquid.xyz/info"
       
        payload = {
            "type": "meta"
        }
        
        headers = {
            'Content-Type': 'application/json'
        }
        
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            
            if 'universe' in data:
                print("=== Hyperliquid  ===")
                print(f"TOTAL: {len(data['universe'])} SYMBOLS\n")
                
                for i, market in enumerate(data['universe'], 1):
                    name = market.get('name', 'Unknown')
                    print(f"{i:3}. {name}")
                
                return data['universe']
            else:
                print("DIDNOT FIND SYMBOLS")
                return None
        else:
            print(f"API ERROR: {response.status_code}")
            return None
            
    except Exception as e:
        print(f"ERROR: {e}")
        return None
    
if __name__ == "__main__":
    get_hyperliquid_markets()