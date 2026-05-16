import urllib.request
import urllib.parse
import hashlib
import os
import json
import gzip

api_interpreter_url = "https://overpass.kumi.systems/api/interpreter"
CACHE_DIR = "cache"

def getRoadList(lat, lon, diam):
    os.makedirs(CACHE_DIR, exist_ok=True)
    hash_key = hashlib.md5(f"{lat}_{lon}_{diam}".encode()).hexdigest()
    cache_file = os.path.join(CACHE_DIR, f"roads_{hash_key}.json")

    if os.path.exists(cache_file):
        print(f"Cache trouvé : {cache_file}")
        with open(cache_file, "r") as f:
            return json.load(f)

    query = (
        f"[out:json][timeout:60];"
        f"way[\"highway\"~\"motorway|trunk|primary|secondary|tertiary|residential|living_street|unclassified\"]"
        f"(around:{int(diam)},{lat},{lon});"
        f"out geom;"
    )

    encoded = urllib.parse.urlencode({"data": query}).encode("utf-8")

    req = urllib.request.Request(
        api_interpreter_url,
        data=encoded,
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:150.0) Gecko/20100101 Firefox/150.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "fr,fr-FR;q=0.9,en-US;q=0.8,en;q=0.7",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1"
        }
    )

    with urllib.request.urlopen(req) as response:
        raw = response.read()
        if response.info().get("Content-Encoding") == "gzip":
            raw = gzip.decompress(raw)
        data = json.loads(raw.decode("utf-8"))

    with open(cache_file, "w") as f:
        json.dump(data, f)

    print(f"Cache sauvegardé : {cache_file}")

    return data