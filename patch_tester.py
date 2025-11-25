import requests
import base64

# fetch original HTML
html = requests.get("http://127.0.0.1:5000/").text
print("Original HTML length:", len(html))

# modify HTML
html = "<br>Patched by patch_tester.py</br>" + html

# submit patched HTML
html_base64 = base64.b64encode(html.encode("utf-8")).decode("utf-8")
res = requests.post("http://127.0.0.1:5000/update_html", json={"html_base64": html_base64})
print("Update response:", res.json())